#!/usr/bin/env python3
"""Cadeado do HUB | SYNDEX — tranca as páginas do portal com senha.

Cada página vira uma tela de senha que guarda o conteúdo original criptografado
(AES-256-GCM, chave derivada da senha com PBKDF2-SHA256). Sem a senha, o conteúdo
publicado no GitHub é ilegível. A senha NUNCA é gravada em arquivo.

Uso (a senha vem da variável HUB_SENHA ou é pedida no terminal):
    python3 _cadeado/cadeado.py trancar     # criptografa as páginas abertas
    python3 _cadeado/cadeado.py abrir       # devolve o conteúdo original, para editar
    python3 _cadeado/cadeado.py verificar   # confere que nada ficou aberto sem querer
    python3 _cadeado/cadeado.py nova-senha  # gera sal novo (use ao trocar a senha)

Fluxo para editar: abrir → editar → trancar → verificar → commit.
Nunca faça commit com páginas abertas: rode "verificar" antes.
"""
import base64, getpass, hashlib, html, json, os, re, secrets, sys
from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

RAIZ = Path(__file__).resolve().parent.parent
CONFIG = Path(__file__).resolve().parent / 'config.json'
MARCA = '<meta name="hub-cadeado" content="v1">'
CHAVE_LOCAL = 'hubsyndex.chave.v1'


def ler_config():
    return json.loads(CONFIG.read_text(encoding='utf-8'))


def gravar_config(cfg):
    CONFIG.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def paginas(cfg):
    abertas = set(cfg['abertas'])
    for p in sorted(RAIZ.rglob('*.html')):
        rel = p.relative_to(RAIZ).as_posix()
        if rel.startswith(('.git/', '_cadeado/')) or rel in abertas:
            continue
        yield p, rel


def pedir_senha(confirmar=False):
    senha = os.environ.get('HUB_SENHA')
    if senha is None:
        senha = getpass.getpass('Senha do HUB: ')
        if confirmar and getpass.getpass('Repita a senha: ') != senha:
            sys.exit('As senhas não conferem.')
    if len(senha) < 12:
        sys.exit('A senha precisa ter pelo menos 12 caracteres.')
    return senha


def derivar(senha, cfg):
    sal = base64.b64decode(cfg['sal'])
    return hashlib.pbkdf2_hmac('sha256', senha.encode('utf-8'), sal, cfg['iteracoes'], 32)


def b64(b):
    return base64.b64encode(b).decode('ascii')


def cabeca_util(original):
    """Copia do original só o que o navegador precisa antes de abrir: ícones, manifest, cor."""
    m = re.search(r'<head[^>]*>(.*?)</head>', original, re.S | re.I)
    trecho = m.group(1) if m else original[:4000]
    tags = re.findall(r'<link\s[^>]*rel="?(?:icon|apple-touch-icon|manifest)"?[^>]*>', trecho, re.I)
    tags += re.findall(r'<meta\s[^>]*name="?(?:theme-color|apple-mobile-web-app-[a-z-]+|mobile-web-app-capable|application-name)"?[^>]*>', trecho, re.I)
    return '\n'.join(dict.fromkeys(tags))


MODELO = open(Path(__file__).resolve().parent / 'tela.html', encoding='utf-8').read()


def trancar_pagina(texto, rel, chave, cfg):
    if MARCA in texto:
        return None  # já trancada
    iv = secrets.token_bytes(12)
    ct = AESGCM(chave).encrypt(iv, texto.encode('utf-8'), None)
    pre = '../' * rel.count('/')
    extra = cabeca_util(texto)
    if 'rel="icon"' not in extra and "rel=icon" not in extra:
        extra = f'<link rel="icon" type="image/png" href="{pre}icon-192.png">\n' + extra
    return (MODELO
            .replace('{{MARCA}}', MARCA)
            .replace('{{TITULO}}', 'HUB | SYNDEX')  # nome da ferramenta só aparece depois da senha
            .replace('{{CABECA}}', extra)
            .replace('{{PRE}}', pre)
            .replace('{{SAL}}', cfg['sal'])
            .replace('{{ITER}}', str(cfg['iteracoes']))
            .replace('{{IV}}', b64(iv))
            .replace('{{CT}}', b64(ct))
            .replace('{{CHAVE_LOCAL}}', CHAVE_LOCAL))


def abrir_pagina(texto, chave):
    if MARCA not in texto:
        return None
    iv = re.search(r'iv:"([A-Za-z0-9+/=]+)"', texto).group(1)
    ct = re.search(r'ct:"([A-Za-z0-9+/=]+)"', texto).group(1)
    return AESGCM(chave).decrypt(base64.b64decode(iv), base64.b64decode(ct), None).decode('utf-8')


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ('trancar', 'abrir', 'verificar', 'nova-senha'):
        sys.exit(__doc__)
    cmd = sys.argv[1]
    cfg = ler_config()

    if cmd == 'verificar':
        abertas = [rel for p, rel in paginas(cfg) if MARCA not in p.read_text(encoding='utf-8')]
        if abertas:
            sys.exit('ATENÇÃO, páginas sem senha: ' + ', '.join(abertas))
        print('ok: todas as páginas estão trancadas (abertas de propósito: ' + ', '.join(cfg['abertas']) + ')')
        return

    if cmd == 'nova-senha':
        cfg['sal'] = b64(secrets.token_bytes(16))
        gravar_config(cfg)
        print('sal novo gravado; agora rode "trancar" com a senha nova (as páginas precisam estar abertas)')
        return

    chave = derivar(pedir_senha(confirmar=(cmd == 'trancar')), cfg)
    if cmd == 'trancar':
        # se já há página trancada, a senha tem que ser a mesma delas
        for p, rel in paginas(cfg):
            texto = p.read_text(encoding='utf-8')
            if MARCA in texto:
                try:
                    abrir_pagina(texto, chave)
                except Exception:
                    sys.exit(f'Essa senha não é a mesma usada em {rel}. Nada foi alterado.')
                break
    feitas = 0
    for p, rel in paginas(cfg):
        texto = p.read_text(encoding='utf-8')
        try:
            novo = trancar_pagina(texto, rel, chave, cfg) if cmd == 'trancar' else abrir_pagina(texto, chave)
        except Exception:
            sys.exit(f'Senha errada (não abriu {rel}). Nada mais foi alterado a partir daqui.')
        if novo is not None:
            p.write_text(novo, encoding='utf-8')
            feitas += 1
    print(f'{cmd}: {feitas} página(s)')


if __name__ == '__main__':
    main()

# Regras deste repositório (HUB | SYNDEX)

- As páginas `*.html` (menos `cotacao/index.html`) estão **trancadas com senha**: o conteúdo é criptografado pelo `_cadeado/cadeado.py`. Veja a seção "Senha (cadeado)" do README.
- Para editar uma página, peça a senha ao Tomás e use `abrir` → editar → `trancar` → `verificar`, passando a senha pela variável `HUB_SENHA` só no comando. **Nunca** grave a senha em arquivo, commit, memória ou mensagem de commit.
- **Nunca faça commit com página aberta.** Rode `python3 _cadeado/cadeado.py verificar` antes de todo commit; se ele acusar página sem senha, tranque antes.
- Página nova também precisa ser trancada (o `trancar` pega todas as páginas, menos as listadas em `_cadeado/config.json` → `abertas`).

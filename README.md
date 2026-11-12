# Portal Syndex

Portal interno com as ferramentas da **Syndex Logística e Gestão Aduaneira** em um só lugar.

**Abrir o portal:** https://tomsoares10-dev.github.io/portal-syndex/

**Site da Syndex:** https://syndex.com.br/

Funciona no computador e no celular. No celular dá para instalar como app:

- **Android (Chrome):** menu ⋮ → *Instalar app* ou *Adicionar à tela inicial*.
- **iPhone (Safari):** Compartilhar → *Adicionar à Tela de Início*.

## Ferramentas

| Seção | Ferramenta | Onde abre |
|---|---|---|
| Clientes | Syndex Ações | Portal (`/acoes`, dados salvos no aparelho) |
| Clientes | Carteira por estado | Claude |
| Clientes | Clientes Ativos | Claude (documento) |
| Clientes | Diário de Visitas | Portal (`/visitas`, dados salvos no aparelho) |
| Clientes | Syndex Chat | Portal (`/chat`, protótipo) |
| Cotações e propostas | Syndex Cotações | Portal (`/cotacao-frete`, em branco) |
| Cotações e propostas | Solicitação para Pricing | Portal (`/pricing`) |
| Cotações e propostas | Gerador de propostas | Portal (`/propostas`) |
| Cotações e propostas | Propostas Compactas | Portal (`/propostas-compactas`, proposta de serviços aduaneiros em PDF no timbrado) |
| Cotações e propostas | Proposta TTD | Site (GitHub, `syndex-proposta-ttd`) |
| Cotações e propostas | Dados da proposta | Site (GitHub, `syndex-dados-proposta`) |
| Cotações e propostas | Estimativa de custo | Portal (`/estimativa`) |
| Cotações e propostas | Mini proposta rodoviária | Portal (`/mini-proposta`) |
| Cotações e propostas | Cupom Especial | Portal (`/cupom`) |
| Cotações e propostas | Programa de Indicação | Portal (`/indicacao`, proposta one-page com botão de imprimir/PDF) |
| Cotações e propostas | Carta de Benefício | Portal (`/carta-beneficio`, carta animada por link + imagem e PDF de 1 página) |
| Rotina | Despesas de viagem | Site (GitHub) |
| Rotina | Syndex Reposição | Portal (`/reposicao`, marcações salvas no aparelho) |
| Rotina | Foto de grupo WhatsApp | Site (GitHub) |
| Para o cliente | Peça sua cotação | Portal (`/cotacao`) |
| Para o cliente | Passaporte Syndex | Portal (`/passaporte`, carimbos salvos no aparelho do cliente) |

As ferramentas que abrem no Claude são links privados: só funcionam para quem recebeu acesso.

## Estrutura

- `index.html` — o portal (menu, busca, cards e links)
- `cotacao/` — página pública Peça sua cotação: gera a ficha do pedido em foto (ícone e cor por modal, cartão de contato) e envia pelo WhatsApp em 2 passos; `preview.jpg` é a imagem de prévia do link
- `passaporte/` — página pública Passaporte Syndex: o cliente emite o passaporte e registra todo mês, pela referência da proposta, quantos processos de desembaraço (1 carimbo por processo) e contêineres de frete (1 carimbo por contêiner) fez; pode carimbar várias vezes e enviar tudo junto e envia a imagem e a mensagem pelo WhatsApp do Tomás; com 10 carimbos abre a página secreta com o prêmio; `preview.jpg` é a imagem de prévia do link
- `pricing/` — Solicitação para Pricing (gera o PDF ou a imagem para mandar no WhatsApp)
- `estimativa/` — Estimativa de custo de importação (gera o PDF)
- `cotacao-frete/` — Syndex Cotações, cotação de frete marítimo em PDF (modelo em branco)
- `propostas/` — Gerador de propostas comerciais em PDF (vendedor: Tomás Soares)
- `propostas-compactas/` — Propostas Compactas: um PDF no timbrado com os serviços escolhidos para o mesmo cliente (desembaraço de importação e de exportação, TTD, Radar Siscomex e registro no MAPA), cada um liga/desliga; rascunho salvo no aparelho
- `visitas/` — Diário de Visitas: agenda, anotações, próximos passos e relatório do mês (dados no aparelho)
- `chat/` — Syndex Chat, protótipo do WhatsApp comercial (dados de exemplo)
- `mini-proposta/` — Mini proposta de frete rodoviário em PDF, com rota e mini mapa
- `cupom/` — Cupom Especial (honorário zero, código CUSTOMS-FREE): nome da empresa na frente; nome, cargo, WhatsApp e e-mail de quem envia no verso (salvos no aparelho); quantidade de processos com honorário zero e estilo do cartão (Azul e verde, Black ou Dourado), livres para qualquer quantidade; GIF animado sem fundo para o e-mail e GIF com fundo branco para o WhatsApp, PNG com frente e verso e link do WhatsApp de quem envia
- `carta-beneficio/` — Carta de Benefício: campos personalizáveis (contato, empresa, logo do cliente, modelo câmbio PTAX ou livre, destaque, serviços, regra, selo da Diretoria liga/desliga, textos e assinatura); baixa a página de 1 folha em imagem (PNG) e PDF e gera o link da carta animada. Os dados da carta vão dentro do próprio link (nada fica salvo); a carta abre no site `syndex-beneficios.github.io/carta/` (repositório `syndex-beneficios/carta`). Rascunho salvo no aparelho
- `assets/` — logo, símbolo e fundo da marca Syndex
- `manifest.webmanifest`, `sw.js`, `icon-*.png`, `apple-touch-icon.png` — para instalar como app

Para trocar o link de uma ferramenta, edite o `href` do card dela no `index.html`.

## Senha (cadeado)

O HUB e todas as ferramentas deste repositório abrem só com a senha do Tomás. As únicas páginas abertas de propósito são `cotacao/` (Peça sua cotação) e `passaporte/` (Passaporte Syndex), feitas para os clientes.

- Cada página publicada é uma tela de senha com o conteúdo original **criptografado** (AES-256-GCM, chave derivada da senha com PBKDF2-SHA256, 600 mil iterações). Sem a senha, o que está no GitHub é ilegível.
- A senha **não fica gravada em lugar nenhum** do repositório. No aparelho, "Lembrar neste aparelho" guarda só a chave derivada no navegador; abrir qualquer página com `?sair` no fim do endereço faz o aparelho esquecer.
- Os sites separados (Despesas, Proposta TTD, Foto de grupo, Dados da proposta) ficam em outros repositórios e **não** têm senha.

Para editar uma página (precisa da senha):

```
python3 _cadeado/cadeado.py abrir      # devolve o conteúdo original no seu computador
# ... editar ...
python3 _cadeado/cadeado.py trancar    # criptografa de novo (inclui páginas novas)
python3 _cadeado/cadeado.py verificar  # confere que nada ficou sem senha — rode antes de todo commit
```

Para trocar a senha: `abrir` com a senha antiga, `nova-senha`, `trancar` com a senha nova.


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
| Clientes | Syndex Ações | Claude |
| Clientes | Carteira por estado | Claude |
| Clientes | Clientes Ativos | Claude (documento) |
| Clientes | Diário de Visitas | Portal (`/visitas`, dados salvos no aparelho) |
| Clientes | Syndex Chat | Portal (`/chat`, protótipo) |
| Cotações e propostas | Syndex Cotações | Portal (`/cotacao-frete`, em branco) |
| Cotações e propostas | Solicitação para Pricing | Portal (`/pricing`) |
| Cotações e propostas | Gerador de propostas | Portal (`/propostas`) |
| Cotações e propostas | Proposta TTD | Site (GitHub, `syndex-proposta-ttd`) |
| Cotações e propostas | Estimativa de custo | Portal (`/estimativa`) |
| Cotações e propostas | Mini proposta rodoviária | Portal (`/mini-proposta`) |
| Cotações e propostas | Cupom Especial | Portal (`/cupom`) |
| Cotações e propostas | Programa de Indicação | Claude (documento) |
| Rotina | Despesas de viagem | Site (GitHub) |
| Rotina | Syndex Reposição | Claude |
| Rotina | Foto de grupo WhatsApp | Site (GitHub) |
| Para o cliente | Peça sua cotação | Portal (`/cotacao`) |

As ferramentas que abrem no Claude são links privados: só funcionam para quem recebeu acesso.

## Estrutura

- `index.html` — o portal (menu, busca, cards e links)
- `cotacao/` — página pública Peça sua cotação: gera a ficha do pedido em foto (ícone e cor por modal, cartão de contato) e envia pelo WhatsApp em 2 passos; `preview.jpg` é a imagem de prévia do link
- `pricing/` — Solicitação para Pricing (gera o PDF)
- `estimativa/` — Estimativa de custo de importação (gera o PDF)
- `cotacao-frete/` — Syndex Cotações, cotação de frete marítimo em PDF (modelo em branco)
- `propostas/` — Gerador de propostas comerciais em PDF (vendedor: Tomás Soares)
- `visitas/` — Diário de Visitas: agenda, anotações, próximos passos e relatório do mês (dados no aparelho)
- `chat/` — Syndex Chat, protótipo do WhatsApp comercial (dados de exemplo)
- `mini-proposta/` — Mini proposta de frete rodoviário em PDF, com rota e mini mapa
- `cupom/` — Cupom Especial (honorário zero, código CUSTOMS-FREE): nome da empresa na frente; nome, cargo, WhatsApp e e-mail de quem envia no verso (salvos no aparelho); GIF animado sem fundo para o e-mail, PNG com frente e verso e link do WhatsApp de quem envia
- `assets/` — logo, símbolo e fundo da marca Syndex
- `manifest.webmanifest`, `sw.js`, `icon-*.png`, `apple-touch-icon.png` — para instalar como app

Para trocar o link de uma ferramenta, edite o `href` do card dela no `index.html`.

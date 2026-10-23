# Portal Syndex

Portal interno com as ferramentas da **Syndex Logística e Gestão Aduaneira** em um só lugar.

**Abrir o portal:** https://tomsoares10-dev.github.io/portal-syndex/

Funciona no computador e no celular. No celular dá para instalar como app:

- **Android (Chrome):** menu ⋮ → *Instalar app* ou *Adicionar à tela inicial*.
- **iPhone (Safari):** Compartilhar → *Adicionar à Tela de Início*.

## Ferramentas

| Seção | Ferramenta | Onde abre |
|---|---|---|
| Clientes | Syndex Ações | Claude |
| Clientes | Carteira por estado | Claude |
| Cotações e propostas | Syndex Cotações | Portal (`/cotacao-frete`, em branco) |
| Cotações e propostas | Solicitação para Pricing | Portal (`/pricing`) |
| Cotações e propostas | Gerador de propostas | Em breve |
| Cotações e propostas | Estimativa de custo | Portal (`/estimativa`) |
| Rotina | Despesas de viagem | Site (GitHub) |
| Rotina | Syndex Reposição | Claude |
| Rotina | Foto de grupo WhatsApp | Site (GitHub) |
| Para o cliente | Peça sua cotação | Portal (`/cotacao`) |

As ferramentas que abrem no Claude são links privados: só funcionam para quem recebeu acesso.

## Estrutura

- `index.html` — o portal (menu, busca, cards e links)
- `cotacao/` — página pública Peça sua cotação (o pedido vai pelo WhatsApp)
- `pricing/` — Solicitação para Pricing (gera o PDF)
- `estimativa/` — Estimativa de custo de importação (gera o PDF)
- `cotacao-frete/` — Syndex Cotações, cotação de frete marítimo em PDF (modelo em branco)
- `assets/` — logo, símbolo e fundo da marca Syndex
- `manifest.webmanifest`, `sw.js`, `icon-*.png`, `apple-touch-icon.png` — para instalar como app

Para trocar o link de uma ferramenta, edite o `href` do card dela no `index.html`.

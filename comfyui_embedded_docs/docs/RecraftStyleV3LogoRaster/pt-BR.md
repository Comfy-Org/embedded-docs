# Recraft Estilo - Logo Raster

Este nó seleciona o estilo raster de logotipo e um subestilo para gerar imagens de logotipo. Ele é especializado na criação de designs de logotipo com tratamentos visuais baseados em raster.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `subestilo` | O subestilo raster de logotipo específico a ser aplicado para a geração do logotipo | STRING | Sim | `"bold"`<br>`"minimal"`<br>`"vibrant"`<br>`"handdrawn"`<br>`"geometric"`<br>`"vintage"`<br>`"neon"`<br>`"gradient"`<br>`"flat"`<br>`"outline"`<br>`"mascot"`<br>`"badge"`<br>`"abstract"`<br>`"retro"`<br>`"modern"`<br>`"playful"`<br>`"luxury"`<br>`"tech"`<br>`"nature"`<br>`"food"`<br>`"sport"`<br>`"fashion"`<br>`"music"`<br>`"travel"`<br>`"education"`<br>`"health"`<br>`"finance"`<br>`"realestate"`<br>`"nonprofit"` |

Nota: Um subestilo deve ser sempre selecionado; não há opção "none".

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `recraft_style` | A configuração de estilo Recraft selecionada, incluindo o estilo raster de logotipo e o subestilo escolhido | CUSTOM |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3LogoRaster/pt-BR.md)

---
**Source fingerprint (SHA-256):** `59c3af980261d2b20b6d401980639c6bbc3a8b7c4e2370ca048ccb07535b10e7`

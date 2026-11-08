# OpenAI GPT Image 2.6 SVG

## Visão geral

OpenAI GPT Image 2.6 SVG gera um SVG editável a partir de um prompt com os modelos GPT Image da OpenAI. O resultado é marcação vetorial, então formas e texto permanecem editáveis em um editor vetorial. Dois modelos estão disponíveis: `gpt-image-2.6-flare` e `gpt-image-2.6-sunburst`.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo GPT Image a usar para o SVG. | DYNAMIC_COMBO | Sim | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"` |

### Entradas do gpt-image-2.6-flare e do gpt-image-2.6-sunburst

Ambos os modelos compartilham os mesmos parâmetros.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model.prompt` | Descrição do SVG a desenhar. (padrão: `""`) | STRING | Sim | N/A |
| `model.size` | Tamanho da imagem de referência a partir da qual o SVG é desenhado. (padrão: `"1024x1024"`) | COMBO | Sim | `"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | Fundo da imagem de referência. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Qualidade da imagem de referência a partir da qual o SVG é desenhado. (padrão: `"low"`) | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | Quanto o modelo planeja a imagem de referência antes da renderização. (padrão: `"high"`) | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |
| `model.seed` | Controla se o nó é executado novamente; os resultados não são determinísticos independentemente da seed. (padrão: `42`) | INT | Sim | 0 a 2147483647 |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `svg` | A imagem vetorial gerada como marcação SVG. | SVG |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageSVGNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8ac2f473b265d3b6857e6280a1c017301b124fc6d671ec83a59c677218062c90`

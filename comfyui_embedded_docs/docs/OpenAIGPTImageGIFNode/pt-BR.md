# OpenAI GPT Image 2.6 GIF

## Visão geral

O OpenAI GPT Image 2.6 GIF gera um GIF animado a partir de um prompt com os modelos GPT Image da OpenAI e o retorna como um lote de quadros mais a taxa de quadros, para que possa ir diretamente para um nó de salvamento de vídeo ou de imagem animada. Dois modelos estão disponíveis: `gpt-image-2.6-flare` e `gpt-image-2.6-sunburst`.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo GPT Image a usar para a animação. | DYNAMIC_COMBO | Sim | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"` |

### Entradas do gpt-image-2.6-flare e do gpt-image-2.6-sunburst

Ambos os modelos compartilham os mesmos parâmetros.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model.prompt` | O que animar. (padrão: `""`) | STRING | Sim | N/A |
| `model.size` | Tamanho de cada quadro. Tamanhos maiores só comportam contagens de quadros menores. (padrão: `"512x512"`) | COMBO | Sim | `"384x384"`<br>`"512x512"`<br>`"640x640"`<br>`"720x720"`<br>`"768x768"`<br>`"960x960"`<br>`"512x288"`<br>`"288x512"`<br>`"1024x576"`<br>`"576x1024"`<br>`"1280x720"`<br>`"720x1280"` |
| `model.frame_count` | Número de quadros. Os quadros são cobrados em faixas: 2 a 8, 9, 10 a 12, 13 a 16. (padrão: `9`) | INT | Sim | 2 a 16 |
| `model.frame_duration_ms` | Por quanto tempo cada quadro é exibido, em milissegundos. (padrão: `200`) | INT | Sim | 20 a 2000 (passo 10) |
| `model.background` | Fundo do quadro. A transparência é mantida por Save WEBM com vp9, Save Animated WEBP e Save Animated PNG. (padrão: `"opaque"`) | COMBO | Sim | `"opaque"`<br>`"transparent"` |
| `model.quality` | Qualidade da imagem. Níveis mais altos custam mais e demoram mais. (padrão: `"low"`) | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | Quanto o modelo planeja a animação antes de renderizar. (padrão: `"high"`) | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |
| `model.seed` | Controla se o nó é executado novamente; os resultados são não determinísticos independentemente da seed. (padrão: `42`) | INT | Sim | 0 a 2147483647 |

**Restrições e limitações dos parâmetros:**

- A taxa de quadros é calculada a partir de `model.frame_duration_ms`: 200 ms resultam em 5 fps.
- Um `model.size` grande combinado com um `model.frame_count` alto não está disponível e mostra "Tamanho grande demais para esta contagem de quadros" no selo de preço.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `frames` | A animação como um lote de quadros, pronta para um nó de salvamento de vídeo ou de imagem animada. | IMAGE |
| `fps` | Quadros por segundo, lidos da duração dos quadros do GIF retornado. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageGIFNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e47ebaef90f8b2618ef3c2659778f75ac9763013dcc515ba5650764ce49da951`

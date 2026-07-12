# Criar Caixas Delimitadoras

Desenhe caixas delimitadoras em uma tela. Gera elementos de prompt Ideogram, caixas delimitadoras em espaço de pixels e uma imagem de pré-visualização.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `fundo` | Imagem opcional usada como fundo na tela e na pré-visualização. | IMAGE | No | - |
| `bboxes` | Bounding boxes, elements, or a JSON string to initialize the canvas. A new upstream value initializes the canvas; edits made on the canvas take priority and are kept until the upstream value changes again. | BOUNDING_BOX, ARRAY, STRING | No | - |
| `largura` | Largura da tela e da grade de pixels para as caixas delimitadoras. | INT | Yes | 64 to 16384 (step: 16) |
| `altura` | Altura da tela e da grade de pixels para as caixas delimitadoras. | INT | Yes | 64 to 16384 (step: 16) |
| `estado_do_editor` | Desenhe caixas delimitadoras e defina o tipo de cada caixa, texto, descrição, paleta de cores. Comece pelo elemento de fundo e termine pelo primeiro plano. | BOUNDING_BOXES | Yes | - |
| `last_incoming` | Internal state managed by the canvas: the upstream bboxes value that last initialized it. Leave empty to re-initialize the canvas from the bboxes input on the next run. | BOUNDING_BOXES | No | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `preview` | An RGB image showing the canvas with all bounding boxes rendered, including labels, color palette swatches, and descriptive text. | IMAGE |
| `bboxes` | A list of bounding boxes in pixel coordinates, with each box containing x, y, width, and height values. | BOUNDING_BOX |
| `elements` | A structured array of element objects, each containing type, bounding box coordinates (normalized 0-1000), text (for text type), description, and color palette. | ARRAY |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dc5545dffefdccf14f3919ff4d9966dbfd1a497dcd64e1863556d5728659ee94`

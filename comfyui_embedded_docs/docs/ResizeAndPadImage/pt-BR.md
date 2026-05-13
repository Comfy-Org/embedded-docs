> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/pt-BR.md)

O nó ResizeAndPadImage redimensiona uma imagem para caber dentro de dimensões especificadas, mantendo sua proporção original. Ele escala a imagem proporcionalmente para caber na largura e altura alvo e, em seguida, adiciona preenchimento ao redor das bordas para preencher qualquer espaço restante. A cor do preenchimento e o método de interpolação podem ser personalizados para controlar a aparência das áreas preenchidas e a qualidade do redimensionamento.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser redimensionada e preenchida |
| `target_width` | INT | Sim | 1 a MAX_RESOLUTION | A largura desejada da imagem de saída (padrão: 512) |
| `target_height` | INT | Sim | 1 a MAX_RESOLUTION | A altura desejada da imagem de saída (padrão: 512) |
| `padding_color` | COMBO | Sim | "white"<br>"black" | A cor a ser usada para as áreas de preenchimento ao redor da imagem redimensionada (padrão: "white") |
| `interpolation` | COMBO | Sim | "area"<br>"bicubic"<br>"nearest-exact"<br>"bilinear"<br>"lanczos" | O método de interpolação usado para redimensionar a imagem (padrão: "area") |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | A imagem de saída redimensionada e preenchida |

---
**Source fingerprint (SHA-256):** `01566327d46043d1ff9ce404b4df8f49e853d0b01d07cc189fb843157dac1cac`

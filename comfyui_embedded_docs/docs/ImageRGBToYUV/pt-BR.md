O nó ImageRGBToYUV converte imagens coloridas RGB para o espaço de cores YUV. Ele recebe uma imagem RGB como entrada e a separa em três canais distintos: Y (luminância), U (projeção azul) e V (projeção vermelha). Cada canal de saída é retornado como uma imagem em escala de cinza separada, representando o componente YUV correspondente.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem RGB de entrada a ser convertida para o espaço de cores YUV | IMAGE | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `Y` | O componente de luminância (brilho) do espaço de cores YUV | IMAGE |
| `U` | O componente de projeção azul do espaço de cores YUV | IMAGE |
| `V` | O componente de projeção vermelha do espaço de cores YUV | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/pt-BR.md)

---
**Source fingerprint (SHA-256):** `119cba119b62c7b46ffdd2c0feca932a9af1ec41c338fead23c21fdf76a6abb2`

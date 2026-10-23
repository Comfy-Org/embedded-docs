# VAE Codificar (para Inpainting)

Este nó foi projetado para codificar imagens em uma representação latente adequada para tarefas de inpaint, incorporando etapas adicionais de pré-processamento para ajustar a imagem de entrada e a máscara para codificação ideal pelo modelo VAE.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `pixels` | A imagem de entrada a ser codificada. Esta imagem passa por pré-processamento e redimensionamento para corresponder às dimensões de entrada esperadas pelo modelo VAE antes da codificação. | `IMAGE` |
| `vae` | O modelo VAE usado para codificar a imagem em sua representação latente. Ele desempenha um papel crucial no processo de transformação, determinando a qualidade e as características do espaço latente de saída. | VAE |
| `máscara` | Uma máscara indicando as regiões da imagem de entrada a serem inpaintadas. Ela é usada para modificar a imagem antes da codificação, garantindo que o VAE se concentre nas áreas relevantes. | `MASK` |
| `aumentar_máscara_em` | Especifica o quanto expandir a máscara de inpaint para garantir transições suaves no espaço latente. Um valor maior aumenta a área afetada pelo inpaint. | `INT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | A saída inclui a representação latente codificada da imagem e uma máscara de ruído, ambos cruciais para tarefas subsequentes de inpaint. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeForInpaint/pt-BR.md)

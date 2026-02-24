> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeForInpaint/pt-BR.md)

Este nó foi projetado para codificar imagens em uma representação latente adequada para tarefas de inpainting, incorporando etapas adicionais de pré-processamento para ajustar a imagem de entrada e a máscara para uma codificação ideal pelo modelo VAE.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `pixels`  | `IMAGE`     | A imagem de entrada a ser codificada. Esta imagem passa por pré-processamento e redimensionamento para corresponder às dimensões de entrada esperadas pelo modelo VAE antes da codificação. |
| `vae`     | VAE       | O modelo VAE usado para codificar a imagem em sua representação latente. Ele desempenha um papel crucial no processo de transformação, determinando a qualidade e as características do espaço latente de saída. |
| `mask`    | `MASK`      | Uma máscara que indica as regiões da imagem de entrada a serem submetidas ao inpainting. Ela é usada para modificar a imagem antes da codificação, garantindo que o VAE se concentre nas áreas relevantes. |
| `grow_mask_by` | `INT` | Especifica o quanto expandir a máscara de inpainting para garantir transições perfeitas no espaço latente. Um valor maior aumenta a área afetada pelo inpainting. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | A saída inclui a representação latente codificada da imagem e uma máscara de ruído, ambas cruciais para tarefas subsequentes de inpainting. |

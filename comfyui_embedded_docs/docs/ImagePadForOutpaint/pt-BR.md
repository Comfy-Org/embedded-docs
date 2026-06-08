Este nó foi projetado para preparar imagens para o processo de extrapolação (outpainting), adicionando preenchimento ao redor delas. Ele ajusta as dimensões da imagem para garantir compatibilidade com algoritmos de extrapolação, facilitando a geração de áreas estendidas da imagem além dos limites originais.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagem` | A entrada 'image' é a imagem principal a ser preparada para extrapolação, servindo como base para as operações de preenchimento. | `IMAGE` |
| `esquerda` | Especifica a quantidade de preenchimento a ser adicionada ao lado esquerdo da imagem, influenciando a área expandida para extrapolação. | `INT` |
| `superior` | Determina a quantidade de preenchimento a ser adicionada ao topo da imagem, afetando a expansão vertical para extrapolação. | `INT` |
| `direita` | Define a quantidade de preenchimento a ser adicionada ao lado direito da imagem, impactando a expansão horizontal para extrapolação. | `INT` |
| `inferior` | Indica a quantidade de preenchimento a ser adicionada à parte inferior da imagem, contribuindo para a expansão vertical para extrapolação. | `INT` |
| `suavização` | Controla a suavidade da transição entre a imagem original e o preenchimento adicionado, melhorando a integração visual para extrapolação. | `INT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagem` | A saída 'image' representa a imagem com preenchimento, pronta para o processo de extrapolação. | `IMAGE` |
| `mask` | A saída 'mask' indica as áreas da imagem original e do preenchimento adicionado, sendo útil para orientar os algoritmos de extrapolação. | `MASK` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImagePadForOutpaint/pt-BR.md)

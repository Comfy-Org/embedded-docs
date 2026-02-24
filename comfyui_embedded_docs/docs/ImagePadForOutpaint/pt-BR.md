> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImagePadForOutpaint/pt-BR.md)

Este nó é projetado para preparar imagens para o processo de outpainting adicionando preenchimento (padding) ao redor delas. Ele ajusta as dimensões da imagem para garantir compatibilidade com algoritmos de outpainting, facilitando a geração de áreas estendidas da imagem além dos limites originais.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | A entrada 'image' é a imagem principal a ser preparada para outpainting, servindo como base para as operações de preenchimento. |
| `left`    | `INT`       | Especifica a quantidade de preenchimento a ser adicionada ao lado esquerdo da imagem, influenciando a área expandida para outpainting. |
| `top`     | `INT`       | Determina a quantidade de preenchimento a ser adicionada ao topo da imagem, afetando a expansão vertical para outpainting. |
| `right`   | `INT`       | Define a quantidade de preenchimento a ser adicionada ao lado direito da imagem, impactando a expansão horizontal para outpainting. |
| `bottom`  | `INT`       | Indica a quantidade de preenchimento a ser adicionada à parte inferior da imagem, contribuindo para a expansão vertical para outpainting. |
| `feathering` | `INT` | Controla a suavidade da transição entre a imagem original e o preenchimento adicionado, melhorando a integração visual para outpainting. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | A 'image' de saída representa a imagem com preenchimento, pronta para o processo de outpainting. |
| `mask`    | `MASK`      | A 'mask' de saída indica as áreas da imagem original e do preenchimento adicionado, útil para orientar os algoritmos de outpainting. |

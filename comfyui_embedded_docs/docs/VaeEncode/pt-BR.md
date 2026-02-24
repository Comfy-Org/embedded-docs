> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncode/pt-BR.md)

Este nó é projetado para codificar imagens em uma representação de espaço latente usando um modelo VAE especificado. Ele abstrai a complexidade do processo de codificação, fornecendo uma maneira direta de transformar imagens em suas representações latentes.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `pixels`  | `IMAGE`     | O parâmetro 'pixels' representa os dados da imagem a serem codificados no espaço latente. Ele desempenha um papel crucial na determinação da representação latente de saída, servindo como entrada direta para o processo de codificação. |
| `vae`     | VAE       | O parâmetro 'vae' especifica o modelo de Autoencoder Variacional a ser usado para codificar os dados da imagem no espaço latente. É essencial para definir o mecanismo de codificação e as características da representação latente gerada. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | A saída é uma representação do espaço latente da imagem de entrada, encapsulando suas características essenciais em uma forma comprimida. |

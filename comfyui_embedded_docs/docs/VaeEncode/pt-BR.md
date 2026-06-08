Este nó foi projetado para codificar imagens em uma representação de espaço latente usando um modelo VAE específico. Ele abstrai a complexidade do processo de codificação, oferecendo uma maneira direta de transformar imagens em suas representações latentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `pixels` | O parâmetro 'pixels' representa os dados da imagem a serem codificados no espaço latente. Ele desempenha um papel crucial na determinação da representação latente de saída, servindo como entrada direta para o processo de codificação. | `IMAGE` |
| `vae` | O parâmetro 'vae' especifica o modelo Autoencoder Variacional a ser usado para codificar os dados da imagem no espaço latente. Ele é essencial para definir o mecanismo de codificação e as características da representação latente gerada. | VAE |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | A saída é uma representação no espaço latente da imagem de entrada, encapsulando suas características essenciais em uma forma compactada. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncode/pt-BR.md)

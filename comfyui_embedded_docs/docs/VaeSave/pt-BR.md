> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAESave/pt-BR.md)

O nó VAESave é projetado para salvar modelos VAE juntamente com seus metadados, incluindo prompts e informações PNG adicionais, em um diretório de saída especificado. Ele encapsula a funcionalidade de serializar o estado do modelo e as informações associadas em um arquivo, facilitando a preservação e o compartilhamento de modelos treinados.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `vae`     | VAE       | O modelo VAE a ser salvo. Este parâmetro é crucial, pois representa o modelo cujo estado será serializado e armazenado. |
| `filename_prefix` | STRING   | Um prefixo para o nome do arquivo sob o qual o modelo e seus metadados serão salvos. Isso permite um armazenamento organizado e uma recuperação fácil dos modelos. |

## Saídas

O nó não possui tipos de saída.

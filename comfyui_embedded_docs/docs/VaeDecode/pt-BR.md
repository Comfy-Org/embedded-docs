> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecode/pt-BR.md)

O nó VAEDecode é projetado para decodificar representações latentes em imagens usando um Autoencoder Variacional (VAE) especificado. Ele tem a finalidade de gerar imagens a partir de representações de dados comprimidos, facilitando a reconstrução de imagens a partir de suas codificações no espaço latente.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | O parâmetro 'samples' representa as representações latentes a serem decodificadas em imagens. É crucial para o processo de decodificação, pois fornece os dados comprimidos a partir dos quais as imagens são reconstruídas. |
| `vae`     | VAE       | O parâmetro 'vae' especifica o modelo de Autoencoder Variacional a ser usado para decodificar as representações latentes em imagens. É essencial para determinar o mecanismo de decodificação e a qualidade das imagens reconstruídas. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | A saída é uma imagem reconstruída a partir da representação latente fornecida, usando o modelo VAE especificado. |

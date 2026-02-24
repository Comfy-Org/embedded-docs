> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentRotate/pt-BR.md)

O nó LatentRotate é projetado para rotacionar representações latentes de imagens por ângulos especificados. Ele abstrai a complexidade de manipular o espaço latente para obter efeitos de rotação, permitindo que os usuários transformem facilmente imagens no espaço latente de um modelo generativo.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | O parâmetro 'samples' representa as representações latentes das imagens a serem rotacionadas. É crucial para determinar o ponto de partida da operação de rotação. |
| `rotation` | COMBO[STRING] | O parâmetro 'rotation' especifica o ângulo pelo qual as imagens latentes devem ser rotacionadas. Ele influencia diretamente a orientação das imagens resultantes. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | A saída é uma versão modificada das representações latentes de entrada, rotacionadas pelo ângulo especificado. |

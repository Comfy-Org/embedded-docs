> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentAdd/pt-BR.md)

O nó LatentAdd é projetado para a adição de duas representações latentes. Ele facilita a combinação de características ou atributos codificados nessas representações por meio da realização de uma adição elemento por elemento.

## Entradas

| Parâmetro    | Tipo de Dados | Descrição |
|--------------|-------------|-------------|
| `samples1`   | `LATENT`    | O primeiro conjunto de amostras latentes a ser adicionado. Representa uma das entradas cujas características devem ser combinadas com outro conjunto de amostras latentes. |
| `samples2`   | `LATENT`    | O segundo conjunto de amostras latentes a ser adicionado. Serve como a outra entrada cujas características são combinadas com o primeiro conjunto de amostras latentes por meio da adição elemento por elemento. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | O resultado da adição elemento por elemento das duas amostras latentes, representando um novo conjunto de amostras latentes que combina as características de ambas as entradas. |

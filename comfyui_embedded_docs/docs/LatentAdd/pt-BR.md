O nó **LatentAdd** é projetado para a adição de duas representações latentes. Ele facilita a combinação de características ou atributos codificados nessas representações por meio de uma adição elemento a elemento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `amostras1` | O primeiro conjunto de amostras latentes a ser adicionado. Representa uma das entradas cujas características serão combinadas com outro conjunto de amostras latentes. | `LATENT` |
| `amostras2` | O segundo conjunto de amostras latentes a ser adicionado. Serve como a outra entrada cujas características são combinadas com o primeiro conjunto de amostras latentes por meio de adição elemento a elemento. | `LATENT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `latent` | O resultado da adição elemento a elemento de duas amostras latentes, representando um novo conjunto de amostras latentes que combina as características de ambas as entradas. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentAdd/pt-BR.md)

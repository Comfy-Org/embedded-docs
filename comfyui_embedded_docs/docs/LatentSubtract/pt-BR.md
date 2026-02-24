> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentSubtract/pt-BR.md)

O nó LatentSubtract é projetado para subtrair uma representação latente de outra. Esta operação pode ser usada para manipular ou modificar as características das saídas de modelos generativos, removendo efetivamente características ou atributos representados em um espaço latente de outro.

## Entradas

| Parâmetro    | Tipo de Dados | Descrição |
|--------------|-------------|-------------|
| `samples1`   | `LATENT`    | O primeiro conjunto de amostras latentes do qual será feita a subtração. Serve como base para a operação de subtração. |
| `samples2`   | `LATENT`    | O segundo conjunto de amostras latentes que será subtraído do primeiro conjunto. Esta operação pode alterar a saída resultante do modelo generativo, removendo atributos ou características. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | O resultado da subtração do segundo conjunto de amostras latentes do primeiro. Esta representação latente modificada pode ser usada para tarefas generativas subsequentes. |

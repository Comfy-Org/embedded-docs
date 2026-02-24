> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/pt-BR.md)

O nó TomePatchModel aplica Token Merging (ToMe) a um modelo de difusão para reduzir os requisitos computacionais durante a inferência. Ele funciona mesclando seletivamente *tokens* semelhantes no mecanismo de atenção, permitindo que o modelo processe menos *tokens* enquanto mantém a qualidade da imagem. Esta técnica ajuda a acelerar a geração sem perda significativa de qualidade.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de difusão ao qual aplicar a mesclagem de *tokens* |
| `ratio` | FLOAT | Não | 0.0 - 1.0 | A proporção de *tokens* a serem mesclados (padrão: 0.3) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com a mesclagem de *tokens* aplicada |

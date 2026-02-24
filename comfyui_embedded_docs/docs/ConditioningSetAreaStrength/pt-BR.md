> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaStrength/pt-BR.md)

Este nó foi projetado para modificar o atributo de força de um conjunto de condicionamento fornecido, permitindo o ajuste da influência ou intensidade do condicionamento no processo de geração.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | O conjunto de condicionamento a ser modificado, representando o estado atual do condicionamento que influencia o processo de geração. |
| `strength` | `FLOAT` | O valor de força a ser aplicado ao conjunto de condicionamento, ditando a intensidade de sua influência. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | O conjunto de condicionamento modificado com os valores de força atualizados para cada elemento. |

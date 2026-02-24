> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentage/pt-BR.md)

O nó ConditioningSetAreaPercentage é especializado em ajustar a área de influência de elementos de condicionamento com base em valores percentuais. Ele permite especificar as dimensões e a posição da área como porcentagens do tamanho total da imagem, juntamente com um parâmetro de força para modular a intensidade do efeito de condicionamento.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Representa os elementos de condicionamento a serem modificados, servindo como base para a aplicação dos ajustes de área e força. |
| `width`   | `FLOAT`     | Especifica a largura da área como uma porcentagem da largura total da imagem, influenciando quanto da imagem o condicionamento afeta horizontalmente. |
| `height`  | `FLOAT`     | Determina a altura da área como uma porcentagem da altura total da imagem, afetando a extensão vertical da influência do condicionamento. |
| `x`       | `FLOAT`     | Indica o ponto de partida horizontal da área como uma porcentagem da largura total da imagem, posicionando o efeito de condicionamento. |
| `y`       | `FLOAT`     | Especifica o ponto de partida vertical da área como uma porcentagem da altura total da imagem, posicionando o efeito de condicionamento. |
| `strength`| `FLOAT`     | Controla a intensidade do efeito de condicionamento dentro da área especificada, permitindo um ajuste fino de seu impacto. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Retorna os elementos de condicionamento modificados com os parâmetros de área e força atualizados, prontos para processamento ou aplicação posteriores. |

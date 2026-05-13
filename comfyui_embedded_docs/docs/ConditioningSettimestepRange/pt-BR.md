> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetTimestepRange/pt-BR.md)

Este nó foi projetado para ajustar o aspecto temporal do condicionamento, definindo um intervalo específico de etapas de tempo (*timesteps*). Ele permite o controle preciso sobre os pontos inicial e final do processo de condicionamento, possibilitando uma geração mais direcionada e eficiente.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | A entrada de condicionamento representa o estado atual do processo de geração, que este nó modifica ao definir um intervalo específico de etapas de tempo. |
| `start` | `FLOAT` | O parâmetro *start* especifica o início do intervalo de etapas de tempo como uma porcentagem do processo total de geração, permitindo um controle refinado sobre quando os efeitos do condicionamento começam. |
| `end` | `FLOAT` | O parâmetro *end* define o ponto final do intervalo de etapas de tempo como uma porcentagem, possibilitando um controle preciso sobre a duração e a conclusão dos efeitos do condicionamento. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | A saída é o condicionamento modificado com o intervalo de etapas de tempo especificado aplicado, pronto para processamento ou geração adicional. |
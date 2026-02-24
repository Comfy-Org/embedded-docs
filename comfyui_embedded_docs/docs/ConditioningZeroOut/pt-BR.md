> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningZeroOut/pt-BR.md)

Este nó zera elementos específicos dentro da estrutura de dados de condicionamento, neutralizando efetivamente sua influência nas etapas subsequentes de processamento. Ele foi projetado para operações avançadas de condicionamento onde é necessária a manipulação direta da representação interna do condicionamento.

## Entradas

| Parâmetro | Tipo Comfy                | Descrição |
|-----------|----------------------------|-------------|
| `CONDITIONING` | CONDITIONING | A estrutura de dados de condicionamento a ser modificada. Este nó zera os elementos 'pooled_output' dentro de cada entrada de condicionamento, se presentes. |

## Saídas

| Parâmetro | Tipo Comfy                | Descrição |
|-----------|----------------------------|-------------|
| `CONDITIONING` | CONDITIONING | A estrutura de dados de condicionamento modificada, com os elementos 'pooled_output' definidos como zero, quando aplicável. |

Este nó zera elementos específicos dentro da estrutura de dados de condicionamento, neutralizando efetivamente sua influência nas etapas de processamento subsequentes. Ele foi projetado para operações avançadas de condicionamento onde é necessária a manipulação direta da representação interna do condicionamento.

## Entradas

| Parâmetro | Descrição | Tipo Comfy |
| --- | --- | --- |
| `CONDITIONING` | A estrutura de dados de condicionamento a ser modificada. Este nó zera os elementos 'pooled_output' dentro de cada entrada de condicionamento, se presentes. | CONDITIONING |

## Saídas

| Parâmetro | Descrição | Tipo Comfy |
| --- | --- | --- |
| `CONDITIONING` | A estrutura de dados de condicionamento modificada, com os elementos 'pooled_output' definidos como zero quando aplicável. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningZeroOut/pt-BR.md)

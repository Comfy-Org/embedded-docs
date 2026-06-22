# Condicionamento (Concatenar)

O nó **ConditioningConcat** foi projetado para concatenar vetores de condicionamento, especificamente mesclando o vetor 'conditioning_from' no vetor 'conditioning_to'. Esta operação é fundamental em cenários onde as informações de condicionamento de duas fontes precisam ser combinadas em uma única representação unificada.

## Entradas

| Parâmetro | Descrição | Tipo Comfy |
| --- | --- | --- |
| `condicionamento_para` | Representa o conjunto principal de vetores de condicionamento ao qual os vetores 'conditioning_from' serão concatenados. Serve como base para o processo de concatenação. | `CONDITIONING` |
| `condicionamento_de` | Consiste em vetores de condicionamento que serão concatenados aos vetores 'conditioning_to'. Este parâmetro permite que informações de condicionamento adicionais sejam integradas ao conjunto existente. | `CONDITIONING` |

## Saídas

| Parâmetro | Descrição | Tipo Comfy |
| --- | --- | --- |
| `conditioning` | A saída é um conjunto unificado de vetores de condicionamento, resultante da concatenação dos vetores 'conditioning_from' nos vetores 'conditioning_to'. | `CONDITIONING` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningConcat/pt-BR.md)

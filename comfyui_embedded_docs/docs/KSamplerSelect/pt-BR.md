O nó KSamplerSelect foi projetado para selecionar um sampler específico com base no nome do sampler fornecido. Ele abstrai a complexidade da seleção do sampler, permitindo que os usuários alternem facilmente entre diferentes estratégias de amostragem para suas tarefas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `nome_do_sampler` | Especifica o nome do sampler a ser selecionado. Este parâmetro determina qual estratégia de amostragem será utilizada, impactando o comportamento geral da amostragem e os resultados. | COMBO[STRING] |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sampler` | Retorna o objeto sampler selecionado, pronto para ser usado em tarefas de amostragem. | `SAMPLER` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerSelect/pt-BR.md)

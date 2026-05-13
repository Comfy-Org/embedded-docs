> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerSelect/pt-BR.md)

O nó KSamplerSelect foi projetado para selecionar um sampler específico com base no nome do sampler fornecido. Ele abstrai a complexidade da seleção do sampler, permitindo que os usuários alternem facilmente entre diferentes estratégias de amostragem para suas tarefas.

## Entradas

| Parâmetro         | Tipo de Dado | Descrição                                                                                      |
|-------------------|--------------|------------------------------------------------------------------------------------------------|
| `sampler_name`    | COMBO[STRING] | Especifica o nome do sampler a ser selecionado. Este parâmetro determina qual estratégia de amostragem será utilizada, impactando o comportamento geral da amostragem e os resultados. |

## Saídas

| Parâmetro   | Tipo de Dado | Descrição                                                                 |
|-------------|--------------|---------------------------------------------------------------------------|
| `sampler`   | `SAMPLER`    | Retorna o objeto sampler selecionado, pronto para ser usado em tarefas de amostragem. |
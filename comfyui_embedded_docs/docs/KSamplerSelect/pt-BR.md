> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerSelect/pt-BR.md)

O nó KSamplerSelect é projetado para selecionar um amostrador específico com base no nome fornecido. Ele abstrai a complexidade da seleção de amostradores, permitindo que os usuários alternem facilmente entre diferentes estratégias de amostragem para suas tarefas.

## Entradas

| Parâmetro         | Tipo de Dados | Descrição                                                                                      |
|-------------------|-------------|------------------------------------------------------------------------------------------------|
| `sampler_name`    | COMBO[STRING] | Especifica o nome do amostrador a ser selecionado. Este parâmetro determina qual estratégia de amostragem será usada, impactando o comportamento geral da amostragem e os resultados. |

## Saídas

| Parâmetro   | Tipo de Dados | Descrição                                                                 |
|-------------|-------------|-----------------------------------------------------------------------------|
| `sampler`   | `SAMPLER`   | Retorna o objeto do amostrador selecionado, pronto para ser usado em tarefas de amostragem. |

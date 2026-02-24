> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/pt-BR.md)

O nó OptimalStepsScheduler calcula os sigmas do cronograma de ruído para modelos de difusão com base no tipo de modelo e na configuração de etapas selecionados. Ele ajusta o número total de etapas de acordo com o parâmetro `denoise` e interpola os níveis de ruído para corresponder à contagem de etapas solicitada. O nó retorna uma sequência de valores sigma que determinam os níveis de ruído usados durante o processo de amostragem de difusão.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model_type` | COMBO | Sim | "FLUX"<br>"Wan"<br>"Chroma" | O tipo de modelo de difusão a ser usado para o cálculo dos níveis de ruído |
| `steps` | INT | Sim | 3-1000 | O número total de etapas de amostragem a serem calculadas (padrão: 20) |
| `denoise` | FLOAT | Não | 0.0-1.0 | Controla a intensidade da remoção de ruído, que ajusta o número efetivo de etapas (padrão: 1.0) |

**Observação:** Quando `denoise` é definido como menor que 1.0, o nó calcula as etapas efetivas como `steps * denoise`. Se `denoise` for definido como 0.0, o nó retorna um tensor vazio.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Uma sequência de valores sigma que representa o cronograma de ruído para a amostragem de difusão |

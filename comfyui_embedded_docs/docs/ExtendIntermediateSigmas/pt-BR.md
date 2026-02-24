> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/pt-BR.md)

O nó ExtendIntermediateSigmas recebe uma sequência existente de valores sigma e insere valores sigma intermediários adicionais entre eles. Ele permite que você especifique quantas etapas extras adicionar, o método de espaçamento para interpolação e limites opcionais de sigma inicial e final para controlar onde a extensão ocorre na sequência de sigma.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | SIGMAS | Sim | - | A sequência de sigma de entrada a ser estendida com valores intermediários |
| `steps` | INT | Sim | 1-100 | Número de etapas intermediárias a inserir entre os sigmas existentes (padrão: 2) |
| `start_at_sigma` | FLOAT | Sim | -1.0 a 20000.0 | Limite superior de sigma para extensão - estende apenas sigmas abaixo deste valor (padrão: -1.0, que significa infinito) |
| `end_at_sigma` | FLOAT | Sim | 0.0 a 20000.0 | Limite inferior de sigma para extensão - estende apenas sigmas acima deste valor (padrão: 12.0) |
| `spacing` | COMBO | Sim | "linear"<br>"cosine"<br>"sine" | O método de interpolação para espaçar os valores sigma intermediários |

**Observação:** O nó insere sigmas intermediários apenas entre pares de sigma existentes onde tanto o sigma atual é menor ou igual a `start_at_sigma` quanto maior ou igual a `end_at_sigma`. Quando `start_at_sigma` é definido como -1.0, ele é tratado como infinito, significando que apenas o limite inferior `end_at_sigma` se aplica.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | A sequência de sigma estendida com valores intermediários adicionais inseridos |

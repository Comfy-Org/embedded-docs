> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/pt-BR.md)

O nó GITSScheduler gera um cronograma de sigmas de ruído para o método de amostragem GITS (Generative Iterative Time Steps). Ele calcula os valores de sigma com base em um parâmetro de coeficiente e no número de etapas, com um fator de remoção de ruído opcional que pode reduzir o total de etapas utilizadas. O nó utiliza níveis de ruído predefinidos e interpolação para criar o cronograma de sigmas final.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `coeff` | FLOAT | Sim | 0.80 - 1.50 | O valor do coeficiente que controla a curva do cronograma de ruído (padrão: 1.20) |
| `steps` | INT | Sim | 2 - 1000 | O número total de etapas de amostragem para as quais gerar os sigmas (padrão: 10) |
| `denoise` | FLOAT | Sim | 0.0 - 1.0 | Fator de remoção de ruído que reduz o número de etapas utilizadas (padrão: 1.0) |

**Observação:** Quando `denoise` é definido como 0.0, o nó retorna um tensor vazio. Quando `denoise` é menor que 1.0, o número real de etapas utilizadas é calculado como `round(steps * denoise)`.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Os valores de sigma gerados para o cronograma de ruído |

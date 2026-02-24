> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/pt-BR.md)

O nó AlignYourStepsScheduler gera valores sigma para o processo de remoção de ruído com base em diferentes tipos de modelo. Ele calcula níveis de ruído apropriados para cada etapa do processo de amostragem e ajusta o número total de etapas de acordo com o parâmetro `denoise`. Isso ajuda a alinhar as etapas de amostragem com os requisitos específicos de diferentes modelos de difusão.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Range | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model_type` | STRING | COMBO | - | SD1, SDXL, SVD | Especifica o tipo de modelo a ser usado para o cálculo do sigma |
| `steps` | INT | INT | 10 | 1-10000 | O número total de etapas de amostragem a serem geradas |
| `denoise` | FLOAT | FLOAT | 1.0 | 0.0-1.0 | Controla o quanto a imagem será processada para remoção de ruído, onde 1.0 usa todas as etapas e valores mais baixos usam menos etapas |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Retorna os valores sigma calculados para o processo de remoção de ruído |

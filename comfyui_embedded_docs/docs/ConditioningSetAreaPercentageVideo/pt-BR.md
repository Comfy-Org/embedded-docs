> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/pt-BR.md)

O nó ConditioningSetAreaPercentageVideo modifica dados de condicionamento definindo uma área específica e uma região temporal para geração de vídeo. Ele permite configurar a posição, o tamanho e a duração da área onde o condicionamento será aplicado usando valores percentuais em relação às dimensões totais. Isso é útil para focar a geração em partes específicas de uma sequência de vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `conditioning` | CONDITIONING | Obrigatório | - | - | Os dados de condicionamento a serem modificados |
| `width` | FLOAT | Obrigatório | 1.0 | 0.0 - 1.0 | A largura da área como uma porcentagem da largura total |
| `height` | FLOAT | Obrigatório | 1.0 | 0.0 - 1.0 | A altura da área como uma porcentagem da altura total |
| `temporal` | FLOAT | Obrigatório | 1.0 | 0.0 - 1.0 | A duração temporal da área como uma porcentagem do comprimento total do vídeo |
| `x` | FLOAT | Obrigatório | 0.0 | 0.0 - 1.0 | A posição horizontal inicial da área como uma porcentagem |
| `y` | FLOAT | Obrigatório | 0.0 | 0.0 - 1.0 | A posição vertical inicial da área como uma porcentagem |
| `z` | FLOAT | Obrigatório | 0.0 | 0.0 - 1.0 | A posição inicial temporal da área como uma porcentagem da linha do tempo do vídeo |
| `strength` | FLOAT | Obrigatório | 1.0 | 0.0 - 10.0 | O multiplicador de intensidade aplicado ao condicionamento dentro da área definida |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Os dados de condicionamento modificados com as configurações de área e intensidade especificadas aplicadas |

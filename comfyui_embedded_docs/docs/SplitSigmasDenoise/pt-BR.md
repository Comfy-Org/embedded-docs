> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/pt-BR.md)

O nó SplitSigmasDenoise divide uma sequência de valores sigma em duas partes com base em um parâmetro de intensidade de remoção de ruído. Ele separa os sigmas de entrada em sequências de sigma alta e baixa, onde o ponto de divisão é determinado multiplicando o total de etapas pelo fator de denoise. Isso permite separar o cronograma de ruído em diferentes faixas de intensidade para processamento especializado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | SIGMAS | Sim | - | A sequência de entrada de valores sigma que representa o cronograma de ruído |
| `denoise` | FLOAT | Sim | 0.0 - 1.0 | O fator de intensidade de remoção de ruído que determina onde dividir a sequência de sigma (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `high_sigmas` | SIGMAS | A primeira parte da sequência de sigma, contendo os valores de sigma mais altos |
| `low_sigmas` | SIGMAS | A segunda parte da sequência de sigma, contendo os valores de sigma mais baixos |

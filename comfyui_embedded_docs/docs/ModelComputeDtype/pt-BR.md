> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/pt-BR.md)

O nó ModelComputeDtype permite que você altere o tipo de dados computacional usado por um modelo durante a inferência. Ele cria uma cópia do modelo de entrada e aplica a configuração de tipo de dados especificada, o que pode ajudar a otimizar o uso de memória e o desempenho, dependendo das capacidades do seu hardware. Isso é particularmente útil para depuração e teste de diferentes configurações de precisão.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de entrada a ser modificado com um novo tipo de dados computacional |
| `dtype` | STRING | Sim | "default"<br>"fp32"<br>"fp16"<br>"bf16" | O tipo de dados computacional a ser aplicado ao modelo |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com o novo tipo de dados computacional aplicado |

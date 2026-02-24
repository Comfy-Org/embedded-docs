> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/pt-BR.md)

O nó ConditioningStableAudio adiciona informações de temporização tanto aos condicionamentos positivos quanto negativos para a geração de áudio. Ele define os parâmetros de tempo de início e duração total que ajudam a controlar quando e por quanto tempo o conteúdo de áudio deve ser gerado. Este nó modifica os dados de condicionamento existentes anexando metadados de temporização específicos para áudio.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | O condicionamento positivo a ser modificado com informações de temporização de áudio |
| `negative` | CONDITIONING | Sim | - | O condicionamento negativo a ser modificado com informações de temporização de áudio |
| `seconds_start` | FLOAT | Sim | 0.0 a 1000.0 | O tempo de início, em segundos, para a geração de áudio (padrão: 0.0) |
| `seconds_total` | FLOAT | Sim | 0.0 a 1000.0 | A duração total, em segundos, para a geração de áudio (padrão: 47.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | O condicionamento positivo modificado com as informações de temporização de áudio aplicadas |
| `negative` | CONDITIONING | O condicionamento negativo modificado com as informações de temporização de áudio aplicadas |

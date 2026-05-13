> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/pt-BR.md)

O nó ConditioningStableAudio adiciona informações de temporização às entradas de condicionamento positivo e negativo para geração de áudio. Ele define os parâmetros de tempo de início e duração total que ajudam a controlar quando e por quanto tempo o conteúdo de áudio deve ser gerado. Este nó modifica os dados de condicionamento existentes, anexando metadados de temporização específicos para áudio.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `positive` | CONDITIONING | Sim | - | A entrada de condicionamento positivo a ser modificada com informações de temporização de áudio |
| `negative` | CONDITIONING | Sim | - | A entrada de condicionamento negativo a ser modificada com informações de temporização de áudio |
| `seconds_start` | FLOAT | Sim | 0.0 a 1000.0 | O tempo de início em segundos para geração de áudio (padrão: 0.0) |
| `seconds_total` | FLOAT | Sim | 0.0 a 1000.0 | A duração total em segundos para geração de áudio (padrão: 47.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positive` | CONDITIONING | O condicionamento positivo modificado com informações de temporização de áudio aplicadas |
| `negative` | CONDITIONING | O condicionamento negativo modificado com informações de temporização de áudio aplicadas |

---
**Source fingerprint (SHA-256):** `ad4fdb2ac536e4f9cc23c044a7a63333e3f3530cc782937eaedc1565cc7c5d0e`

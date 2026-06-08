O nó ConditioningStableAudio adiciona informações de temporização às entradas de condicionamento positivo e negativo para geração de áudio. Ele define os parâmetros de tempo de início e duração total que ajudam a controlar quando e por quanto tempo o conteúdo de áudio deve ser gerado. Este nó modifica os dados de condicionamento existentes, anexando metadados de temporização específicos para áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | A entrada de condicionamento positivo a ser modificada com informações de temporização de áudio | CONDITIONING | Sim | - |
| `negativo` | A entrada de condicionamento negativo a ser modificada com informações de temporização de áudio | CONDITIONING | Sim | - |
| `segundos_início` | O tempo de início em segundos para geração de áudio (padrão: 0.0) | FLOAT | Sim | 0.0 a 1000.0 |
| `segundos_total` | A duração total em segundos para geração de áudio (padrão: 47.0) | FLOAT | Sim | 0.0 a 1000.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | O condicionamento positivo modificado com informações de temporização de áudio aplicadas | CONDITIONING |
| `negativo` | O condicionamento negativo modificado com informações de temporização de áudio aplicadas | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ad4fdb2ac536e4f9cc23c044a7a63333e3f3530cc782937eaedc1565cc7c5d0e`

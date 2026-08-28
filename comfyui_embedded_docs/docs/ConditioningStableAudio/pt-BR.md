# CondicionamentoStable Audio

O nó ConditioningStableAudio adiciona informações de temporização às entradas de condicionamento positivo e negativo para a geração de áudio. Ele define os parâmetros de tempo de início e duração total, que ajudam a controlar quando e por quanto tempo o conteúdo de áudio deve ser gerado. Este nó modifica os dados de condicionamento existentes anexando metadados de temporização específicos de áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | A entrada de condicionamento positivo a ser modificada com informações de temporização de áudio | CONDITIONING | Sim | - |
| `negativo` | A entrada de condicionamento negativo a ser modificada com informações de temporização de áudio | CONDITIONING | Sim | - |
| `segundos_início` | O tempo de início em segundos para a geração de áudio (padrão: 0.0) | FLOAT | Sim | 0.0 a 1000.0 |
| `segundos_total` | A duração total em segundos para a geração de áudio (padrão: 47.0) | FLOAT | Sim | 0.0 a 1000.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | O condicionamento positivo modificado com informações de temporização de áudio aplicadas | CONDITIONING |
| `negativo` | O condicionamento negativo modificado com informações de temporização de áudio aplicadas | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8bdf29514002837090c549b9921e8cb19c07d385881fe09a58885fcbfe968261`

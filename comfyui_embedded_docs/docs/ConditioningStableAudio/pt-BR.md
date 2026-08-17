# CondicionamentoStable Audio

O nó ConditioningStableAudio adiciona informações de tempo às entradas de condicionamento positivo e negativo para geração de áudio. Ele define os parâmetros de tempo inicial e duração total que ajudam a controlar quando e por quanto tempo o conteúdo de áudio deve ser gerado. Este nó modifica os dados de condicionamento existentes acrescentando metadados de tempo específicos de áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | A entrada de condicionamento positivo a ser modificada com informações de tempo de áudio | CONDITIONING | Sim | - |
| `negative` | A entrada de condicionamento negativo a ser modificada com informações de tempo de áudio | CONDITIONING | Sim | - |
| `seconds_start` | O tempo inicial em segundos para a geração de áudio (padrão: 0.0) | FLOAT | Sim | 0.0 a 1000.0 |
| `seconds_total` | A duração total em segundos para a geração de áudio (padrão: 47.0) | FLOAT | Sim | 0.0 a 1000.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | O condicionamento positivo modificado com informações de tempo de áudio aplicadas | CONDITIONING |
| `negative` | O condicionamento negativo modificado com informações de tempo de áudio aplicadas | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8bdf29514002837090c549b9921e8cb19c07d385881fe09a58885fcbfe968261`

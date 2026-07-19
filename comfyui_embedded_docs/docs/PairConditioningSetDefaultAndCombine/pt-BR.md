# PairConditioningSetDefaultAndCombine

O nó **PairConditioningSetDefaultAndCombine** define valores de condicionamento padrão e os combina com dados de condicionamento de entrada. Ele recebe entradas de condicionamento positivo e negativo junto com suas contrapartes padrão, processando-as através do sistema de hooks do ComfyUI para produzir saídas de condicionamento finais que incorporam os valores padrão.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | A entrada primária de condicionamento positivo a ser processada | CONDITIONING | Sim | - |
| `negative` | A entrada primária de condicionamento negativo a ser processada | CONDITIONING | Sim | - |
| `positive_DEFAULT` | Os valores padrão de condicionamento positivo a serem usados como fallback | CONDITIONING | Sim | - |
| `negative_DEFAULT` | Os valores padrão de condicionamento negativo a serem usados como fallback | CONDITIONING | Sim | - |
| `hooks` | Grupo opcional de hooks para lógica de processamento personalizada | HOOKS | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | O condicionamento positivo processado com valores padrão incorporados | CONDITIONING |
| `negative` | O condicionamento negativo processado com valores padrão incorporados | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dfa47d0fe02e81db8b68d20ae9b765c2518773f4f7fc8caf774cb870267dbb21`

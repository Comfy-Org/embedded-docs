# WAN Context Windows (Manual)

O nó Wan Context Windows (Manual) permite configurar manualmente janelas de contexto para modelos semelhantes ao Wan com processamento bidimensional. Ele aplica as configurações de janela de contexto durante a amostragem, especificando o comprimento da janela, a sobreposição, o método de agendamento e a técnica de fusão, dando a você controle sobre como o modelo processa diferentes regiões de contexto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo ao qual as janelas de contexto serão aplicadas durante a amostragem. | MODEL | Sim | - |
| `context_length` | O comprimento da janela de contexto em quadros reais. Deve ser 4*n + 1. (padrão: 81) | INT | Sim | 1 a 16384 (passo 4) |
| `context_overlap` | A sobreposição da janela de contexto em quadros reais. (padrão: 30) | INT | Sim | 0 ou maior |
| `context_schedule` | Algoritmo de agendamento dependente da etapa para janelas de contexto. (padrão: "uniform_standard") | COMBO | Sim | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `context_stride` | O passo da janela de contexto; aplicável apenas a agendamentos uniformes. (padrão: 1) | INT | Sim | 1 ou maior |
| `closed_loop` | Se deve fechar o loop da janela de contexto; aplicável apenas a agendamentos em loop. (padrão: False) | BOOLEAN | Sim | True or False |
| `fuse_method` | O método a ser usado para fundir as janelas de contexto. (padrão: "pyramid") | COMBO | Sim | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | Se deve aplicar o embaralhamento de ruído FreeNoise, o que melhora a mistura entre janelas. (padrão: True) | BOOLEAN | Sim | True or False |
| `retain_first_frame` | Mantém o primeiro quadro I2V em cada janela de contexto (pode ajudar a preservar a referência inicial). (padrão: False) | BOOLEAN | Sim | True or False |
| `split_conds_to_windows` | Se deve dividir múltiplos condicionamentos (criados por ConditionCombine) em cada janela com base no índice de região. (padrão: False) | BOOLEAN | Sim | True or False |

**Observação:** `context_stride` afeta apenas agendamentos uniformes, e `closed_loop` aplica-se apenas a agendamentos em loop. `context_length` deve seguir o padrão 4n + 1. O nó converte `context_length` e `context_overlap` de quadros reais para unidades de modelo antes de aplicá-los, garantindo um mínimo de 1 para `context_length` e 0 para `context_overlap`. As entradas `context_stride`, `closed_loop`, `freenoise` e `split_conds_to_windows` são opções avançadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo com a configuração de janela de contexto aplicada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`

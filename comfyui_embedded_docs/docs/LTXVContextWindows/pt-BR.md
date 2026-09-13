# Janelas de Contexto LTXV

Este nó define janelas de contexto para modelos semelhantes ao LTXV durante a amostragem. Ele divide a geração em janelas sobrepostas para ajudar a gerenciar o uso de memória e melhorar a coerência temporal.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo ao qual aplicar janelas de contexto durante a amostragem. | MODEL | Sim | - |
| `context_length` | O comprimento da janela de contexto em quadros reais. Deve ser 8*n + 1. (padrão: 145) | INT | Sim | Mínimo: 1<br>Máximo: nodes.MAX_RESOLUTION<br>Passo: 8 |
| `context_overlap` | A sobreposição da janela de contexto em quadros reais. (padrão: 40) | INT | Sim | Mínimo: 0<br>Passo: 8 |
| `context_schedule` | Algoritmo de agendamento dependente do passo para janelas de contexto. (padrão: "UNIFORM_STANDARD") | COMBO | Sim | `"STATIC_STANDARD"`<br>`"UNIFORM_STANDARD"`<br>`"UNIFORM_LOOPED"`<br>`"BATCHED"` |
| `context_stride` | O passo da janela de contexto; aplicável apenas a agendamentos uniformes. (padrão: 1) | INT | Sim | Mínimo: 1 |
| `closed_loop` | Se deve fechar o loop da janela de contexto; aplicável apenas a agendamentos em loop. (padrão: False) | BOOLEAN | Sim | True<br>False |
| `fuse_method` | O método a ser usado para fundir as janelas de contexto. As opções disponíveis são definidas por `ContextFuseMethods.LIST_STATIC`. (padrão: "PYRAMID") | COMBO | Sim | Definido por `ContextFuseMethods.LIST_STATIC` |
| `freenoise` | Se deve aplicar o embaralhamento de ruído FreeNoise, melhora a mesclagem de janelas. (padrão: True) | BOOLEAN | Sim | True<br>False |
| `retain_first_frame` | Reter o primeiro quadro latente em cada janela de contexto (pode ajudar a reter a referência inicial). (padrão: False) | BOOLEAN | Sim | True<br>False |
| `split_conds_to_windows` | Se deve dividir múltiplos condicionamentos (criados por ConditionCombine) para cada janela com base no índice de região. (padrão: False) | BOOLEAN | Sim | True<br>False |

**Nota:** O valor de `context_length` é fornecido em quadros reais e é convertido internamente para quadros latentes usando a fórmula `((context_length - 1) // 8) + 1`, com um mínimo de 1. O valor de `context_overlap` também é fornecido em quadros reais e é convertido para quadros latentes usando divisão inteira por 8, com um mínimo de 0. A dica de ferramenta para `context_length` indica que ele deve seguir o padrão 8*n + 1.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `MODEL` | O modelo com janelas de contexto aplicadas para amostragem. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/pt-BR.md)

---
**Source fingerprint (SHA-256):** `148649d0a938e08c932a163f5d7614332626fba37b8f79db7f92bbcf422e692f`

# Janelas de Contexto (Manual)

Aqui está a tradução da documentação para português brasileiro, seguindo todas as regras estabelecidas:

O nó Context Windows (Manual) permite configurar manualmente janelas de contexto para modelos durante a amostragem. Ele cria segmentos de contexto sobrepostos com comprimento, sobreposição e padrões de agendamento especificados para processar dados em partes gerenciáveis, mantendo a continuidade entre os segmentos. Este nó fornece opções avançadas para controlar como as janelas de contexto são aplicadas, incluindo embaralhamento de ruído, retenção de condicionamento e correção de janela causal.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual aplicar as janelas de contexto durante a amostragem. | MODEL | Sim | - |
| `comprimento_contexto` | O comprimento da janela de contexto (padrão: 16). | INT | Não | 1+ |
| `sobreposição_contexto` | A sobreposição da janela de contexto (padrão: 4). | INT | Não | 0+ |
| `agendamento_contexto` | O passo da janela de contexto. | COMBO | Não | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `passo_contexto` | O passo da janela de contexto; aplicável apenas a agendamentos uniformes (padrão: 1). | INT | Não | 1+ |
| `ciclo_fechado` | Se deve fechar o loop da janela de contexto; aplicável apenas a agendamentos em loop (padrão: False). | BOOLEAN | Não | - |
| `método_fusão` | O método a ser usado para fundir as janelas de contexto (padrão: PYRAMID). | COMBO | Não | `PYRAMID`<br>`LIST_STATIC` |
| `dimensão` | A dimensão à qual aplicar as janelas de contexto (padrão: 0). | INT | Não | 0-5 |
| `freenoise` | Se deve aplicar o embaralhamento de ruído FreeNoise, melhora a mesclagem das janelas (padrão: False). | BOOLEAN | Não | - |
| `cond_retain_index_list` | Lista de índices latentes a serem retidos nos tensores de condicionamento para cada janela; por exemplo, definir como '0' usará a imagem inicial para cada janela (padrão: ""). | STRING | Não | - |
| `split_conds_to_windows` | Se deve dividir múltiplos condicionamentos (criados pelo ConditionCombine) em cada janela com base no índice da região (padrão: False). | BOOLEAN | Não | - |
| `causal_window_fix` | Se deve adicionar um quadro de correção causal a janelas de contexto com índice diferente de 0 (padrão: True). | BOOLEAN | Não | - |

**Restrições dos Parâmetros:**

- `context_stride` é usado apenas quando agendamentos uniformes são selecionados
- `closed_loop` é aplicável apenas a agendamentos em loop
- `dim` deve estar entre 0 e 5 inclusive
- `cond_retain_index_list` espera uma lista de índices inteiros separados por vírgula como uma string (ex.: "0,1,2")

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo com janelas de contexto aplicadas durante a amostragem. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b05ddda0ba38588305e6f733cd218c8b462268c39d16226ca961d09054187261`

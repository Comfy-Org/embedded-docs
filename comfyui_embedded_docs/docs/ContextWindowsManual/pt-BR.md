# Janelas de Contexto (Manual)

O nó Context Windows (Manual) permite configurar manualmente janelas de contexto para modelos durante a amostragem. Ele cria segmentos de contexto sobrepostos com comprimento, sobreposição e padrões de agendamento especificados para processar dados em partes gerenciáveis, mantendo a continuidade entre os segmentos. Este nó oferece opções avançadas para controlar como as janelas de contexto são aplicadas, incluindo embaralhamento de ruído, retenção de condicionamento, retenção de ruído latente e correção de janela causal.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo ao qual aplicar janelas de contexto durante a amostragem. | MODEL | Sim | - |
| `context_length` | O comprimento da janela de contexto (padrão: 16). | INT | Não | 1+ |
| `context_overlap` | A sobreposição da janela de contexto (padrão: 4). | INT | Não | 0+ |
| `context_schedule` | Algoritmo de agendamento dependente da etapa para janelas de contexto (padrão: STATIC_STANDARD). | COMBO | Não | `"STATIC_STANDARD"`<br>`"UNIFORM_STANDARD"`<br>`"UNIFORM_LOOPED"`<br>`"BATCHED"` |
| `context_stride` | O avanço (stride) da janela de contexto; aplicável apenas a agendamentos uniformes (padrão: 1). | INT | Não | 1+ |
| `closed_loop` | Se deve fechar o loop da janela de contexto; aplicável apenas a agendamentos em loop (padrão: False). | BOOLEAN | Não | - |
| `fuse_method` | O método a ser usado para fundir as janelas de contexto (padrão: PYRAMID). | COMBO | Não | `"PYRAMID"`<br>`"LIST_STATIC"` |
| `dim` | A dimensão à qual aplicar as janelas de contexto (padrão: 0). | INT | Não | 0-5 |
| `freenoise` | Se deve aplicar o embaralhamento de ruído FreeNoise, melhora a mistura das janelas (padrão: False). | BOOLEAN | Não | - |
| `cond_retain_index_list` | Lista de índices latentes a serem retidos nos tensores de condicionamento para cada janela. Para modelos I2V do tipo concat (ex.: Wan I2V, HunyuanVideo I2V, Cosmos I2V, SVD), a imagem inicial codificada reside nos canais de condicionamento c_concat; definir isso como '0' reterá o conteúdo da imagem inicial na sub-posição 0 de cada janela (padrão: ""). | STRING | Não | - |
| `split_conds_to_windows` | Se deve dividir múltiplos condicionamentos (criados por ConditionCombine) para cada janela com base no índice da região (padrão: False). | BOOLEAN | Não | - |
| `latent_retain_index_list` | Lista de índices latentes a serem retidos no próprio ruído latente para cada janela. Use para fluxos de trabalho onde o conteúdo de referência (ex.: uma imagem inicial) reside diretamente no ruído latente, em vez de canais de condicionamento separados (ex.: I2V do tipo inplace, como LTXV, AnimateDiff). Independente de cond_retain_index_list (padrão: ""). | STRING | Não | - |
| `causal_window_fix` | Se deve adicionar um quadro de correção causal a janelas de contexto com índice diferente de 0 (padrão: True). | BOOLEAN | Não | - |

**Restrições dos Parâmetros:**

- `context_stride` é usado apenas quando agendamentos uniformes são selecionados.
- `closed_loop` é aplicável apenas a agendamentos em loop.
- `dim` deve estar entre 0 e 5 inclusive.
- `cond_retain_index_list` espera uma lista de índices inteiros separados por vírgula como string (ex.: "0,1,2").
- `latent_retain_index_list` espera uma lista de índices inteiros separados por vírgula como string (ex.: "0,1,2") e é independente de `cond_retain_index_list`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo com janelas de contexto aplicadas durante a amostragem. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/pt-BR.md)

---
**Source fingerprint (SHA-256):** `39dc39ece3d3c10c13ca8c4b85af4fbbebbcaba8a019145a6d4727c3df7b302b`

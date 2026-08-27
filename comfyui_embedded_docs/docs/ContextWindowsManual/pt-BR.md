# Janelas de Contexto (Manual)

O nó Context Windows (Manual) permite configurar manualmente janelas de contexto para um modelo durante a amostragem, criando segmentos de contexto sobrepostos com comprimento, sobreposição e padrão de agendamento especificados, para que os dados sejam processados em blocos gerenciáveis, mantendo a continuidade entre os segmentos. Ele oferece opções avançadas para controlar como as janelas de contexto são aplicadas, incluindo embaralhamento de ruído, retenção de condicionamento e correções de janela causal. Este nó é experimental.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual aplicar as janelas de contexto durante a amostragem. | MODEL | Sim | - |
| `comprimento_contexto` | O comprimento da janela de contexto (padrão: 16). | INT | Sim | 1+ |
| `sobreposição_contexto` | A sobreposição da janela de contexto (padrão: 4). | INT | Sim | 0+ |
| `agendamento_contexto` | Algoritmo de agendamento dependente do passo para janelas de contexto (padrão: STATIC_STANDARD). | COMBO | Sim | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `passo_contexto` | O stride da janela de contexto; aplicável somente a agendamentos uniformes (padrão: 1). | INT | Sim | 1+ |
| `ciclo_fechado` | Indica se o loop da janela de contexto deve ser fechado; aplicável somente a agendamentos em loop (padrão: False). | BOOLEAN | Sim | - |
| `método_fusão` | O método usado para fundir as janelas de contexto (padrão: PYRAMID). | COMBO | Sim | Métodos de fusão estáticos (consulte `ContextFuseMethods.LIST_STATIC`) |
| `dimensão` | A dimensão à qual as janelas de contexto serão aplicadas (padrão: 0). | INT | Sim | 0-5 |
| `freenoise` | Indica se o embaralhamento de ruído FreeNoise deve ser aplicado; melhora a mistura entre janelas (padrão: False). | BOOLEAN | Sim | - |
| `cond_retain_index_list` | Lista de índices latentes a serem retidos nos tensores de condicionamento para cada janela. Para modelos I2V do tipo concat (por exemplo, Wan I2V, HunyuanVideo I2V, Cosmos I2V, SVD), a imagem inicial codificada está presente nos canais de condicionamento `c_concat`; definir isto como '0' reterá o conteúdo dessa imagem inicial na sub-posição 0 de cada janela (padrão: ""). | STRING | Não | - |
| `split_conds_to_windows` | Indica se múltiplos condicionamentos (criados por ConditionCombine) devem ser divididos para cada janela com base no índice de região (padrão: False). | BOOLEAN | Não | - |
| `latent_retain_index_list` | Lista de índices latentes a serem retidos no próprio ruído latente para cada janela. Use para fluxos de trabalho em que o conteúdo de referência (por exemplo, uma imagem inicial) está diretamente no ruído latente, em vez de canais de condicionamento separados (por exemplo, I2V do tipo inplace, como LTXV, AnimateDiff). Independente de `cond_retain_index_list` (padrão: ""). | STRING | Não | - |
| `causal_window_fix` | Indica se um quadro de correção causal deve ser adicionado a janelas de contexto não indexadas em 0 (padrão: True). | BOOLEAN | Não | - |

**Restrições de parâmetro:**

- `context_stride` só é usado quando um agendamento uniforme é selecionado (`UNIFORM_STANDARD` ou `UNIFORM_LOOPED`).
- `closed_loop` é aplicável apenas a agendamentos em loop (`UNIFORM_LOOPED`).
- `dim` deve estar entre 0 e 5, inclusive.
- `cond_retain_index_list` e `latent_retain_index_list` esperam uma lista de índices inteiros separados por vírgula, como uma string (por exemplo, "0,1,2").
- `latent_retain_index_list` é independente de `cond_retain_index_list`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo com janelas de contexto aplicadas durante a amostragem. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/pt-BR.md)

---
**Source fingerprint (SHA-256):** `39dc39ece3d3c10c13ca8c4b85af4fbbebbcaba8a019145a6d4727c3df7b302b`

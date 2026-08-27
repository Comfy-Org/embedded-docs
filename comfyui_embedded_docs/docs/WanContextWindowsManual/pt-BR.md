# WAN Context Windows (Manual)

The WAN Context Windows (Manual) node permite configurar manualmente janelas de contexto para modelos de vídeo do estilo Wan. Ele aplica essas configurações durante a amostragem, dando controle sobre o comprimento da janela, a sobreposição, o agendamento e o método de fusão usados enquanto o modelo processa o vídeo. O comprimento e a sobreposição do contexto são especificados em quadros reais e convertidos internamente para o processamento 2D do modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual aplicar janelas de contexto durante a amostragem. | MODEL | Sim | - |
| `comprimento_do_contexto` | O comprimento da janela de contexto em quadros reais. Deve ser 4*n + 1 (padrão: 81). | INT | Sim | 1 a 16384 (MAX_RESOLUTION), step 4 |
| `sobreposição_do_contexto` | A sobreposição da janela de contexto em quadros reais (padrão: 30). | INT | Sim | 0 or higher |
| `agendamento_do_contexto` | Algoritmo de agendamento dependente da etapa para janelas de contexto (padrão: "uniform_standard"). | COMBO | Sim | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `passo_do_contexto` | O stride (passo) da janela de contexto; aplica-se apenas a agendamentos uniformes (padrão: 1). | INT | Sim | 1 or higher |
| `ciclo_fechado` | Se deve fechar o loop da janela de contexto; aplica-se apenas a agendamentos em loop (padrão: False). | BOOLEAN | Sim | - |
| `método_de_fusão` | O método a ser usado para fundir as janelas de contexto (padrão: "pyramid"). | COMBO | Sim | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | Se deve aplicar o embaralhamento de ruído FreeNoise; melhora a fusão das janelas (padrão: True). | BOOLEAN | Sim | - |
| `reter_primeiro_quadro` | Manter o primeiro quadro I2V em cada janela de contexto (pode ajudar a manter a referência inicial) (padrão: False). | BOOLEAN | Sim | - |
| `dividir_condições_para_janelas` | Se deve dividir múltiplos condicionamentos (criados pelo ConditionCombine) para cada janela com base no índice de região (padrão: False). | BOOLEAN | Sim | - |

**Nota:** `context_stride` afeta apenas agendamentos uniformes, e `closed_loop` aplica-se apenas a agendamentos em loop. O comprimento e a sobreposição do contexto são especificados em quadros reais e são automaticamente convertidos e limitados aos valores mínimos válidos durante o processamento (`context_length` torna-se ((length - 1) / 4) + 1, `context_overlap` torna-se overlap / 4). `context_length` deve seguir a forma 4*n + 1. `retain_first_frame` é destinado ao uso de imagem para vídeo. `split_conds_to_windows` espera múltiplos condicionamentos criados pelo nó ConditionCombine. O parâmetro `fuse_method` inclui várias opções além de apenas "pyramid".

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo com a configuração de janela de contexto aplicada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`

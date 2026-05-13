> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/en.md)

O nó WAN Context Windows (Manual) permite configurar manualmente janelas de contexto para modelos do tipo WAN com processamento bidimensional. Ele aplica configurações personalizadas de janela de contexto durante a amostragem, especificando o comprimento da janela, a sobreposição, o método de agendamento e a técnica de fusão. Isso oferece controle preciso sobre como o modelo processa informações em diferentes regiões de contexto.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | MODEL | Sim | - | O modelo ao qual aplicar as janelas de contexto durante a amostragem. |
| `context_length` | INT | Sim | 1 a 1048576 | O comprimento da janela de contexto (padrão: 81). |
| `context_overlap` | INT | Sim | 0 a 1048576 | A sobreposição da janela de contexto (padrão: 30). |
| `context_schedule` | COMBO | Sim | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` | O passo da janela de contexto. |
| `context_stride` | INT | Sim | 1 a 1048576 | O passo da janela de contexto; aplicável apenas a agendamentos uniformes (padrão: 1). |
| `closed_loop` | BOOLEAN | Sim | - | Se deve fechar o loop da janela de contexto; aplicável apenas a agendamentos em loop (padrão: Falso). |
| `fuse_method` | COMBO | Sim | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` | O método a ser usado para fundir as janelas de contexto (padrão: "pyramid"). |
| `freenoise` | BOOLEAN | Sim | - | Se deve aplicar a mistura de ruído FreeNoise, melhora a mesclagem das janelas (padrão: Falso). |

**Nota:** O parâmetro `context_stride` afeta apenas agendamentos uniformes, e `closed_loop` se aplica apenas a agendamentos em loop. Os valores de comprimento e sobreposição do contexto são ajustados automaticamente para garantir valores mínimos válidos durante o processamento. O parâmetro `fuse_method` agora inclui opções adicionais além de apenas "pyramid".

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model` | MODEL | O modelo com a configuração de janela de contexto aplicada. |

---
**Source fingerprint (SHA-256):** `33e539f1e6647a6a2bc98fadc357a25279b0900746f5b3d568e2782cdb770258`

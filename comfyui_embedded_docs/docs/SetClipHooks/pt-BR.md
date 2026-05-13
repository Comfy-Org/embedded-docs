> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetClipHooks/pt-BR.md)

O nó SetClipHooks permite aplicar hooks personalizados a um modelo CLIP, possibilitando modificações avançadas em seu comportamento. Ele pode aplicar hooks às saídas de condicionamento e, opcionalmente, ativar a funcionalidade de agendamento do CLIP. Este nó cria uma cópia clonada do modelo CLIP de entrada com as configurações de hook especificadas aplicadas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `clip` | CLIP | Sim | - | O modelo CLIP ao qual aplicar os hooks |
| `apply_to_conds` | BOOLEAN | Sim | - | Se deve aplicar hooks às saídas de condicionamento (padrão: True) |
| `schedule_clip` | BOOLEAN | Sim | - | Se deve ativar o agendamento do CLIP (padrão: False) |
| `hooks` | HOOKS | Não | - | Grupo opcional de hooks a ser aplicado ao modelo CLIP |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `clip` | CLIP | Um modelo CLIP clonado com os hooks especificados aplicados |

---
**Source fingerprint (SHA-256):** `904a878638c015bdce1983ae0c11a2b580b271090fca39edb304f6ed90c8c66d`

O nó SetClipHooks permite aplicar hooks personalizados a um modelo CLIP, possibilitando modificações avançadas em seu comportamento. Ele pode aplicar hooks às saídas de condicionamento e, opcionalmente, ativar a funcionalidade de agendamento do CLIP. Este nó cria uma cópia clonada do modelo CLIP de entrada com as configurações de hook especificadas aplicadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP ao qual aplicar os hooks | CLIP | Sim | - |
| `aplicar_a_conds` | Se deve aplicar hooks às saídas de condicionamento (padrão: True) | BOOLEAN | Sim | - |
| `agendar_clip` | Se deve ativar o agendamento do CLIP (padrão: False) | BOOLEAN | Sim | - |
| `hooks` | Grupo opcional de hooks a ser aplicado ao modelo CLIP | HOOKS | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `clip` | Um modelo CLIP clonado com os hooks especificados aplicados | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetClipHooks/pt-BR.md)

---
**Source fingerprint (SHA-256):** `904a878638c015bdce1983ae0c11a2b580b271090fca39edb304f6ed90c8c66d`

# CLIPMergeAdd

O nó CLIPMergeAdd combina dois modelos CLIP adicionando patches do segundo modelo ao primeiro modelo. Ele cria uma cópia do primeiro modelo CLIP e incorpora seletivamente patches-chave do segundo modelo, excluindo IDs de posição e parâmetros de escala logit. Isso permite mesclar componentes de modelos CLIP preservando a estrutura do modelo base.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip1` | O modelo CLIP base que será clonado e usado como base para a mesclagem | CLIP | Sim | - |
| `clip2` | O modelo CLIP secundário que fornece patches-chave a serem adicionados ao modelo base | CLIP | Sim | - |

## Saídas

| Nome de Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CLIP` | Um modelo CLIP mesclado contendo a estrutura do modelo base com patches adicionados do modelo secundário | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e6271ea9139598eb580f79ce63ff5d92307d7ed93f57cdc666c5e022b671a0dd`

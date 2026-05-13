> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/pt-BR.md)

O nó CLIPMergeAdd combina dois modelos CLIP adicionando patches do segundo modelo ao primeiro modelo. Ele cria uma cópia do primeiro modelo CLIP e incorpora seletivamente patches-chave do segundo modelo, excluindo IDs de posição e parâmetros de escala logit. Isso permite mesclar componentes de modelos CLIP preservando a estrutura do modelo base.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip1` | CLIP | Sim | - | O modelo CLIP base que será clonado e usado como base para a mesclagem |
| `clip2` | CLIP | Sim | - | O modelo CLIP secundário que fornece patches-chave a serem adicionados ao modelo base |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Um modelo CLIP mesclado contendo a estrutura do modelo base com patches adicionados do modelo secundário |

---
**Source fingerprint (SHA-256):** `f212c2750f317ad51516a10a1a03a838b75bc878333381348d5eb388a2faf516`

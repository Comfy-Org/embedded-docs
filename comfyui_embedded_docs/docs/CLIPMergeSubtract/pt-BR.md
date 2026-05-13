> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/pt-BR.md)

O nó CLIPMergeSubtract realiza a fusão de modelos subtraindo os pesos de um modelo CLIP de outro. Ele cria um novo modelo CLIP clonando o primeiro modelo e, em seguida, subtraindo os patches-chave do segundo modelo, com um multiplicador ajustável para controlar a intensidade da subtração. Isso permite uma combinação refinada de modelos, removendo características específicas do modelo base.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `clip1` | CLIP | Sim | - | O modelo CLIP base que será clonado e modificado |
| `clip2` | CLIP | Sim | - | O modelo CLIP cujos patches-chave serão subtraídos do modelo base |
| `multiplier` | FLOAT | Sim | -10.0 a 10.0 | Controla a intensidade da operação de subtração (padrão: 1.0) |

**Observação:** O nó exclui os parâmetros `.position_ids` e `.logit_scale` da operação de subtração, independentemente do valor do multiplicador.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `clip` | CLIP | O modelo CLIP resultante após subtrair os pesos do segundo modelo do primeiro |

---
**Source fingerprint (SHA-256):** `3136cf509fcbfa291af8f820928a6cc14de7a586f953af0ada9bea949b437d86`

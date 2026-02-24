> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/pt-BR.md)

O nó CLIPMergeSubtract realiza a fusão de modelos subtraindo os pesos de um modelo CLIP de outro. Ele cria um novo modelo CLIP clonando o primeiro modelo e, em seguida, subtraindo os *key patches* do segundo modelo, com um multiplicador ajustável para controlar a força da subtração. Isso permite uma mesclagem de modelos com ajuste fino, removendo características específicas do modelo base.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip1` | CLIP | Sim | - | O modelo CLIP base que será clonado e modificado |
| `clip2` | CLIP | Sim | - | O modelo CLIP cujos *key patches* serão subtraídos do modelo base |
| `multiplier` | FLOAT | Sim | -10.0 a 10.0 | Controla a força da operação de subtração (padrão: 1.0) |

**Observação:** O nó exclui os parâmetros `.position_ids` e `.logit_scale` da operação de subtração, independentemente do valor do multiplicador.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `clip` | CLIP | O modelo CLIP resultante após subtrair os pesos do segundo modelo do primeiro |

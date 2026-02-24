> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/pt-BR.md)

O nó CLIPMergeAdd combina dois modelos CLIP adicionando patches do segundo modelo ao primeiro. Ele cria uma cópia do primeiro modelo CLIP e incorpora seletivamente patches-chave do segundo modelo, excluindo IDs de posição e parâmetros de escala de logit. Isso permite mesclar componentes de modelos CLIP preservando a estrutura do modelo base.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip1` | CLIP | Sim | - | O modelo CLIP base que será clonado e usado como fundamento para a mesclagem |
| `clip2` | CLIP | Sim | - | O modelo CLIP secundário que fornece os patches-chave a serem adicionados ao modelo base |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Um modelo CLIP mesclado contendo a estrutura do modelo base com patches adicionados do modelo secundário |

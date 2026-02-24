> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/pt-BR.md)

O nó CLIPSubtract realiza uma operação de subtração entre dois modelos CLIP. Ele utiliza o primeiro modelo CLIP como base e subtrai os *key patches* do segundo modelo CLIP, com um multiplicador opcional para controlar a intensidade da subtração. Isso permite uma mesclagem de modelos ajustada, removendo características específicas de um modelo usando outro.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `clip1` | CLIP | Obrigatório | - | - | O modelo CLIP base que será modificado |
| `clip2` | CLIP | Obrigatório | - | - | O modelo CLIP cujos *key patches* serão subtraídos do modelo base |
| `multiplier` | FLOAT | Obrigatório | 1.0 | -10.0 a 10.0, passo 0.01 | Controla a intensidade da operação de subtração |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `CLIP` | CLIP | O modelo CLIP resultante após a operação de subtração |

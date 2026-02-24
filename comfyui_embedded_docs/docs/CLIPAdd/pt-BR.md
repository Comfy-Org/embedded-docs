> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAdd/pt-BR.md)

O nó CLIPAdd combina dois modelos CLIP mesclando seus *patches* de chave. Ele cria uma cópia do primeiro modelo CLIP e, em seguida, adiciona a maioria dos *patches* de chave do segundo modelo, excluindo os parâmetros de IDs de posição e escala de logit. Isso permite que você misture características de diferentes modelos CLIP, preservando a estrutura do primeiro modelo.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `clip1` | CLIP | Obrigatório | - | - | O modelo CLIP principal que será usado como base para a mesclagem |
| `clip2` | CLIP | Obrigatório | - | - | O modelo CLIP secundário que fornece *patches* adicionais a serem incorporados |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Retorna um modelo CLIP mesclado, combinando características de ambos os modelos de entrada |

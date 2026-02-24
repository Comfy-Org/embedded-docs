> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/pt-BR.md)

Este nó utiliza o modelo Kling AI para gerar um vídeo a partir de uma descrição textual. Ele envia seu *prompt* para uma API remota e retorna o vídeo gerado. O nó permite controlar a duração, o formato e a qualidade do vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Sim | `"kling-video-o1"` | O modelo Kling específico a ser usado para a geração de vídeo. |
| `prompt` | STRING | Sim | 1 a 2500 caracteres | Um *prompt* textual descrevendo o conteúdo do vídeo. Pode incluir descrições positivas e negativas. |
| `aspect_ratio` | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` | A forma ou dimensões do vídeo a ser gerado. |
| `duration` | COMBO | Sim | `5`<br>`10` | A duração do vídeo em segundos. |
| `resolution` | COMBO | Não | `"1080p"`<br>`"720p"` | A qualidade ou resolução em pixels do vídeo (padrão: `"1080p"`). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado com base no *prompt* textual fornecido. |

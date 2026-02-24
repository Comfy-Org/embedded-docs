> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/pt-BR.md)

O nó Kling Text to Video with Audio gera um vídeo curto a partir de uma descrição em texto. Ele envia uma solicitação para o serviço Kling AI, que processa o prompt e retorna um arquivo de vídeo. O nó também pode gerar áudio de acompanhamento para o vídeo com base no texto.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Sim | `"kling-v2-6"` | O modelo de IA específico a ser usado para a geração do vídeo. |
| `prompt` | STRING | Sim | - | Prompt de texto positivo. A descrição usada para gerar o vídeo. Deve ter entre 1 e 2500 caracteres. |
| `mode` | COMBO | Sim | `"pro"` | O modo operacional para a geração do vídeo. |
| `aspect_ratio` | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` | A proporção largura-altura desejada para o vídeo gerado. |
| `duration` | COMBO | Sim | `5`<br>`10` | A duração do vídeo em segundos. |
| `generate_audio` | BOOLEAN | Não | - | Controla se o áudio é gerado para o vídeo. Quando habilitado, a IA criará som com base no prompt. (padrão: `True`) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado. |

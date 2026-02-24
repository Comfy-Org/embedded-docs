> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/pt-BR.md)

O nó Kling Image(First Frame) to Video with Audio utiliza o modelo Kling AI para gerar um vídeo curto a partir de uma única imagem inicial e um prompt de texto. Ele cria uma sequência de vídeo que começa com a imagem fornecida e pode, opcionalmente, incluir áudio gerado por IA para acompanhar a parte visual.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Sim | `"kling-v2-6"` | A versão específica do modelo Kling AI a ser usada para a geração do vídeo. |
| `start_frame` | IMAGE | Sim | - | A imagem que servirá como o primeiro quadro do vídeo gerado. A imagem deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2.5 e 2.5:1. |
| `prompt` | STRING | Sim | - | Prompt de texto positivo. Descreve o conteúdo do vídeo que você deseja gerar. O prompt deve ter entre 1 e 2500 caracteres. |
| `mode` | COMBO | Sim | `"pro"` | O modo operacional para a geração do vídeo. |
| `duration` | COMBO | Sim | `5`<br>`10` | A duração do vídeo a ser gerado, em segundos. |
| `generate_audio` | BOOLEAN | Não | - | Quando habilitado, o nó irá gerar áudio para acompanhar o vídeo. Quando desabilitado, o vídeo será silencioso. (padrão: Verdadeiro) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `video` | VIDEO | O arquivo de vídeo gerado, que pode incluir áudio dependendo da entrada `generate_audio`. |

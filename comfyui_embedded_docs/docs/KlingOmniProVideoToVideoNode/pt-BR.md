> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/pt-BR.md)

Este nó utiliza o modelo Kling AI para gerar um novo vídeo com base em um vídeo de entrada e imagens de referência opcionais. Você fornece um prompt de texto descrevendo o conteúdo desejado, e o nó transforma o vídeo de referência de acordo. Ele também pode incorporar até quatro imagens de referência adicionais para orientar o estilo e o conteúdo da saída.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Sim | `"kling-video-o1"` | O modelo Kling específico a ser usado para a geração do vídeo. |
| `prompt` | STRING | Sim | N/A | Um prompt de texto descrevendo o conteúdo do vídeo. Pode incluir descrições positivas e negativas. |
| `aspect_ratio` | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` | A proporção de tela desejada para o vídeo gerado. |
| `duration` | INT | Sim | 3 a 10 | A duração do vídeo gerado em segundos (padrão: 3). |
| `reference_video` | VIDEO | Sim | N/A | Vídeo a ser usado como referência. |
| `keep_original_sound` | BOOLEAN | Sim | N/A | Determina se o áudio do vídeo de referência é mantido na saída (padrão: Verdadeiro). |
| `reference_images` | IMAGE | Não | N/A | Até 4 imagens de referência adicionais. |
| `resolution` | COMBO | Não | `"1080p"`<br>`"720p"` | A resolução para o vídeo gerado (padrão: "1080p"). |

**Restrições dos Parâmetros:**

* O `prompt` deve ter entre 1 e 2500 caracteres.
* O `reference_video` deve ter uma duração entre 3,0 e 10,05 segundos.
* O `reference_video` deve ter dimensões entre 720x720 e 2160x2160 pixels.
* Um máximo de 4 `reference_images` pode ser fornecido. Cada imagem deve ter pelo menos 300x300 pixels e uma proporção de tela entre 1:2,5 e 2,5:1.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo recém-gerado. |

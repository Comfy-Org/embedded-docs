> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/pt-BR.md)

Este nó gera um vídeo usando um prompt de texto junto com imagens do primeiro e do último quadro. Ele utiliza sua descrição e os dois quadros-chave para criar uma sequência de vídeo completa que transita entre eles. O nó oferece várias opções para controlar a resolução, proporção de tela, duração e outros parâmetros de geração do vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | COMBO | combo | seedance_1_lite | seedance_1_lite | Nome do modelo |
| `prompt` | STRING | string | - | - | O prompt de texto usado para gerar o vídeo. |
| `first_frame` | IMAGE | image | - | - | Primeiro quadro a ser usado para o vídeo. |
| `last_frame` | IMAGE | image | - | - | Último quadro a ser usado para o vídeo. |
| `resolution` | COMBO | combo | - | 480p, 720p, 1080p | A resolução do vídeo de saída. |
| `aspect_ratio` | COMBO | combo | - | adaptive, 16:9, 4:3, 1:1, 3:4, 9:16, 21:9 | A proporção de tela do vídeo de saída. |
| `duration` | INT | slider | 5 | 3-12 | A duração do vídeo de saída em segundos. |
| `seed` | INT | number | 0 | 0-2147483647 | Semente a ser usada para a geração. (opcional) |
| `camera_fixed` | BOOLEAN | boolean | False | - | Especifica se a câmera deve ser fixa. A plataforma anexa uma instrução para fixar a câmera ao seu prompt, mas não garante o efeito real. (opcional) |
| `watermark` | BOOLEAN | boolean | True | - | Se deve adicionar uma marca d'água "Gerado por IA" ao vídeo. (opcional) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado |

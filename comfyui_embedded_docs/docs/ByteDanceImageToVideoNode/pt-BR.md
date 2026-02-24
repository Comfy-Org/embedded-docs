> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/pt-BR.md)

O nó ByteDance Image to Video gera vídeos usando modelos da ByteDance por meio de uma API, com base em uma imagem de entrada e um prompt de texto. Ele utiliza um quadro inicial de imagem e cria uma sequência de vídeo que segue a descrição fornecida. O nó oferece várias opções de personalização para resolução, proporção de tela, duração e outros parâmetros de geração do vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | STRING | COMBO | seedance_1_pro | Opções de Image2VideoModelName | Nome do modelo |
| `prompt` | STRING | STRING | - | - | O prompt de texto usado para gerar o vídeo. |
| `image` | IMAGE | IMAGE | - | - | Primeiro quadro a ser usado para o vídeo. |
| `resolution` | STRING | COMBO | - | ["480p", "720p", "1080p"] | A resolução do vídeo de saída. |
| `aspect_ratio` | STRING | COMBO | - | ["adaptive", "16:9", "4:3", "1:1", "3:4", "9:16", "21:9"] | A proporção de tela do vídeo de saída. |
| `duration` | INT | INT | 5 | 3-12 | A duração do vídeo de saída em segundos. |
| `seed` | INT | INT | 0 | 0-2147483647 | Semente a ser usada para a geração. |
| `camera_fixed` | BOOLEAN | BOOLEAN | False | - | Especifica se a câmera deve ser fixa. A plataforma anexa uma instrução para fixar a câmera ao seu prompt, mas não garante o efeito real. |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Se deve adicionar uma marca d'água "Gerado por IA" ao vídeo. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado com base na imagem de entrada e nos parâmetros do prompt. |

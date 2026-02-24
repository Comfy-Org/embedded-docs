> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/pt-BR.md)

O nó ByteDance Image Reference gera vídeos usando um prompt de texto e de uma a quatro imagens de referência. Ele envia as imagens e o prompt para um serviço de API externo que cria um vídeo correspondente à sua descrição, incorporando o estilo visual e o conteúdo das suas imagens de referência. O nó oferece vários controles para resolução do vídeo, proporção de tela, duração e outros parâmetros de geração.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seedance_1_lite | seedance_1_lite | Nome do modelo. |
| `prompt` | STRING | STRING | - | - | O prompt de texto usado para gerar o vídeo. |
| `images` | IMAGE | IMAGE | - | - | De uma a quatro imagens. |
| `resolution` | STRING | COMBO | - | 480p, 720p | A resolução do vídeo de saída. |
| `aspect_ratio` | STRING | COMBO | - | adaptativa, 16:9, 4:3, 1:1, 3:4, 9:16, 21:9 | A proporção de tela do vídeo de saída. |
| `duration` | INT | INT | 5 | 3-12 | A duração do vídeo de saída em segundos. |
| `seed` | INT | INT | 0 | 0-2147483647 | Semente a ser usada para a geração. |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Se deve adicionar uma marca d'água "Gerado por IA" ao vídeo. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado com base no prompt de entrada e nas imagens de referência. |

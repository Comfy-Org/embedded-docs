> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/pt-BR.md)

Este nó utiliza o modelo Kling AI para gerar um vídeo com base em um prompt de texto e até sete imagens de referência. Ele permite controlar a proporção, duração e resolução do vídeo. O nó envia a solicitação para uma API externa e retorna o vídeo gerado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Sim | `"kling-video-o1"` | O modelo Kling específico a ser usado para a geração de vídeo. |
| `prompt` | STRING | Sim | - | Um prompt de texto descrevendo o conteúdo do vídeo. Pode incluir descrições positivas e negativas. O texto é normalizado automaticamente e deve ter entre 1 e 2500 caracteres. |
| `aspect_ratio` | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` | A proporção de aspecto desejada para o vídeo gerado. |
| `duration` | INT | Sim | 3 a 10 | A duração do vídeo em segundos. O valor pode ser ajustado com um controle deslizante (padrão: 3). |
| `reference_images` | IMAGE | Sim | - | Até 7 imagens de referência. Cada imagem deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2,5 e 2,5:1. |
| `resolution` | COMBO | Não | `"1080p"`<br>`"720p"` | A resolução de saída do vídeo. Este parâmetro é opcional (padrão: "1080p"). |

**Observação:** A entrada `reference_images` aceita no máximo 7 imagens. Se mais forem fornecidas, o nó retornará um erro. Cada imagem é validada quanto às dimensões mínimas e à proporção de aspecto.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado. |

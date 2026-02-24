> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/pt-BR.md)

O nó PikaFrames v2.2 gera vídeos combinando seu primeiro e último quadro. Você faz upload de duas imagens para definir os pontos inicial e final, e a IA cria uma transição suave entre elas para produzir um vídeo completo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image_start` | IMAGE | Sim | - | A primeira imagem a ser combinada. |
| `image_end` | IMAGE | Sim | - | A última imagem a ser combinada. |
| `prompt_text` | STRING | Sim | - | Prompt de texto descrevendo o conteúdo de vídeo desejado. |
| `negative_prompt` | STRING | Sim | - | Texto descrevendo o que evitar no vídeo. |
| `seed` | INT | Sim | - | Valor de semente aleatória para consistência na geração. |
| `resolution` | STRING | Sim | - | Resolução do vídeo de saída. |
| `duration` | INT | Sim | - | Duração do vídeo gerado. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado, combinando os quadros inicial e final com transições de IA. |

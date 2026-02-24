> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToVideoApi/pt-BR.md)

O nó Wan Text to Video gera conteúdo de vídeo com base em descrições de texto. Ele utiliza modelos de IA para criar vídeos a partir de prompts e suporta vários tamanhos de vídeo, durações e entradas de áudio opcionais. O nó pode gerar áudio automaticamente quando necessário e oferece opções para aprimoramento de prompt e marca d'água.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | "wan2.5-t2v-preview" | Modelo a ser utilizado (padrão: "wan2.5-t2v-preview") |
| `prompt` | STRING | Sim | - | Prompt usado para descrever os elementos e características visuais, suporta inglês/chinês (padrão: "") |
| `negative_prompt` | STRING | Não | - | Prompt de texto negativo para orientar o que evitar (padrão: "") |
| `size` | COMBO | Não | "480p: 1:1 (624x624)"<br>"480p: 16:9 (832x480)"<br>"480p: 9:16 (480x832)"<br>"720p: 1:1 (960x960)"<br>"720p: 16:9 (1280x720)"<br>"720p: 9:16 (720x1280)"<br>"720p: 4:3 (1088x832)"<br>"720p: 3:4 (832x1088)"<br>"1080p: 1:1 (1440x1440)"<br>"1080p: 16:9 (1920x1080)"<br>"1080p: 9:16 (1080x1920)"<br>"1080p: 4:3 (1632x1248)"<br>"1080p: 3:4 (1248x1632)" | Resolução e proporção de tela do vídeo (padrão: "480p: 1:1 (624x624)") |
| `duration` | INT | Não | 5-10 | Durações disponíveis: 5 e 10 segundos (padrão: 5) |
| `audio` | AUDIO | Não | - | O áudio deve conter uma voz clara e alta, sem ruídos externos ou música de fundo |
| `seed` | INT | Não | 0-2147483647 | Semente a ser usada para a geração (padrão: 0) |
| `generate_audio` | BOOLEAN | Não | - | Se não houver entrada de áudio, gerar áudio automaticamente (padrão: False) |
| `prompt_extend` | BOOLEAN | Não | - | Se deve aprimorar o prompt com assistência de IA (padrão: True) |
| `watermark` | BOOLEAN | Não | - | Se deve adicionar uma marca d'água "AI generated" ao resultado (padrão: True) |

**Observação:** O parâmetro `duration` aceita apenas valores de 5 ou 10 segundos, pois essas são as durações disponíveis. Ao fornecer uma entrada de áudio, ela deve ter entre 3,0 e 29,0 segundos de duração e conter voz clara sem ruído de fundo ou música.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado com base nos parâmetros de entrada |

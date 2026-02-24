> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideoApi/pt-BR.md)

O nó Wan Image to Video gera conteúdo de vídeo a partir de uma única imagem de entrada e um prompt de texto. Ele cria sequências de vídeo estendendo o quadro inicial de acordo com a descrição fornecida, com opções para controlar a qualidade do vídeo, duração e integração de áudio.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | "wan2.5-i2v-preview"<br>"wan2.5-i2v-preview" | Modelo a ser utilizado (padrão: "wan2.5-i2v-preview") |
| `image` | IMAGE | Sim | - | Imagem de entrada que serve como o primeiro quadro para a geração do vídeo |
| `prompt` | STRING | Sim | - | Prompt usado para descrever os elementos e características visuais, suporta inglês/chinês (padrão: vazio) |
| `negative_prompt` | STRING | Não | - | Prompt de texto negativo para orientar o que evitar (padrão: vazio) |
| `resolution` | COMBO | Não | "480P"<br>"720P"<br>"1080P" | Qualidade de resolução do vídeo (padrão: "480P") |
| `duration` | INT | Não | 5-10 | Durações disponíveis: 5 e 10 segundos (padrão: 5) |
| `audio` | AUDIO | Não | - | O áudio deve conter uma voz clara e alta, sem ruídos estranhos ou música de fundo |
| `seed` | INT | Não | 0-2147483647 | Semente a ser usada para a geração (padrão: 0) |
| `generate_audio` | BOOLEAN | Não | - | Se não houver entrada de áudio, gera áudio automaticamente (padrão: Falso) |
| `prompt_extend` | BOOLEAN | Não | - | Se deve aprimorar o prompt com assistência de IA (padrão: Verdadeiro) |
| `watermark` | BOOLEAN | Não | - | Se deve adicionar uma marca d'água "Gerado por IA" ao resultado (padrão: Verdadeiro) |

**Restrições:**

- Exatamente uma imagem de entrada é necessária para a geração do vídeo
- O parâmetro de duração aceita apenas valores de 5 ou 10 segundos
- Quando o áudio é fornecido, ele deve ter uma duração entre 3,0 e 29,0 segundos

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | Vídeo gerado com base na imagem de entrada e no prompt |

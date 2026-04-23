> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/pt-BR.md)

O nó Wan2VideoEditApi utiliza o modelo Wan 2.7 para editar um vídeo com base em instruções de texto, imagens de referência ou transferência de estilo. Ele processa o vídeo de entrada e gera um novo vídeo de acordo com os parâmetros especificados, como resolução, duração e proporção de aspecto.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"wan2.7-videoedit"` | O modelo a ser usado para edição de vídeo. |
| `model.prompt` | STRING | Sim | - | Instruções de edição ou requisitos de transferência de estilo. (padrão: string vazia) |
| `model.resolution` | COMBO | Sim | `"720P"`<br>`"1080P"` | A resolução do vídeo de saída. |
| `model.ratio` | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | A proporção de aspecto do vídeo de saída. Se não for alterada, aproxima-se da proporção do vídeo de entrada. |
| `model.duration` | COMBO | Sim | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` | A duração da saída em segundos. 'auto' corresponde à duração do vídeo de entrada. Um valor específico trunca a partir do início do vídeo. (padrão: "auto") |
| `model.reference_images` | IMAGE | Não | - | Uma lista de até 4 imagens de referência para orientar a edição. |
| `video` | VIDEO | Sim | - | O vídeo a ser editado. |
| `seed` | INT | Não | 0 a 2147483647 | A semente a ser usada para a geração. (padrão: 0) |
| `audio_setting` | COMBO | Não | `"auto"`<br>`"origin"` | 'auto': o modelo decide se deve regenerar o áudio com base no prompt. 'origin': preserva o áudio original do vídeo de entrada. (padrão: "auto") |
| `watermark` | BOOLEAN | Não | - | Se deve adicionar uma marca d'água gerada por IA ao resultado. (padrão: Falso) |

**Restrições:**
*   O `model.prompt` deve ter pelo menos 1 caractere.
*   O `video` de entrada deve ter duração entre 2 e 10 segundos.
*   A entrada `model.reference_images` pode aceitar no máximo 4 imagens.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O vídeo editado gerado pelo modelo. |
O nó Wan2VideoEditApi utiliza o modelo Wan 2.7 para editar um vídeo com base em instruções de texto, imagens de referência ou transferência de estilo. Ele processa o vídeo de entrada e gera um novo vídeo de acordo com os parâmetros especificados, como resolução, duração e proporção de aspecto.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo a ser usado para edição de vídeo. | COMBO | Sim | `"wan2.7-videoedit"` |
| `model.prompt` | Instruções de edição ou requisitos de transferência de estilo. (padrão: string vazia) | STRING | Sim | - |
| `model.resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"720P"`<br>`"1080P"` |
| `model.ratio` | A proporção de aspecto do vídeo de saída. Se não for alterada, aproxima-se da proporção do vídeo de entrada. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `model.duration` | A duração da saída em segundos. 'auto' corresponde à duração do vídeo de entrada. Um valor específico trunca a partir do início do vídeo. (padrão: "auto") | COMBO | Sim | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `model.reference_images` | Uma lista de até 4 imagens de referência para orientar a edição. | IMAGE | Não | - |
| `vídeo` | O vídeo a ser editado. | VIDEO | Sim | - |
| `semente` | A semente a ser usada para a geração. (padrão: 0) | INT | Não | 0 a 2147483647 |
| `configuração_de_áudio` | 'auto': o modelo decide se deve regenerar o áudio com base no prompt. 'origin': preserva o áudio original do vídeo de entrada. (padrão: "auto") | COMBO | Não | `"auto"`<br>`"origin"` |
| `marca_d'água` | Se deve adicionar uma marca d'água gerada por IA ao resultado. (padrão: False) | BOOLEAN | Não | - |

**Restrições:**
*   O `model.prompt` deve ter pelo menos 1 caractere.
*   O `video` de entrada deve ter entre 2 e 10 segundos de duração.
*   A entrada `model.reference_images` pode aceitar no máximo 4 imagens.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo editado gerado pelo modelo. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d2dd65d743358c6a357e75076774e93c52c39893fbb376da2f4395446f440a20`

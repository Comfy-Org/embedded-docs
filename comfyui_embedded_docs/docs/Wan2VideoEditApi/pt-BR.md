# Wan 2.7 Edição de Vídeo

O nó Wan2VideoEditApi usa o modelo Wan 2.7 para editar um vídeo com base em instruções de texto, imagens de referência ou transferência de estilo. Ele processa o vídeo de entrada e gera um novo vídeo de acordo com os parâmetros especificados, como resolução, duração e proporção de aspecto.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo a ser usado para edição de vídeo. | COMBO | Sim | `"wan2.7-videoedit"` |
| `video` | O vídeo a ser editado. | VIDEO | Sim | - |
| `seed` | Semente a ser usada para a geração. (padrão: 0) | INT | Não | 0 a 2147483647 |
| `audio_setting` | 'auto': o modelo decide se deve regenerar o áudio com base no prompt. 'origin': preserva o áudio original do vídeo de entrada. (padrão: "auto") | COMBO | Não | `"auto"`<br>`"origin"` |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado. (padrão: False) | BOOLEAN | Não | - |

### Entradas do wan2.7-videoedit

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Instruções de edição ou requisitos de transferência de estilo. (padrão: string vazia) | STRING | Sim | - |
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"720P"`<br>`"1080P"` |
| `ratio` | Proporção de aspecto. Se não for alterada, aproxima a proporção do vídeo de entrada. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Duração da saída em segundos. 'auto' corresponde à duração do vídeo de entrada. Um valor específico corta a partir do início do vídeo. (padrão: "auto") | COMBO | Sim | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |

### Entradas de Referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot expansível: conecte de 0 a 4 imagens (`image1`...`image4`) para orientar a edição. O limite de contagem é 4 para o modelo wan2.7-videoedit. | IMAGE | Não | 0 a 4 itens |

**Restrições:**
*   O `prompt` deve conter pelo menos 1 caractere.
*   O `video` de entrada deve ter entre 2 e 10 segundos de duração.
*   O slot expansível `reference_images` aceita no máximo 4 imagens.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O vídeo editado gerado pelo modelo. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `27283273ee56c90903db103a3e9bc17dc4df0914676c9aedd2a115b07937dc10`

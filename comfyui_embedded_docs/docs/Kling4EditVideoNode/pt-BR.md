# Kling 4.0 Edição de Vídeo

Edita um vídeo existente com um prompt de texto usando o modelo Kling 4.0, opcionalmente guiado por vídeos de referência e imagens de referência. O resultado mantém a duração do vídeo de entrada. Use-o para mudar o que acontece em um clipe, alterar o estilo ou trocar elementos enquanto a temporização original permanece intacta.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Seletor de modelo. `"kling-4.0"` oferece suporte a edições em 1080p de até 30 segundos; `"kling-4.0-flash"` é limitado a 720p e 20 segundos. Selecionar um modelo revela suas entradas abaixo. | DYNAMIC_COMBO | Sim | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Entradas do kling-4.0

Estas entradas aparecem quando `model` está definido como `"kling-4.0"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `video_1` | O vídeo a ser editado, com 3 a 30 segundos de duração. A saída mantém a mesma duração. | VIDEO | Sim | 3 a 30 segundos |
| `reference_videos` | Slots expansíveis para vídeos de referência, até 4. Refira-se a eles no prompt como `@Video2` e assim por diante. Cada vídeo e todos os vídeos juntos devem ter de 3 a 30 segundos de duração. | AUTOGROW | Não | 0 a 4 vídeos |
| `reference_images` | Slots expansíveis para imagens de referência, até 10. Refira-se a elas no prompt como `@Image1`, `@Image2` e assim por diante. | AUTOGROW | Não | 0 a 10 imagens |
| `prompt` | Descrição do que alterar e do que manter. Refira-se ao vídeo sendo editado como `@Video1`, aos vídeos de referência como `@Video2` e assim por diante, e às imagens como `@Image1` e assim por diante. | STRING | Sim | 1 a 26000 caracteres |
| `resolution` | Resolução do vídeo de saída. Padrão: `"720p"`. | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Proporção de aspecto do vídeo de saída. `"adaptive"` mantém a proporção de aspecto do vídeo de entrada. Padrão: `"adaptive"`. | COMBO | Sim | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |
| `audio` | `"native"` gera um novo áudio para o vídeo editado; `"original"` mantém o áudio do vídeo de entrada. Padrão: `"native"`. | COMBO | Não | `"native"`<br>`"original"` |

### Entradas do kling-4.0-flash

Estas entradas aparecem quando `model` está definido como `"kling-4.0-flash"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `video_1` | O vídeo a ser editado, com 3 a 20 segundos de duração. A saída mantém a mesma duração. | VIDEO | Sim | 3 a 20 segundos |
| `reference_videos` | Slots expansíveis para vídeos de referência, até 4. Refira-se a eles no prompt como `@Video2` e assim por diante. Cada vídeo e todos os vídeos juntos devem ter de 3 a 20 segundos de duração. | AUTOGROW | Não | 0 a 4 vídeos |
| `reference_images` | Slots expansíveis para imagens de referência, até 10. Refira-se a elas no prompt como `@Image1`, `@Image2` e assim por diante. | AUTOGROW | Não | 0 a 10 imagens |
| `prompt` | Descrição do que alterar e do que manter. Refira-se ao vídeo sendo editado como `@Video1`, aos vídeos de referência como `@Video2` e assim por diante, e às imagens como `@Image1` e assim por diante. | STRING | Sim | 1 a 26000 caracteres |
| `resolution` | Resolução do vídeo de saída. O Flash renderiza apenas em 720p. Padrão: `"720p"`. | COMBO | Sim | `"720p"` |
| `aspect_ratio` | Proporção de aspecto do vídeo de saída. `"adaptive"` mantém a proporção de aspecto do vídeo de entrada. Padrão: `"adaptive"`. | COMBO | Sim | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |
| `audio` | `"native"` gera um novo áudio para o vídeo editado; `"original"` mantém o áudio do vídeo de entrada. Padrão: `"native"`. | COMBO | Não | `"native"`<br>`"original"` |

**Restrições e comportamento:**

* O vídeo de entrada e cada vídeo de referência devem ter de 3 a 30 segundos de duração (3 a 20 com `kling-4.0-flash`), pelo menos 700x700 e no máximo 4553x4553 pixels, no máximo 8,294,400 pixels no total, com uma proporção de aspecto entre 2:5 e 5:2 e uma taxa de quadros de pelo menos 24 fps. Todos os vídeos juntos não devem exceder o mesmo limite.
* Cada imagem de referência deve ter pelo menos 300x300 pixels com uma proporção de aspecto entre 2:5 e 5:2, e no máximo 10 imagens podem ser conectadas.
* Um prompt que mencione `@VideoN` ou `@ImageN` gera um erro quando menos de N entradas desse tipo estão conectadas.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `video` | O vídeo editado, baixado do provedor assim que a tarefa for concluída. Tem a mesma duração do vídeo de entrada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4EditVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c682db61e1426059dc565b12c0da749944394f77f34aaa71b97c69f984cb0931`

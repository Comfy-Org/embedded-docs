# Kling 4.0 Referência para Vídeo

Gera um vídeo a partir de imagens e vídeos de referência com o modelo Kling 4.0, incluindo áudio. As referências orientam o sujeito, o estilo e o movimento, e um primeiro e um último quadro opcionais fixam o início e o fim do clipe. Use-o para manter um personagem ou uma cena consistentes ao longo de uma tomada enquanto descreve a ação no prompt.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Seletor de modelo. `"kling-4.0"` suporta até 1080p, clipes de 30 segundos e um último quadro; `"kling-4.0-flash"` é limitado a 720p e 20 segundos e não possui entrada `last_frame`. Selecionar um modelo revela suas entradas abaixo. | DYNAMIC_COMBO | Sim | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Entradas do kling-4.0

Essas entradas aparecem quando `model` está definido como `"kling-4.0"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slots expansíveis para imagens de referência, até 10. Refira-se a elas no prompt como `@Image1`, `@Image2` e assim por diante, na ordem de conexão. | AUTOGROW | Não | 0 a 10 imagens |
| `reference_videos` | Slots expansíveis para vídeos de referência, até 5. Refira-se a eles no prompt como `@Video1`, `@Video2` e assim por diante. Cada vídeo e todos os vídeos juntos devem ter de 3 a 30 segundos de duração. | AUTOGROW | Não | 0 a 5 vídeos |
| `first_frame` | Quadro opcional em que o vídeo começa. Conta para o limite de 10 imagens junto com as imagens de referência. | IMAGE | Não | - |
| `last_frame` | Quadro opcional em que o vídeo termina. Conta para o limite de 10 imagens junto com as imagens de referência. | IMAGE | Não | - |
| `prompt` | Descrição do vídeo a ser gerado. Refira-se às entradas como `@Image1`, `@Image2` e assim por diante, e `@Video1`, `@Video2` e assim por diante. | STRING | Sim | 1 a 26000 caracteres |
| `resolution` | Resolução do vídeo de saída. Padrão: `"720p"`. | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Proporção do vídeo de saída. `"adaptive"` segue o prompt, depois o primeiro quadro ou os vídeos de referência e, caso contrário, recorre a 16:9. Padrão: `"adaptive"`. | COMBO | Sim | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Duração do vídeo gerado em segundos. Padrão: 5. | INT | Sim | 3 a 30 |
| `seed` | A seed controla se o nó deve ser reexecutado; os resultados não são determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

### Entradas do kling-4.0-flash

Essas entradas aparecem quando `model` está definido como `"kling-4.0-flash"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slots expansíveis para imagens de referência, até 10. Refira-se a elas no prompt como `@Image1`, `@Image2` e assim por diante, na ordem de conexão. | AUTOGROW | Não | 0 a 10 imagens |
| `reference_videos` | Slots expansíveis para vídeos de referência, até 5. Refira-se a eles no prompt como `@Video1`, `@Video2` e assim por diante. Cada vídeo e todos os vídeos juntos devem ter de 3 a 20 segundos de duração. | AUTOGROW | Não | 0 a 5 vídeos |
| `first_frame` | Quadro opcional em que o vídeo começa. Conta para o limite de 10 imagens junto com as imagens de referência. | IMAGE | Não | - |
| `prompt` | Descrição do vídeo a ser gerado. Refira-se às entradas como `@Image1`, `@Image2` e assim por diante, e `@Video1`, `@Video2` e assim por diante. | STRING | Sim | 1 a 26000 caracteres |
| `resolution` | Resolução do vídeo de saída. O Flash renderiza apenas em 720p. Padrão: `"720p"`. | COMBO | Sim | `"720p"` |
| `aspect_ratio` | Proporção do vídeo de saída. `"adaptive"` segue o prompt, depois o primeiro quadro ou os vídeos de referência e, caso contrário, recorre a 16:9. Padrão: `"adaptive"`. | COMBO | Sim | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Duração do vídeo gerado em segundos. Padrão: 5. | INT | Sim | 3 a 20 |
| `seed` | A seed controla se o nó deve ser reexecutado; os resultados não são determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Restrições e comportamento:**

* As imagens são limitadas a 10 no total, contando as imagens de referência, o primeiro quadro e o último quadro.
* Cada imagem deve ter pelo menos 300x300 pixels com uma proporção entre 2:5 e 5:2.
* Cada vídeo de referência deve ter de 3 a 30 segundos de duração (3 a 20 com `kling-4.0-flash`), pelo menos 700x700 e no máximo 4553x4553 pixels, não mais de 8,294,400 pixels no total, com uma proporção entre 2:5 e 5:2 e uma taxa de quadros de pelo menos 24 fps. Todos os vídeos de referência juntos não devem exceder o mesmo limite.
* Um prompt que mencione `@ImageN` ou `@VideoN` gera um erro quando menos de N entradas desse tipo estiverem conectadas.
* Quando um primeiro ou um último quadro estiver conectado, o nó adiciona uma instrução de que o vídeo começa ou termina exatamente nesse quadro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo gerado, baixado do provedor assim que a tarefa for concluída. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ReferenceToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `78a85e66ab05f784102829fc86917b363fabad6bb5443c36b83e250e59ed07b7`

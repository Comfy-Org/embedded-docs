# Kling 4.0 Imagem para Vídeo

Gera um vídeo a partir de um conjunto de keyframes com o modelo Kling 4.0, incluindo áudio. O primeiro frame, até oito frames intermediários e o último frame são enviados em ordem, os frames intermediários são distribuídos uniformemente ao longo do clipe e a saída assume a proporção do primeiro keyframe. Use-o para animar uma imagem ou para conduzir uma cena por meio de uma sequência de momentos-chave.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `modelo` | Seletor de modelo. `"kling-4.0"` suporta até 1080p e 30 segundos; `"kling-4.0-flash"` é limitado a 720p, 20 segundos e um único primeiro frame. Selecionar um modelo revela suas entradas abaixo. | DYNAMIC_COMBO | Sim | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Entradas do kling-4.0

Estas entradas aparecem quando `model` está definido como `"kling-4.0"`. Pelo menos uma das entradas de frame deve estar conectada.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `first_frame` | Frame opcional em que o vídeo começa. | IMAGE | Não | - |
| `middle_frames` | Slots expansíveis opcionais para frames entre o primeiro e o último, até 8. Eles são distribuídos uniformemente ao longo do clipe. | AUTOGROW | Não | 0 a 8 imagens |
| `last_frame` | Frame opcional em que o vídeo termina. | IMAGE | Não | - |
| `prompt` | Descrição opcional do movimento. Refira-se aos frames conectados como `@Image1`, `@Image2` e assim por diante, na ordem: primeiro frame, frames intermediários, último frame. Padrão: string vazia. | STRING | Sim | Texto multilinha |
| `resolution` | Resolução do vídeo de saída. Padrão: `"720p"`. | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `duration` | Duração do vídeo gerado em segundos. Padrão: 5. | INT | Sim | 3 a 30 |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

### Entradas do kling-4.0-flash

Estas entradas aparecem quando `model` está definido como `"kling-4.0-flash"`. O Flash anima um único primeiro frame.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `first_frame` | Frame em que o vídeo começa. | IMAGE | Sim | - |
| `prompt` | Descrição opcional do movimento. Refira-se ao primeiro frame como `@Image1`. Padrão: string vazia. | STRING | Sim | Texto multilinha |
| `resolution` | Resolução do vídeo de saída. O Flash renderiza apenas em 720p. Padrão: `"720p"`. | COMBO | Sim | `"720p"` |
| `duration` | Duração do vídeo gerado em segundos. Padrão: 5. | INT | Sim | 3 a 20 |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Restrições e comportamento:**

* No máximo 10 frames podem ser conectados no total, contando o primeiro frame, todos os frames intermediários e o último frame.
* O vídeo assume a proporção do primeiro keyframe, portanto não é necessária uma entrada de proporção.
* Cada frame deve ter pelo menos 300x300 pixels, com uma proporção entre 2:5 e 5:2.
* Um prompt que mencione `@ImageN` gera um erro quando menos de N frames estão conectados.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---------------|-----------|---------------|
| `video` | O vídeo gerado, baixado do provedor assim que a tarefa é concluída. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `248ab33bf7a50afbc08baf1e64e5b1908a38905cda2a87d1303eeeb2755b5a6d`

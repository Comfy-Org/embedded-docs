# Kling 4.0 Imagem para Vídeo

Gera um vídeo a partir de um conjunto de quadros-chave com o modelo Kling 4.0, incluindo áudio. O primeiro quadro, até oito quadros intermediários e o último quadro são enviados em ordem, os quadros intermediários são distribuídos uniformemente ao longo do clipe, e a saída assume a proporção do primeiro quadro-chave. Use-o para animar uma imagem ou conduzir uma tomada por uma sequência de momentos-chave.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Seletor de modelo. `"kling-4.0"` suporta até 4K HDR e 30 segundos; `"kling-4.0-flash"` é limitado a 720p, 20 segundos e um único primeiro quadro. Selecionar um modelo revela suas entradas abaixo. | DYNAMIC_COMBO | Sim | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Entradas do kling-4.0

Essas entradas aparecem quando `model` está definido como `"kling-4.0"`. Pelo menos uma das entradas de quadro deve estar conectada.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | Quadro opcional em que o vídeo começa. | IMAGE | Não | - |
| `middle_frames` | Slots expansíveis opcionais para quadros entre o primeiro e o último, até 8. Eles são distribuídos uniformemente ao longo do clipe. | AUTOGROW | Não | 0 a 8 imagens |
| `last_frame` | Quadro opcional em que o vídeo termina. | IMAGE | Não | - |
| `prompt` | Descrição opcional do movimento. Refira-se aos quadros conectados como `@Image1`, `@Image2` e assim por diante, na ordem primeiro quadro, quadros intermediários, último quadro. Padrão: string vazia. | STRING | Sim | Texto multilinha |
| `resolution` | Resolução do vídeo de saída; uma opção com `HDR` no nome retorna um vídeo HDR. Padrão: `"720p"`. | COMBO | Sim | `"720p"`<br>`"1080p"`<br>`"4k"`<br>`"1080p HDR"`<br>`"4k HDR"` |
| `duration` | Duração do vídeo gerado em segundos. Padrão: 5. | INT | Sim | 3 a 30 |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

### Entradas do kling-4.0-flash

Essas entradas aparecem quando `model` está definido como `"kling-4.0-flash"`. O Flash anima um único primeiro quadro.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | Quadro em que o vídeo começa. | IMAGE | Sim | - |
| `prompt` | Descrição opcional do movimento. Refira-se ao primeiro quadro como `@Image1`. Padrão: string vazia. | STRING | Sim | Texto multilinha |
| `resolution` | Resolução do vídeo de saída. O Flash renderiza apenas em 720p. Padrão: `"720p"`. | COMBO | Sim | `"720p"` |
| `duration` | Duração do vídeo gerado em segundos. Padrão: 5. | INT | Sim | 3 a 20 |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Restrições e comportamento:**

* No máximo 10 quadros podem ser conectados no total, contando o primeiro quadro, cada quadro intermediário e o último quadro.
* O vídeo assume a proporção do primeiro quadro-chave, portanto, nenhuma entrada de proporção é necessária.
* Cada quadro deve ter pelo menos 300x300 pixels, com uma proporção entre 2:5 e 5:2.
* Um prompt que menciona `@ImageN` gera um erro quando menos de N quadros estão conectados.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `video` | O vídeo gerado, baixado do provedor assim que a tarefa for concluída. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `289c96204f02fdd378ae7a4dd5a5685ffa4bf7619d098785b9d1ae148fb3ac4a`

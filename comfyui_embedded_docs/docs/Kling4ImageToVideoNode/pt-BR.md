# Kling 4.0 Image to Video

Gera um vídeo a partir de um conjunto de quadros-chave com o modelo Kling 4.0, incluindo áudio. O primeiro quadro, até oito quadros intermediários e o último quadro são enviados em ordem; os quadros intermediários são espaçados uniformemente ao longo do clipe, e a saída assume a proporção do primeiro quadro-chave. Use-o para animar uma imagem ou conduzir uma tomada por uma sequência de momentos-chave.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Seletor de modelo. Apenas `"kling-4.0"` está disponível; selecioná-lo revela as entradas abaixo. | DYNAMIC_COMBO | Sim | `"kling-4.0"` |

### Entradas do kling-4.0

Estas entradas aparecem quando `model` é definido como `"kling-4.0"`. Pelo menos uma das entradas de quadro deve estar conectada.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | Quadro opcional em que o vídeo começa. | IMAGE | Não | - |
| `middle_frames` | Slots expansíveis opcionais para quadros entre o primeiro e o último, até 8. Eles são espaçados uniformemente ao longo do clipe. | AUTOGROW | Não | 0 a 8 imagens |
| `last_frame` | Quadro opcional em que o vídeo termina. | IMAGE | Não | - |
| `prompt` | Descrição opcional do movimento. Refira-se aos quadros conectados como `@Image1`, `@Image2` e assim por diante, na ordem primeiro quadro, quadros intermediários, último quadro. Padrão: string vazia. | STRING | Sim | Texto multilinha |
| `resolution` | Resolução do vídeo de saída. Padrão: `"720p"`. | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `duration` | Duração do vídeo gerado em segundos. Padrão: 5. | INT | Sim | 3 a 30 |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Restrições e comportamento:**

* No máximo 10 quadros podem ser conectados no total, contando o primeiro quadro, cada quadro intermediário e o último quadro.
* O vídeo assume a proporção do primeiro quadro-chave, então nenhuma entrada de proporção é necessária.
* Cada quadro deve ter pelo menos 300x300 pixels, com proporção entre 2:5 e 5:2.
* Um prompt que menciona `@ImageN` gera um erro quando menos de N quadros estão conectados.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `video` | O vídeo gerado, baixado do provedor assim que a tarefa for concluída. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `762c350abd4a881b96355a7ce5b9e346d5c3ff22e9f11db820584d02aee12885`

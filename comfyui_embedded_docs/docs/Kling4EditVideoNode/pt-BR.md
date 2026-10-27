# Kling 4.0 Edit Video

Edita um vídeo existente com um prompt de texto usando o modelo Kling 4.0, opcionalmente guiado por vídeos de referência e imagens de referência. O resultado mantém a duração do vídeo de entrada. Use-o para alterar o que acontece em um clipe, mudar seu estilo ou trocar elementos enquanto a sincronização original permanece intacta.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `model` | Seletor de modelo. Apenas `"kling-4.0"` está disponível; selecioná-lo revela as entradas abaixo. | DYNAMIC_COMBO | Sim | `"kling-4.0"` |

### Entradas do kling-4.0

Estas entradas aparecem quando `model` está definido como `"kling-4.0"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `video_1` | O vídeo a ser editado, com duração de 3 a 30 segundos. A saída mantém sua duração. | VIDEO | Sim | 3 a 30 segundos |
| `reference_videos` | Slots expansíveis para vídeos de referência, até 4. Refira-se a eles no prompt como `@Video2` e assim por diante. Cada vídeo e todos os vídeos juntos devem ter de 3 a 30 segundos de duração. | AUTOGROW | Não | 0 a 4 vídeos |
| `reference_images` | Slots expansíveis para imagens de referência, até 10. Refira-se a elas no prompt como `@Image1`, `@Image2` e assim por diante. | AUTOGROW | Não | 0 a 10 imagens |
| `prompt` | Descrição do que alterar e do que manter. Refira-se ao vídeo sendo editado como `@Video1`, aos vídeos de referência como `@Video2` e assim por diante, e às imagens como `@Image1` e assim por diante. | STRING | Sim | 1 a 26000 caracteres |
| `resolution` | Resolução do vídeo de saída. Padrão: `"720p"`. | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Relação de aspecto do vídeo de saída. `"adaptive"` mantém a relação de aspecto do vídeo de entrada. Padrão: `"adaptive"`. | COMBO | Sim | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Restrições e comportamento:**

* O vídeo de entrada e cada vídeo de referência devem ter de 3 a 30 segundos de duração, pelo menos 700x700 e no máximo 4553x4553 pixels, no máximo 8,294,400 pixels no total, com uma relação de aspecto entre 2:5 e 5:2 e uma taxa de quadros de pelo menos 24 fps. Todos os vídeos juntos não devem exceder 30 segundos.
* Cada imagem de referência deve ter pelo menos 300x300 pixels com uma relação de aspecto entre 2:5 e 5:2, e no máximo 10 imagens podem ser conectadas.
* Um prompt que menciona `@VideoN` ou `@ImageN` gera um erro quando menos de N entradas desse tipo estão conectadas.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---------------|-----------|---------------|
| `video` | O vídeo editado, baixado do provedor assim que a tarefa for concluída. Tem a mesma duração do vídeo de entrada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4EditVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `00e8de2529df9be6bc1fae5f2c2beda01f151143448e91b79f9cfb27436064ff`

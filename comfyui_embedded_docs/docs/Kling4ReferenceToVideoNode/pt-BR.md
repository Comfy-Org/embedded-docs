# Kling 4.0 Reference to Video

Gera um vídeo a partir de imagens de referência e vídeos de referência com o modelo Kling 4.0, incluindo áudio. As referências orientam o sujeito, o estilo e o movimento, e um primeiro quadro e um último quadro opcionais fixam o início e o fim do clipe. Use-o para manter um personagem ou uma cena consistentes ao longo de uma tomada enquanto descreve a ação no prompt.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Seletor de modelo. Apenas `"kling-4.0"` está disponível; selecioná-lo revela as entradas abaixo. | DYNAMIC_COMBO | Sim | `"kling-4.0"` |

### Entradas do kling-4.0

Estas entradas aparecem quando `model` é definido como `"kling-4.0"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Espaços expansíveis para imagens de referência, até 10. Refira-se a elas no prompt como `@Image1`, `@Image2` e assim por diante, na ordem de conexão. | AUTOGROW | Não | 0 a 10 imagens |
| `reference_videos` | Espaços expansíveis para vídeos de referência, até 5. Refira-se a eles no prompt como `@Video1`, `@Video2` e assim por diante. Cada vídeo e todos os vídeos juntos devem ter de 3 a 30 segundos de duração. | AUTOGROW | Não | 0 a 5 vídeos |
| `first_frame` | Quadro opcional em que o vídeo começa. Conta para o limite de 10 imagens junto com as imagens de referência. | IMAGE | Não | - |
| `last_frame` | Quadro opcional em que o vídeo termina. Conta para o limite de 10 imagens junto com as imagens de referência. | IMAGE | Não | - |
| `prompt` | Descrição do vídeo a ser gerado. Refira-se às entradas como `@Image1`, `@Image2` e assim por diante, e `@Video1`, `@Video2` e assim por diante. | STRING | Sim | 1 a 26000 caracteres |
| `resolution` | Resolução do vídeo de saída. Padrão: `"720p"`. | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Proporção de aspecto do vídeo de saída. `"adaptive"` segue o prompt, depois o primeiro quadro ou os vídeos de referência e, caso contrário, recorre a 16:9. Padrão: `"adaptive"`. | COMBO | Sim | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Duração do vídeo gerado em segundos. Padrão: 5. | INT | Sim | 3 a 30 |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Restrições e comportamento:**

* As imagens são limitadas a 10 no total, contando as imagens de referência, o primeiro quadro e o último quadro.
* Cada imagem deve ter pelo menos 300x300 pixels, com uma proporção de aspecto entre 2:5 e 5:2.
* Cada vídeo de referência deve ter de 3 a 30 segundos de duração, pelo menos 700x700 e no máximo 4553x4553 pixels, não mais que 8.294.400 pixels no total, com uma proporção de aspecto entre 2:5 e 5:2 e uma taxa de quadros de pelo menos 24 fps. Todos os vídeos de referência juntos não podem exceder 30 segundos.
* Um prompt que menciona `@ImageN` ou `@VideoN` gera um erro quando menos de N entradas desse tipo estão conectadas.
* Quando um primeiro quadro ou um último quadro está conectado, o nó adiciona uma instrução de que o vídeo começa ou termina exatamente nesse quadro.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `video` | O vídeo gerado, baixado do provedor assim que a tarefa for concluída. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ReferenceToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bda2298ed6ed06db04a8f342ec6ad0d5a0494e09bfadee72fce4420ebe4eaf6a`

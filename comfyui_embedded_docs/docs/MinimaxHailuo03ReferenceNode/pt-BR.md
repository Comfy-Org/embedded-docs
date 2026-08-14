# MiniMax H3 Referência para Vídeo

Este nó gera um vídeo usando o modelo MiniMax H3, utilizando imagens, vídeos e áudio de referência para condicionar o resultado. As referências são mencionadas no prompt pela ordem de conexão: "Image 1", "Image 2", "Video 1", "Audio 1" e assim por diante.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado para geração de vídeo (padrão: "MiniMax H3"). A seleção de "MiniMax H3" fornece as configurações de `prompt`, `resolution`, `ratio`, `duration`, `reference_images`, `reference_videos` e `reference_audios` abaixo. | STRING | Sim | "MiniMax H3" |
| `seed` | Semente aleatória. A mesma solicitação com a mesma semente gera resultados semelhantes, porém não garantidamente idênticos (padrão: 42). | INT | Sim | 0 a 4294967295 |
| `watermark` | Se deve adicionar uma marca d'água AIGC ao vídeo (padrão: false). | BOOLEAN | Não | true<br>false |

### Entradas do MiniMax H3

Estas entradas aparecem quando "MiniMax H3" é selecionado como modelo.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. A mídia de referência pode ser referenciada pela ordem, por exemplo "Image 1", "Image 2", "Video 1" ou "Audio 1". | STRING | Sim | Comprimento mínimo: 1 caractere |
| `resolution` | Resolução do vídeo de saída (padrão: "768P"). | STRING | Sim | "768P"<br>"2K" |
| `ratio` | Proporção de aspecto do vídeo de saída (padrão: "adaptive"). | STRING | Sim | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Duração do vídeo de saída em segundos (padrão: 5). | INT | Sim | 4 a 15 |

### Entradas de Referência

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot expansível: conecte de 1 a 9 itens (`image_1`...`image_9`). Imagens de referência de assunto ou estilo, referenciadas no prompt como "Image 1".."Image 9" na ordem de conexão. Até 9 imagens. | IMAGE | Não | 0 a 9 imagens |
| `reference_videos` | Slot expansível: conecte de 1 a 3 itens (`video_1`...`video_3`). Vídeos de referência de movimento ou cena, referenciados no prompt como "Video 1".."Video 3" na ordem de conexão. Até 3 vídeos, com 2 a 15 segundos cada, 15 segundos no total. | VIDEO | Não | 0 a 3 vídeos |
| `reference_audios` | Slot expansível: conecte de 1 a 3 itens (`audio_1`...`audio_3`). Referências de áudio, referenciadas no prompt como "Audio 1".."Audio 3" na ordem de conexão. Até 3 clipes, com 2 a 15 segundos cada, 15 segundos no total. Não pode ser usado sem uma imagem ou vídeo de referência. | AUDIO | Não | 0 a 3 clipes |

### Restrições de Parâmetros

- É necessário pelo menos uma imagem de referência ou um vídeo de referência. Áudio de referência sozinho não é aceito.
- Cada imagem de referência deve ter uma proporção de aspecto entre aproximadamente 0,4 e 2,5 (2:5 a 5:2) e largura e altura mínimas de 256 pixels.
- Cada vídeo de referência deve ter entre 2 e 15 segundos de duração, com uma taxa de quadros entre 23,976 e 60 FPS. A duração total de todos os vídeos de referência não pode exceder 15 segundos.
- Cada clipe de áudio de referência deve ter entre 2 e 15 segundos de duração. A duração total de todos os clipes de áudio de referência não pode exceder 15 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `video` | O vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f7e9c68addda6b48a2366139ecfa28ee57e6cda4aa5cd775c2d769517366573f`

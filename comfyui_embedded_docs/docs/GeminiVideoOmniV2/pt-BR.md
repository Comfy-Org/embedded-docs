# Google Gemini Omni (Vídeo)

O Google Gemini Omni (Video) gera um vídeo com áudio a partir de um prompt de texto usando os modelos Gemini Omni Flash do Google. Você pode, opcionalmente, anexar imagens e/ou vídeos de referência para orientar o resultado ou editar material de vídeo existente. Descreva a duração desejada (3 a 10 segundos) diretamente no prompt.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de vídeo Gemini usado para gerar o vídeo. | DYNAMIC_COMBO | Sim | "Omni Flash 1.1"<br>"Omni Flash" |

### Entradas do Omni Flash 1.1

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descreva o vídeo a ser gerado ou a edição a ser aplicada a um vídeo anexado. Especifique a duração diretamente no prompt, por exemplo, "um clipe de 6 segundos" ou, para a tarefa 'extend', "estender em 5 segundos"; a duração gerada pode ser de 3 a 10 segundos e o padrão é 10. A saída tem áudio. (padrão: "") | STRING | Sim | - |
| `resolution` | Resolução de saída. (padrão: "720p") | COMBO | Sim | "360p"<br>"720p"<br>"1080p"<br>"4k" |
| `aspect_ratio` | Proporção de aspecto de saída: 16:9 (paisagem) ou 9:16 (retrato). As tarefas 'edit' e 'extend' mantêm, em vez disso, a proporção de aspecto do vídeo de entrada. (padrão: "16:9") | COMBO | Sim | "16:9"<br>"9:16" |
| `task_type` | O que fazer com o prompt e a mídia anexada. Com 'auto', o modelo decide. 'text_to_video' gera a partir apenas do prompt e rejeita mídia anexada. 'image_to_video' anima uma imagem ou interpola de um quadro inicial para um quadro final quando duas são anexadas. 'reference_to_video' trata a mídia anexada como referências de assunto. 'edit' reescreve exatamente um vídeo anexado, e 'extend' acrescenta novo conteúdo a ele, de modo que a saída começa com o vídeo de entrada. (padrão: "auto") | COMBO | Sim | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit"<br>"extend" |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 42) | INT | Sim | 0 a 2147483647 |

### Entradas do Omni Flash

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descreva o vídeo a ser gerado ou a edição a ser aplicada a um vídeo anexado. Especifique a duração diretamente no prompt, por exemplo, "um clipe de 6 segundos"; a duração pode ser de 3 a 10 segundos. A saída é 720p, 24 FPS, com áudio. (padrão: "") | STRING | Sim | - |
| `aspect_ratio` | Proporção de aspecto de saída: 16:9 (paisagem) ou 9:16 (retrato). A tarefa 'edit' mantém, em vez disso, a proporção de aspecto do vídeo de entrada. (padrão: "16:9") | COMBO | Sim | "16:9"<br>"9:16" |
| `task_type` | O que fazer com o prompt e a mídia anexada. Com 'auto', o modelo decide. 'text_to_video' gera a partir apenas do prompt e rejeita mídia anexada. 'image_to_video' anima uma imagem ou interpola de um quadro inicial para um quadro final quando duas são anexadas. 'reference_to_video' trata a mídia anexada como referências de assunto. 'edit' reescreve exatamente um vídeo anexado. (padrão: "auto") | COMBO | Sim | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit" |
| `temperature` | Controla a aleatoriedade. Valores mais baixos geram resultados mais focados/determinísticos; valores mais altos, mais variados. (padrão: 1.0) | FLOAT | Sim | 0.0 a 2.0 (step 0.01) |
| `top_p` | Amostragem de núcleo: amostra do menor conjunto de tokens cuja probabilidade acumulada atinja top_p. (padrão: 0.95) | FLOAT | Sim | 0.0 a 1.0 (step 0.01) |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 42) | INT | Sim | 0 a 2147483647 |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | Slot expansível: conecte até 14 imagens (`image_1`...`image_14`). Imagem(ns) de referência opcional(is) para orientar ou animar o vídeo. Na tarefa 'image_to_video', a primeira é o quadro inicial e a segunda, opcional, é o quadro final. | IMAGE | Não | 0 a 14 images |
| `videos` | Slot expansível: conecte até 3 vídeos (`video_1`...`video_3`). Vídeo(s) de referência opcional(is) para orientar ou editar. Cada um com até 10 segundos de duração. | VIDEO | Não | 0 a 3 videos |

**Observações:**
- O `prompt` não pode estar vazio; o nó gera um erro se estiver.
- A tarefa `text_to_video` gera a partir apenas do prompt — anexar imagens ou vídeos gera um erro.
- A tarefa `image_to_video` aceita somente imagens (sem vídeos) e exige exatamente 1 ou 2 imagens: a primeira é o quadro inicial e a segunda, opcional, é o quadro final.
- A tarefa `edit` (ambos os modelos) e a tarefa `extend` (somente Omni Flash 1.1) exigem exatamente um vídeo de entrada e mantêm a proporção de aspecto desse vídeo de entrada, substituindo o valor de `aspect_ratio`.
- No máximo 14 imagens e 3 vídeos podem ser anexados, e cada vídeo anexado deve ter 10 segundos ou menos.
- O Omni Flash sempre gera vídeo em 720p, 24 FPS, com áudio; a seleção de resolução só está disponível com o Omni Flash 1.1.
- Os controles `temperature` e `top_p` estão disponíveis apenas com o modelo Omni Flash; o Omni Flash 1.1 usa configurações de geração fixas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` (primeira saída) | O vídeo gerado com áudio. Para o Omni Flash: 720p, 24 FPS. Para o Omni Flash 1.1: a resolução selecionada na entrada `resolution`. | VIDEO |
| `text` (segunda saída) | O conteúdo de texto gerado pelo modelo junto com o vídeo (pode estar vazio). | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmniV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7a0dda4bcd662c9df3c680297ec9de7886d35e618de8b3ce0cd95b9afd13a892`

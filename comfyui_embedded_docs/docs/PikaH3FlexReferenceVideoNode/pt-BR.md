# Pika H3 Flex Reference to Video

Este nó gera ou edita um vídeo com áudio sincronizado, guiado por imagens, vídeos e clipes de áudio de referência. Pika H3 Flex é o modelo MiniMax H3 pós-treinado da Pika. Conecte referências e mencione-as no prompt como `@Image1`, `@Video1` ou `@Audio1`, na ordem de conexão. É necessário conectar pelo menos uma imagem ou um vídeo de referência, e no máximo 12 referências podem ser conectadas no total.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Até 9 imagens, mencionadas no prompt como `@Image1` a `@Image9` na ordem de conexão. É necessário conectar pelo menos uma imagem ou vídeo. | AUTOGROW | Não | 0 a 9 imagens |
| `reference_videos` | Até 3 clipes, mencionados no prompt como `@Video1` a `@Video3` na ordem de conexão. Cada clipe deve ter de 2 a 15 segundos e os clipes devem totalizar 15 segundos ou menos. Cobrado por segundo. | AUTOGROW | Não | 0 a 3 vídeos |
| `reference_audios` | Até 3 clipes, mencionados no prompt como `@Audio1` a `@Audio3`. Cada clipe deve ter de 2 a 15 segundos e os clipes devem totalizar 15 segundos ou menos. Quando copiados para a saída, os clipes são reproduzidos na ordem de conexão, antes do som dos vídeos conectados. | AUTOGROW | Não | 0 a 3 clipes de áudio |
| `prompt` | O que gerar, ou a edição a ser feita. Mencione as referências como `@Image1`, `@Video1`, `@Audio1`, ou como `<Picture 1>`, `<Video 1>`, `<Audio 1>`. Não deve ficar vazio. Padrão: "" (string vazia). | STRING | Sim | 1 a 8000 caracteres |
| `reference_video_audio` | Copia o som dos vídeos conectados para a saída. Desative para criar uma nova ambiência ou para transferência de movimento com nova música. Um vídeo de uma pessoa falando em close sem diálogo no prompt então recebe uma fala inventada. Padrão: True. | BOOLEAN | Sim | true<br>false |
| `resolution` | Resolução de saída. `"1080p"` e acima são renderizados em 768p e ampliados uma vez. A mesma seed em 480p gera um vídeo diferente. Padrão: `"768p"`. | COMBO | Sim | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `aspect_ratio` | Proporção de tela da saída. `"auto"` segue um vídeo de referência; caso contrário, o prompt. Imagens de referência não afetam isso. Padrão: `"auto"`. | COMBO | Sim | `"auto"`<br>`"21:9"`<br>`"16:9"`<br>`"3:2"`<br>`"4:3"`<br>`"5:4"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"9:21"` |
| `duration` | Duração do clipe em segundos. A duração da saída segue uma grade de frames: 5 segundos geram 124 frames, cerca de 5,17 segundos. Padrão: 5. | INT | Sim | 5 a 15 segundos |
| `rewrite_prompt` | Deixe a Pika expandir o prompt primeiro. A mesma seed então gera um vídeo diferente a cada execução. Padrão: False. | BOOLEAN | Sim | true<br>false |
| `seed` | Seed para amostragem. Com `rewrite_prompt` desativado, a mesma seed repete o vídeo exatamente, embora uma execução local com a mesma seed gere um resultado diferente. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Restrições:**

* É necessário conectar pelo menos uma imagem ou um vídeo de referência.
* No máximo 12 referências podem ser conectadas no total, contando imagens, vídeos e clipes de áudio juntos.
* Cada vídeo de referência e clipe de áudio deve ter de 2 a 15 segundos; os vídeos devem totalizar 15 segundos ou menos, e os clipes de áudio, 15 segundos ou menos.
* O prompt deve ter entre 1 e 8000 caracteres.
* Fazer referência a um slot não conectado, como `@Image3` com duas imagens fornecidas, gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O clipe gerado ou editado com seu áudio sincronizado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaH3FlexReferenceVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c6d8700e3bb0c4ed7663aff55d477314af566568bd6db353fc21d6249ddd93bd`

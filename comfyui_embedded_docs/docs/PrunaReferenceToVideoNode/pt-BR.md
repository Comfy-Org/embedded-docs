# Pruna P-Video-2 Pro Reference to Video

Gere um vídeo a partir de um prompt guiado por imagens, vídeos e áudio de referência com Pruna P-Video-2 Pro Reference to Video. Refira-se a cada referência por número no prompt, e o modelo leva o sujeito, estilo ou movimento dela para o resultado.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo de vídeo Pruna a usar. Selecionar um modelo revela suas entradas abaixo. | DYNAMIC_COMBO | Sim | `"p-video-2-pro-reference"` |

### Entradas do P-Video-2 Pro Reference

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model.images` | Slot expansível para imagens de referência (`image_1`, `image_2`, ...), referenciadas no prompt como `@Image1` até `@Image9` na ordem de conexão. Até 9 imagens, contando o primeiro e o último quadro. | AUTOGROW | Não | 0 a 9 imagens |
| `model.videos` | Slot expansível para vídeos de referência (`video_1`, `video_2`, ...), referenciados como `@Video1` até `@Video3`. Cada um de 2 a 15 segundos a até 60 fps, 15 segundos no total. Vídeos acima de 1080p têm a resolução reduzida. | AUTOGROW | Não | 0 a 3 vídeos |
| `model.audios` | Slot expansível para áudio de referência (`audio_1`, `audio_2`, ...), referenciados como `@Audio1` até `@Audio3`. Até 15 segundos no total. | AUTOGROW | Não | 0 a 3 clipes de áudio |
| `model.prompt` | Descreve o vídeo. Refira-se às referências como `@Image1`, `@Video1` ou `@Audio1` (padrão: vazio). Até 5000 caracteres. | STRING | Sim | 1 a 5000 caracteres |
| `model.first_frame` | Imagem a partir da qual o vídeo começa. Conta para o limite de 9 imagens. | IMAGE | Não | - |
| `model.last_frame` | Imagem em que o vídeo termina. Conta para o limite de 9 imagens. | IMAGE | Não | - |
| `model.keep_audio` | Use o áudio conectado como trilha sonora e gere o vídeo para corresponder a ele (padrão: False). Requer exatamente um áudio: áudios mais curtos são seguidos por som gerado; áudios mais longos são cortados para a duração. | BOOLEAN | Sim | `True`<br>`False` |
| `model.duration` | Duração do vídeo em segundos (padrão: `"5"`). | COMBO | Sim | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"` |
| `model.resolution` | Resolução de saída (padrão: `"768p"`). 1080p, 2k e 4k aumentam a resolução do vídeo gerado em 768p. | COMBO | Sim | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `model.mode` | `"cost"` é mais barato, `"speed"` renderiza mais rápido (padrão: `"speed"`). | COMBO | Sim | `"cost"`<br>`"speed"` |
| `model.aspect_ratio` | Proporção de aspecto do vídeo de saída (padrão: `"16:9"`). `"adaptive"` usa a proporção mais comum entre as referências e, com `enhance_prompt` ativado, o prompt reescrito escolhe a proporção. | COMBO | Sim | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"1:1"` |
| `model.enhance_prompt` | Reescreve o prompt com mais detalhes antes da geração; `"max"` é mais lento (padrão: `"turbo"`). Mantenha ativado quando o prompt se referir a referências por número; um primeiro ou último quadro sempre usa `"turbo"`. Configuração avançada. | COMBO | Sim | `"off"`<br>`"turbo"`<br>`"max"` |
| `model.seed` | Semente para a geração (padrão: 42). A mesma semente reproduz um resultado exatamente apenas quando `model.enhance_prompt` está desativado. | INT | Sim | 0 a 2147483647<br>Passo: 1 |

**Notas:**

- Conecte pelo menos uma imagem de referência, um vídeo, um primeiro quadro ou um último quadro; caso contrário, o nó interrompe com um erro.
- São permitidas 9 imagens, incluindo o primeiro e o último quadro, e 12 referências no total entre imagens, quadros, vídeos e áudio.
- Vídeo de referência e áudio de referência são limitados a 15 segundos no total cada um, e cada vídeo de referência individual deve ter de 2 a 15 segundos a até 60 fps.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `video` | O vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaReferenceToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d6e295b394984c924386ea6432532c7653b4512c646b1f86793be9b98583eef3`

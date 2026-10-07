# Vidu Q4 Reference-to-Video Generation

Gere um vídeo a partir de imagens de referência, áudio de referência opcional e um prompt com um modelo Vidu Q4. Esta é a variante de referência para vídeo dos nós de geração do Vidu Q4.

Selecionar um `model` revela os parâmetros específicos desse modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado para geração de vídeo. Selecionar um modelo revela os parâmetros específicos dele: `reference_images`, `reference_audios`, `prompt`, `aspect_ratio`, `resolution`, `duration`, `audio` e `seed`. | DYNAMIC_COMBO | Sim | `"Vidu Q4 Preview"` |
| `reference_images` | Slot expansível: conecte uma ou mais imagens de referência (`image_1`, `image_2`, ...) para o vídeo gerado; cada imagem de um lote conta para o total. Refira-se a elas no prompt pela ordem: imagem 1, imagem 2 e assim por diante. | IMAGE | Sim | Até 15 imagens |
| `reference_audios` | Slot expansível: conecte referências de voz opcionais (`audio_1`, `audio_2`, `audio_3`), com 3 a 12 segundos cada. Apenas a voz é usada, não as palavras: escreva o diálogo no prompt e atribua uma voz por ordem, por exemplo `image 1 says "Hello!" in the voice from audio 1`. Requer que `audio` esteja habilitado. | AUDIO | Não | Até 3 clipes |
| `prompt` | Uma descrição textual para geração de vídeo, com até 5000 caracteres. Necessária para descrever as referências que você deseja usar. | STRING | Sim | Qualquer texto |
| `aspect_ratio` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"3:4"`<br>`"4:3"` |
| `resolution` | Resolução do vídeo de saída (padrão: `"720p"`). | COMBO | Sim | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` |
| `duration` | Duração do vídeo de saída em segundos (padrão: 5). | INT | Sim | 3 a 16 |
| `audio` | Quando habilitado, produz vídeo com som, incluindo diálogo e efeitos sonoros (padrão: True). | BOOLEAN | Sim | `True`<br>`False` |
| `seed` | A `seed` controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Este parâmetro tem a funcionalidade "controle após gerar" (padrão: 42). | INT | Sim | 1 a 2147483647 |

**Nota:** No máximo 15 imagens de referência podem ser usadas no total, contando cada imagem de um lote. Cada imagem deve ter pelo menos 128x128 pixels com uma proporção de aspecto entre 1:5 e 5:1. O áudio de referência requer que `audio` esteja habilitado e gera um erro caso contrário.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu4ReferenceVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f37ceec93a6140d69332415b8fd748d55e6a608177430975b4b42ab33e593489`

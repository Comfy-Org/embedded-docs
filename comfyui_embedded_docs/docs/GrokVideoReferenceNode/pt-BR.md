# Grok Referência-para-Vídeo

O nó Grok Reference-to-Video gera um vídeo a partir de um prompt de texto, usando até sete imagens de referência para orientar o estilo e o conteúdo da saída. Com o modelo `grok-imagine-video-1.5`, você também pode anexar até três referências de voz predefinidas e fazer referência a imagens e vozes diretamente no prompt usando as tags `@ImageN` e `@AudioN`. O nó envia a solicitação para uma API externa, aguarda a conclusão da geração e baixa o vídeo resultante.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição textual do vídeo desejado. Deve ser uma string não vazia. | STRING | Sim | N/A |
| `modelo` | O modelo a ser usado para a geração de vídeo. | COMBO | Sim | `"grok-imagine-video-1.5"`<br>`"grok-imagine-video"` |
| `semente` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos, independentemente da semente (padrão: 0). | INT | Não | 0 a 2147483647 |

### Entradas do Grok Imagine Video 1.5

Disponível quando `model` está definido como `grok-imagine-video-1.5`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `voice_1` | Referência de voz predefinida opcional; consulte-a no prompt como @Audio1. A API suporta apenas essas vozes predefinidas, não áudio personalizado (padrão: nenhum). | COMBO | Não | Opções de voz predefinidas (inclui `"none"`) |
| `voice_2` | Segunda referência de voz opcional; @Audio2 no prompt (padrão: nenhum). | COMBO | Não | Opções de voz predefinidas (inclui `"none"`) |
| `voice_3` | Terceira referência de voz opcional; @Audio3 no prompt (padrão: nenhum). | COMBO | Não | Opções de voz predefinidas (inclui `"none"`) |
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `aspect_ratio` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | A duração do vídeo de saída em segundos (padrão: 6). | INT | Sim | 1 a 15 |

### Entradas do Grok Imagine Video

Disponível quando `model` está definido como `grok-imagine-video`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `aspect_ratio` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | A duração do vídeo de saída em segundos (padrão: 6). | INT | Sim | 2 a 10 |

### Entradas de Referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot expansível: conecte de 1 a 7 imagens de referência para orientar a geração do vídeo. Com `grok-imagine-video-1.5`, consulte-as no prompt como @Image1 ... @Image7, numeradas na ordem de entrada; uma entrada em lote conta uma vez por imagem. | IMAGE | Sim | 1 a 7 imagens |

**Nota:** Os subparâmetros exibidos dependem do `model` selecionado; `grok-imagine-video-1.5` adiciona as entradas `voice_1`, `voice_2` e `voice_3`. É necessária pelo menos uma imagem de referência e o total é limitado a 7 (uma entrada em lote conta uma vez por imagem). Com `grok-imagine-video-1.5`, o prompt pode fazer referência a imagens conectadas como `@Image1` ... `@Image7` e vozes habilitadas como `@Audio1`, `@Audio2`, `@Audio3`; referenciar uma imagem não conectada ou uma voz definida como `none` causa um erro. A API suporta apenas vozes predefinidas, não áudio personalizado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ac068b34ad7efe786d29f51052a623eaf324041a99b124f6b5f81fadea661a83`

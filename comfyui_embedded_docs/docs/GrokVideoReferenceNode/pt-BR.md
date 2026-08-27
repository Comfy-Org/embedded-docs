# Grok Referência-para-Vídeo

O nó Grok Reference-to-Video gera um vídeo a partir de um prompt de texto, usando até sete imagens de referência para orientar o estilo e o conteúdo da saída. Com o modelo `grok-imagine-video-1.5`, você também pode anexar até três referências de voz predefinidas e fazer referência a imagens e vozes diretamente no prompt usando as tags `@ImageN` e `@AudioN`. O nó envia a solicitação para uma API externa, aguarda a conclusão da geração e baixa o vídeo resultante.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `modelo` | O modelo a ser usado para a geração de vídeo. | DYNAMIC_COMBO | Sim | `"grok-imagine-video-1.5"`<br>`"grok-imagine-video"` |
| `prompt` | Descrição textual do vídeo desejado. Deve ser uma string não vazia. | STRING | Sim | N/A |
| `semente` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Sim | 0 a 2147483647 |

### Entradas do Grok Imagine Video 1.5

Disponível quando `model` está definido como `grok-imagine-video-1.5`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `voice_1` | Referência de voz predefinida opcional; refira-se a ela no prompt como @Audio1. A API suporta apenas essas vozes predefinidas, não áudio personalizado (padrão: nenhuma). | COMBO | Não | Opções de voz predefinidas, incluindo `"none"` |
| `voice_2` | Segunda referência de voz opcional; @Audio2 no prompt (padrão: nenhuma). | COMBO | Não | Opções de voz predefinidas, incluindo `"none"` |
| `voice_3` | Terceira referência de voz opcional; @Audio3 no prompt (padrão: nenhuma). | COMBO | Não | Opções de voz predefinidas, incluindo `"none"` |
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `aspect_ratio` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | A duração do vídeo de saída em segundos (padrão: 6). | INT | Sim | 1 a 15 |

### Entradas do Grok Imagine Video

Disponível quando `model` está definido como `grok-imagine-video`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `aspect_ratio` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | A duração do vídeo de saída em segundos (padrão: 6). | INT | Sim | 2 a 10 |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `reference_images` | Slot expansível: conecte de 1 a 7 imagens de referência para orientar a geração de vídeo. Com `grok-imagine-video-1.5`, refira-se a elas no prompt como @Image1 ... @Image7, numeradas na ordem de entrada; uma entrada em lote conta uma vez por imagem. | IMAGE | Sim | 1 a 7 imagens |

**Observação:** Os subparâmetros exibidos dependem do `model` selecionado; `grok-imagine-video-1.5` adiciona as entradas `voice_1`, `voice_2` e `voice_3`. Pelo menos uma imagem de referência é obrigatória, e o total é limitado a 7 (uma entrada em lote conta uma vez por imagem). Com `grok-imagine-video-1.5`, o prompt pode referenciar imagens conectadas como `@Image1` ... `@Image7` e slots de voz como `@Audio1`, `@Audio2`, `@Audio3`; um `@image` ou `@audio` sem número refere-se ao primeiro. `@AudioN` refere-se ao widget `voice_N`, não à ordem das vozes habilitadas. Referenciar uma imagem que não está conectada ou um slot de voz definido como `none` causa um erro. A API suporta apenas vozes predefinidas, não áudio personalizado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e584c450563eaa7fcb7751d2325f9ef847fa34a4342df01f2bd9ce2e4ff8f2c3`

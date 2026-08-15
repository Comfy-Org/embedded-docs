# Kling 3.0 Vídeo

Este nó gera vídeos usando o modelo Kling V3. Ele suporta o modo texto-para-vídeo, onde um vídeo é criado a partir de uma descrição em texto, e o modo imagem-para-vídeo, onde uma imagem existente é animada. Ele também oferece recursos avançados, como a criação de vídeos com múltiplos segmentos, com prompts individuais para cada parte (storyboards) e a geração opcional de áudio de acompanhamento.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `multi_shot` | Gera uma série de segmentos de vídeo com prompts e durações individuais. Quando definido para uma opção de storyboard, entradas adicionais para o prompt e a duração de cada storyboard aparecem. | COMBO | Sim | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `modelo` | Configurações de modelo e geração. Selecionar um modelo revela seus subparâmetros `model.resolution` e `model.aspect_ratio`. | COMBO | Sim | `"kling-v3"`<br>`"kling-3.0-turbo"` |
| `gerar áudio` | Quando habilitado, o nó gera áudio para o vídeo. Observação: `"kling-3.0-turbo"` sempre gera áudio nativo, portanto esta opção é ignorada para esse modelo. O padrão é True. | BOOLEAN | Sim | True<br>False |
| `seed` | A semente (seed) controla se o nó deve ser reexecutado; os resultados são não determinísticos independentemente da semente. O padrão é 0. | INT | Sim | 0 a 2147483647 |
| `quadro inicial` | Imagem opcional do quadro inicial. Quando conectada, alterna para o modo imagem-para-vídeo. | IMAGE | Não | - |

### Entradas do kling-v3

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `resolução` | A resolução do vídeo gerado. O padrão é `"1080p"`. | COMBO | Sim | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `proporção` | A proporção de aspecto do vídeo gerado. Ignorada no modo imagem-para-vídeo. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Entradas do kling-3.0-turbo

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `resolução` | A resolução do vídeo gerado. O padrão é `"720p"`. | COMBO | Sim | `"1080p"`<br>`"720p"` |
| `proporção` | A proporção de aspecto do vídeo gerado. Ignorada no modo imagem-para-vídeo. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Entradas de multi-shot

**Quando `multi_shot` está definido como `"disabled"`:**

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | A descrição textual principal do vídeo. Deve ter entre 1 e 2500 caracteres. | STRING | Sim | 1 a 2500 caracteres |
| `negative_prompt` | Texto que descreve o que não deve aparecer no vídeo. Pode ser deixado vazio. | STRING | Não | - |
| `duration` | A duração do vídeo em segundos. O padrão é 5. | INT | Sim | 3 a 15 |

**Quando `multi_shot` está definido para uma opção de storyboard (ex.: `"3 storyboards"`):**

Para cada segmento N do storyboard (de 1 até a quantidade selecionada de storyboards), as seguintes entradas aparecem:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `storyboard_N_prompt` | Prompt para o segmento N do storyboard. Máximo de 512 caracteres. | STRING | Sim | 1 a 512 caracteres |
| `storyboard_N_duration` | Duração do segmento N do storyboard em segundos. O padrão é 4. | INT | Sim | 1 a 15 |

**Restrições e comportamento:**

- O modo texto-para-vídeo é usado quando `start_frame` não está conectado; o modo imagem-para-vídeo é usado quando `start_frame` está conectado. No modo imagem-para-vídeo, o parâmetro `model.aspect_ratio` é ignorado e a imagem de entrada deve ter pelo menos 300x300 pixels com uma proporção de aspecto entre 1:2.5 e 2.5:1.
- No modo storyboard, o `prompt` principal e o `negative_prompt` não são usados. A soma total de todas as durações dos storyboards deve estar entre 3 e 15 segundos.
- Para `kling-v3`, cada storyboard é enviado à API como um segmento separado. Para `kling-3.0-turbo`, os prompts e as durações dos storyboards são combinados em um único prompt multi-shot.
- Para `kling-3.0-turbo`, `generate_audio` é ignorado porque este modelo sempre gera áudio nativo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2863d7a971a1978b6009e5321ed2112a9c04809281acd5f65d85ab72c4b49f08`

# ByteDance Seedance 2.0 Primeiro-Último-Frame para Vídeo

Este nó gera um vídeo a partir de uma imagem de primeiro quadro obrigatória e uma imagem de último quadro opcional usando os modelos ByteDance Seedance. Você descreve o vídeo com um prompt de texto; o primeiro quadro guia o início do vídeo e o último quadro guia o fim. Ele suporta Seedance 2.5 e a família Seedance 2.0 (Seedance 2.0, Seedance 2.0 Fast e Seedance 2.0 Mini).

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Seedance 2.5 para o modelo mais recente, vídeos de até 30 segundos e saída mp4/mov; Seedance 2.0 para qualidade máxima e 4k; Fast para otimização de velocidade; Mini para a geração mais rápida e de menor custo. Selecionar um modelo revela entradas específicas do modelo abaixo. | DYNAMIC_COMBO | Sim | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `primeiro_frame` | Imagem do primeiro quadro para o vídeo. | IMAGE | Não | - |
| `último_frame` | Imagem do último quadro para o vídeo. | IMAGE | Não | - |
| `first_frame_asset_id` | Asset_id Seedance para usar como primeiro quadro. Mutuamente exclusivo com a entrada de imagem `first_frame`. O padrão é uma string vazia. | STRING | Não | - |
| `last_frame_asset_id` | Asset_id Seedance para usar como último quadro. Mutuamente exclusivo com a entrada de imagem `last_frame`. O padrão é uma string vazia. | STRING | Não | - |
| `semente` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. O padrão é 0. | INT | Sim | 0 a 2147483647 |
| `marca_d'água` | Se deve adicionar uma marca d'água ao vídeo. O padrão é False. | BOOLEAN | Sim | False<br>True |

### Entradas do Seedance 2.5

Estas entradas aparecem quando `Seedance 2.5` é selecionado.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. Coloque falas entre aspas duplas para direcionar o diálogo gerado. | STRING | Sim | - |
| `resolution` | Resolução do vídeo de saída. O padrão é 720p. | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | Duração do vídeo de saída em segundos (4-30). O padrão é 5. | INT | Sim | 4 a 30 |
| `generate_audio` | Ativar a geração de áudio para o vídeo de saída. O padrão é True. | BOOLEAN | Sim | False<br>True |
| `output_format` | Formato de contêiner do vídeo de saída. O padrão é mp4. | COMBO | Sim | `"mp4"` |

### Entradas do Seedance 2.0

Estas entradas aparecem quando `Seedance 2.0` é selecionado.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. | STRING | Sim | - |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Proporção de aspecto do vídeo de saída. O padrão é `adaptive`, que usa a proporção suportada mais próxima da proporção de aspecto do quadro de entrada. | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos (4-15). O padrão é 7. | INT | Sim | 4 a 15 |
| `generate_audio` | Ativar a geração de áudio para o vídeo de saída. O padrão é True. | BOOLEAN | Sim | False<br>True |

### Entradas do Seedance 2.0 Fast e Seedance 2.0 Mini

Compartilhadas por `Seedance 2.0 Fast` e `Seedance 2.0 Mini`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. | STRING | Sim | - |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `ratio` | Proporção de aspecto do vídeo de saída. O padrão é `adaptive`, que usa a proporção suportada mais próxima da proporção de aspecto do quadro de entrada. | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos (4-15). O padrão é 7. | INT | Sim | 4 a 15 |
| `generate_audio` | Ativar a geração de áudio para o vídeo de saída. O padrão é True. | BOOLEAN | Sim | False<br>True |

**Restrições dos Parâmetros**

- Você deve fornecer o primeiro quadro como uma imagem `first_frame` ou como um `first_frame_asset_id`. Fornecer ambos gera um erro; fornecer nenhum também gera um erro.
- As entradas `last_frame` e `last_frame_asset_id` são opcionais, mas você não pode fornecer ambas para o mesmo quadro.
- Os Asset IDs devem referenciar assets de Imagem Seedance existentes e ativos.
- A entrada `prompt` é obrigatória e não pode estar vazia.
- Com `Seedance 2.5`, a proporção de aspecto da saída é sempre adaptativa e segue a proporção de aspecto do próprio primeiro quadro, portanto nenhuma entrada `ratio` é exibida.
- Com os modelos da família Seedance 2.0 e imagens de quadro locais, as imagens são recortadas do centro e redimensionadas para a resolução e proporção de saída alvo antes da geração. Quando `ratio` é `adaptive`, a proporção suportada mais próxima da imagem de entrada é usada.
- As imagens de quadro locais são validadas quanto à proporção de aspecto e dimensões suportadas; imagens superdimensionadas são reduzidas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bc2eb5f43c935986ad870703cfbc92dd99a53d6f0ac91cf0cad46bee33ff2cc0`

# ByteDance Seedance 2.0 Primeiro-Último-Frame para Vídeo

Este nó gera um vídeo a partir de uma imagem obrigatória de primeiro quadro e uma imagem opcional de último quadro usando os modelos ByteDance Seedance 2.5 ou Seedance 2.0. O primeiro quadro define o início do clipe; o último quadro (quando fornecido) define o final; e um prompt de texto descreve o movimento. O modelo selecionado controla as resoluções, durações e opções de formato de saída disponíveis.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo usado para geração de vídeo. O Seedance 2.5 é o modelo mais recente, com vídeos de até 30 segundos e saída em mp4/mov; o Seedance 2.0 oferece qualidade máxima e 1080p/4k; o Fast é otimizado para velocidade; o Mini é a geração mais rápida e de menor custo. Selecionar um modelo revela as entradas específicas dele abaixo. | DYNAMIC_COMBO | Sim | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `first_frame` | Imagem do primeiro quadro do vídeo. Uma das entradas `first_frame` ou `first_frame_asset_id` é obrigatória. | IMAGE | Não | - |
| `last_frame` | Imagem do último quadro do vídeo. | IMAGE | Não | - |
| `first_frame_asset_id` | asset_id Seedance a ser usado como primeiro quadro. É mutuamente exclusivo com a entrada de imagem `first_frame`. O padrão é uma string vazia. | STRING | Não | - |
| `last_frame_asset_id` | asset_id Seedance a ser usado como último quadro. É mutuamente exclusivo com a entrada de imagem `last_frame`. O padrão é uma string vazia. | STRING | Não | - |
| `seed` | O seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente do seed. O padrão é 0. | INT | Não | 0 a 2147483647 |
| `watermark` | Indica se deve ser adicionada uma marca d'água ao vídeo. O padrão é False. | BOOLEAN | Não | - |

### Entradas do Seedance 2.5

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. Coloque falas entre aspas duplas para direcionar o diálogo gerado. O padrão é uma string vazia. | STRING | Sim | - |
| `resolution` | Resolução do vídeo de saída. O padrão é "720p". | COMBO | Sim | `"480p"`<br>`"720p"` |
| `duration` | Duração do vídeo de saída em segundos (4-30). O padrão é 5. | INT | Sim | 4 a 30 |
| `generate_audio` | Habilita a geração de áudio para o vídeo de saída. O padrão é True. | BOOLEAN | Sim | - |
| `output_format` | Formato de contêiner do vídeo de saída. O padrão é "mp4". | COMBO | Sim | `"mp4"` |

### Entradas do Seedance 2.0

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. O padrão é uma string vazia. | STRING | Sim | - |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Proporção de aspecto do vídeo de saída. O padrão é "adaptive". | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos (4-15). O padrão é 7. | INT | Sim | 4 a 15 |
| `generate_audio` | Habilita a geração de áudio para o vídeo de saída. O padrão é True. | BOOLEAN | Sim | - |

### Entradas compartilhadas por Seedance 2.0 Fast e Seedance 2.0 Mini

Esses dois modelos expõem as mesmas entradas do Seedance 2.0, exceto que apenas as resoluções 480p e 720p estão disponíveis.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. O padrão é uma string vazia. | STRING | Sim | - |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `ratio` | Proporção de aspecto do vídeo de saída. O padrão é "adaptive". | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos (4-15). O padrão é 7. | INT | Sim | 4 a 15 |
| `generate_audio` | Habilita a geração de áudio para o vídeo de saída. O padrão é True. | BOOLEAN | Sim | - |

**Restrições e limitações:**

*   O `prompt` é obrigatório e deve conter pelo menos um caractere que não seja espaço em branco (espaços em branco no início e no final são ignorados).
*   Você deve fornecer exatamente uma fonte de primeiro quadro: ou a imagem `first_frame` ou o `first_frame_asset_id`. Fornecer ambos gera um erro, e não fornecer nenhum também gera um erro.
*   A imagem `last_frame` e o `last_frame_asset_id` são mutuamente exclusivos. Ambos podem ser omitidos.
*   Os IDs de asset devem fazer referência a assets Seedance existentes com o status Ativo. Se um asset não estiver ativo ou não for um asset de imagem, um erro será gerado.
*   Imagens locais devem ter uma proporção de aspecto entre 0,4 e 2,5 (2:5 a 5:2).
*   Para os modelos Seedance 2.0, as imagens locais devem ter pelo menos 300x300 pixels. Elas são redimensionadas automaticamente para as dimensões exatas de saída compatíveis com a resolução e a proporção selecionadas, e a solicitação é enviada com a proporção "adaptive". Quando `ratio` é "adaptive", a proporção de aspecto da saída é derivada da proporção de aspecto do próprio primeiro quadro, ajustada para a proporção compatível mais próxima. Quando IDs de asset são usados em vez de imagens locais, o valor `ratio` selecionado é aplicado diretamente.
*   Para o Seedance 2.5 e para qualquer modelo quando IDs de asset são usados, as imagens são reduzidas automaticamente para um lado máximo de 6000 pixels e devem ter entre 300 e 6000 pixels em cada dimensão.
*   O Seedance 2.5 sempre mantém a proporção de aspecto do próprio primeiro quadro; portanto, nenhuma entrada `ratio` é exibida para este modelo.
*   Os limites de duração variam conforme o modelo: o Seedance 2.5 aceita de 4 a 30 segundos, enquanto o Seedance 2.0, o 2.0 Fast e o 2.0 Mini aceitam de 4 a 15 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d87265eb75d67f7d80f76474fc699f7ca87b6edbddda36733d5e440708b074a2`

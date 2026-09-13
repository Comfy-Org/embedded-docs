# ByteDance Seedance 2.5 Referência para Vídeo (Legado)

Este nó gera, edita ou estende vídeos usando os modelos de IA Seedance 2.5 ou Seedance 2.0 da ByteDance. Você descreve o vídeo em um prompt de texto e pode anexar imagens, vídeos e áudios de referência para orientar o resultado, com suporte a referência multimodal, edição de vídeo e extensão de vídeo. Esta é a versão legada e obsoleta do nó de referência para vídeo do Seedance.

## Entradas

A seleção de um `model` determina quais dos parâmetros abaixo estão disponíveis. `video_editing` e `output_format` aparecem somente quando Seedance 2.5 está selecionado. Os slots de referência expansíveis e as opções de redimensionamento automático de vídeos de referência são compartilhados por todos os modelos e estão descritos em Entradas de referência.

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de IA usado para gerar o vídeo. Seedance 2.5 para o modelo mais recente, vídeos de até 30 segundos e saída mp4/mov; Seedance 2.0 para qualidade máxima e 4k; Fast para otimização de velocidade; Mini para a geração mais rápida e de menor custo. Selecionar um modelo revela as entradas específicas do modelo listadas abaixo. | DYNAMIC_COMBO | Sim | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | A seed controla se o nó deve ser reexecutado; os resultados são não determinísticos independentemente da seed (padrão: 0). | INT | Sim | 0 a 2147483647<br>Passo: 1 |
| `watermark` | Se deve adicionar uma marca d'água ao vídeo (padrão: False). Configuração avançada. | BOOLEAN | Sim | `True`<br>`False` |

### Entradas do Seedance 2.5

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. Coloque falas em aspas duplas para orientar o diálogo gerado. Deve conter pelo menos um caractere que não seja espaço em branco (padrão: vazio). | STRING | Sim | Qualquer texto |
| `resolution` | Resolução do vídeo de saída (padrão: `"720p"`). | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Proporção de aspecto do vídeo de saída (padrão: `"16:9"`). | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos (padrão: 5). | INT | Sim | 4 a 30<br>Passo: 1 |
| `generate_audio` | Habilita a geração de áudio para o vídeo de saída (padrão: True). | BOOLEAN | Sim | `True`<br>`False` |
| `video_editing` | Habilite quando o prompt editar um vídeo de referência conectado, por exemplo, substituindo um objeto nele. A saída então mantém a duração e a proporção de aspecto do clipe de origem, e os widgets `duration` e `ratio` são ignorados. Deixe desabilitado para gerar um novo vídeo ou para estender um vídeo até a duração definida (padrão: False). | BOOLEAN | Sim | `True`<br>`False` |
| `output_format` | Formato de contêiner do vídeo de saída (padrão: `"mp4"`). | COMBO | Sim | `"mp4"` |

### Entradas do Seedance 2.0

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. Deve conter pelo menos um caractere que não seja espaço em branco (padrão: vazio). | STRING | Sim | Qualquer texto |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Proporção de aspecto do vídeo de saída (padrão: `"adaptive"`). | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos (padrão: 7). | INT | Sim | 4 a 15<br>Passo: 1 |
| `generate_audio` | Habilita a geração de áudio para o vídeo de saída (padrão: True). | BOOLEAN | Sim | `True`<br>`False` |

### Entradas do Seedance 2.0 Fast e do Seedance 2.0 Mini

Compartilhado por Seedance 2.0 Fast e Seedance 2.0 Mini. Esses dois modelos expõem o mesmo conjunto de entradas que o Seedance 2.0, exceto que `resolution` é limitado a 480p e 720p.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. Deve conter pelo menos um caractere que não seja espaço em branco (padrão: vazio). | STRING | Sim | Qualquer texto |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `ratio` | Proporção de aspecto do vídeo de saída (padrão: `"adaptive"`). | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos (padrão: 7). | INT | Sim | 4 a 15<br>Passo: 1 |
| `generate_audio` | Habilita a geração de áudio para o vídeo de saída (padrão: True). | BOOLEAN | Sim | `True`<br>`False` |

### Entradas de referência

Disponíveis para todos os modelos. O número máximo de slots depende do modelo selecionado: o Seedance 2.5 suporta mais referências do que os modelos Seedance 2.0.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot expansível: conecte uma ou mais imagens de referência (`image_1`, `image_2`, ...) que orientam a geração do vídeo. As imagens são reduzidas automaticamente para um lado máximo de 6000 pixels e devem ter pelo menos 300x300 pixels, com uma proporção de aspecto entre 0,4 e 2,5. | IMAGE | Não | Até 30 (Seedance 2.5)<br>Até 9 (modelos Seedance 2.0) |
| `reference_videos` | Slot expansível: conecte um ou mais vídeos de referência (`video_1`, `video_2`, ...) que orientam a geração do vídeo; usados para edição e extensão de vídeo. | VIDEO | Não | Até 10 (Seedance 2.5)<br>Até 3 (modelos Seedance 2.0) |
| `reference_audios` | Slot expansível: conecte um ou mais clipes de áudio de referência (`audio_1`, `audio_2`, ...) que orientam a geração do vídeo. | AUDIO | Não | Até 10 (Seedance 2.5)<br>Até 3 (modelos Seedance 2.0) |
| `auto_downscale` | Reduz automaticamente a escala de vídeos de referência que excedem o orçamento de pixels do modelo para a resolução selecionada. A proporção de aspecto é preservada; vídeos que já estão dentro dos limites não são alterados (padrão: True). | BOOLEAN | Não | `True`<br>`False` |
| `auto_upscale` | Configuração avançada. Aumenta automaticamente a escala de vídeos de referência que estão abaixo da contagem mínima de pixels do modelo para a resolução selecionada. A proporção de aspecto é preservada; vídeos que já atendem ao mínimo não são alterados. Observação: aumentar a escala de uma fonte de baixa resolução não adiciona detalhes reais e pode produzir gerações de qualidade inferior (padrão: False). | BOOLEAN | Não | `True`<br>`False` |
| `reference_assets` | Slot expansível: IDs de ativos da biblioteca virtual Seedance criados anteriormente (Image, Video ou Audio) a serem usados como referências (`asset_1`, `asset_2`, ...). Cada ativo deve existir e ter status Active. No prompt, os ativos podem ser referidos como `asset1`, `asset 1`, etc.; o nó substitui esses tokens por rótulos como "Image 2". | STRING | Não | Até 30 (Seedance 2.5)<br>Até 9 (modelos Seedance 2.0) |

**Restrições importantes:**

* Pelo menos uma referência é obrigatória. Para Seedance 2.0, 2.0 Fast e 2.0 Mini, você deve fornecer pelo menos uma imagem ou vídeo de referência (via `reference_images`, `reference_videos` ou uma entrada de imagem ou vídeo em `reference_assets`). O Seedance 2.5 também aceita referências somente de áudio (via `reference_audios` ou uma entrada de áudio em `reference_assets`).
* As contagens de referência dependem do modelo e são validadas considerando entradas diretas e referências de ativos combinadas: o Seedance 2.5 permite até 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios` e 30 `reference_assets`; os modelos Seedance 2.0 permitem até 9 imagens, 3 vídeos, 3 clipes de áudio e 9 ativos.
* Cada vídeo de referência deve ter pelo menos 1,8 segundos, e cada clipe de áudio de referência deve ter pelo menos 1,8 segundos. A duração total de todos os vídeos de referência e de todos os áudios de referência deve permanecer dentro do limite do modelo selecionado (15,1 segundos para os modelos Seedance 2.0).
* Vídeos de referência também devem atender aos limites de contagem de pixels do modelo para a resolução selecionada. Com `auto_downscale` habilitado (padrão), vídeos grandes são redimensionados automaticamente; com `auto_upscale` habilitado, vídeos pequenos são ampliados. Se qualquer ajuste automático estiver desabilitado, vídeos fora do limite correspondente geram um erro.
* Quando `video_editing` está habilitado no Seedance 2.5, as entradas `duration` e `ratio` são ignoradas; a saída corresponde à duração e à proporção de aspecto do próprio vídeo de referência. Se o provedor interpretar o prompt como edição de um vídeo de referência, a geração falhará, a menos que `video_editing` esteja habilitado ou o prompt seja reformulado para descrever um novo vídeo.
* Se o provedor rejeitar a faixa de áudio gerada para o vídeo (por exemplo, uma possível correspondência de direitos autorais), a tarefa falhará; desabilitar `generate_audio` produz um vídeo silencioso.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4a1b62f65ff3515cdb749c9b3916e631e53523fe144e8cdf71ca020825196ae6`

# ByteDance Seedance 2.0 Referência para Vídeo

Este nó gera, edita ou estende vídeos usando os modelos de IA Seedance 2.5 ou 2.0 da ByteDance. Você descreve o vídeo em um prompt de texto e pode adicionar imagens, vídeos e áudios de referência para orientar o resultado. Ele suporta entradas de referência multimodais, edição de vídeo e extensão de vídeo. Esta é a versão legada e obsoleta do nó ByteDance Seedance 2.5 Reference to Video.

## Entradas

Selecionar um `model` determina quais dos parâmetros abaixo estão disponíveis. `video_editing` e `output_format` aparecem apenas quando o Seedance 2.5 está selecionado. Os slots expansíveis de referência e as opções de redimensionamento automático de vídeos de referência são compartilhados por todos os modelos e são descritos em Entradas de referência.

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de IA usado para gerar o vídeo. Seedance 2.5 para o modelo mais novo, vídeos de até 30 segundos e saída em mp4/mov; Seedance 2.0 para qualidade máxima e 1080p/4k; Fast para otimização de velocidade; Mini para a geração mais rápida e de menor custo. Selecionar um modelo revela as entradas específicas do modelo listadas abaixo. | DYNAMIC_COMBO | Sim | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | O `seed` controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente do seed (padrão: 0). | INT | Sim | 0 a 2147483647<br>Passo: 1 |
| `watermark` | Se deve adicionar uma marca-d'água ao vídeo (padrão: False). | BOOLEAN | Sim | `True`<br>`False` |

### Entradas do Seedance 2.5

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para a geração de vídeo. Coloque as falas entre aspas para orientar o diálogo gerado. Deve conter pelo menos um caractere que não seja espaço em branco (padrão: vazio). | STRING | Sim | Qualquer texto |
| `resolution` | Resolução do vídeo de saída (padrão: `"720p"`). | COMBO | Sim | `"480p"`<br>`"720p"` |
| `ratio` | Proporção de aspecto do vídeo de saída (padrão: `"16:9"`). | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos (padrão: 5). | INT | Sim | 4 a 30<br>Passo: 1 |
| `generate_audio` | Ativa a geração de áudio para o vídeo de saída (padrão: True). | BOOLEAN | Sim | `True`<br>`False` |
| `video_editing` | Ative quando o prompt editar um vídeo de referência conectado, por exemplo, substituindo um objeto nele. A saída então mantém a duração e a proporção de aspecto do próprio clipe de origem, e os widgets de duração e proporção são ignorados. Deixe desativado para gerar um novo vídeo ou para estender um para a duração que você definir (padrão: False). | BOOLEAN | Sim | `True`<br>`False` |
| `output_format` | Formato de contêiner do vídeo de saída (padrão: `"mp4"`). | COMBO | Sim | `"mp4"` |

### Entradas do Seedance 2.0

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para a geração de vídeo. Deve conter pelo menos um caractere que não seja espaço em branco (padrão: vazio). | STRING | Sim | Qualquer texto |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Proporção de aspecto do vídeo de saída (padrão: `"adaptive"`). | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos (padrão: 7). | INT | Sim | 4 a 15<br>Passo: 1 |
| `generate_audio` | Ativa a geração de áudio para o vídeo de saída (padrão: True). | BOOLEAN | Sim | `True`<br>`False` |

### Entradas do Seedance 2.0 Fast e Seedance 2.0 Mini

Compartilhadas pelo Seedance 2.0 Fast e Seedance 2.0 Mini. Esses dois modelos expõem o mesmo conjunto de entradas do Seedance 2.0, exceto que `resolution` é limitada a 480p e 720p.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para a geração de vídeo. Deve conter pelo menos um caractere que não seja espaço em branco (padrão: vazio). | STRING | Sim | Qualquer texto |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `ratio` | Proporção de aspecto do vídeo de saída (padrão: `"adaptive"`). | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos (padrão: 7). | INT | Sim | 4 a 15<br>Passo: 1 |
| `generate_audio` | Ativa a geração de áudio para o vídeo de saída (padrão: True). | BOOLEAN | Sim | `True`<br>`False` |

### Entradas de referência

Disponível para todos os modelos. O número máximo de slots depende do modelo selecionado: o Seedance 2.5 suporta mais referências do que os modelos Seedance 2.0.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot expansível: conecte uma ou mais imagens de referência (`image_1`, `image_2`, ...) que orientam a geração de vídeo. O limite de quantidade é por modelo (consulte as seções dos modelos). As imagens são reduzidas automaticamente para um lado máximo de 6000 pixels e devem ter pelo menos 300x300 pixels, com proporção de aspecto entre 0,4 e 2,5. | IMAGE | Não | Até 30 (Seedance 2.5)<br>Até 9 (modelos Seedance 2.0) |
| `reference_videos` | Slot expansível: conecte um ou mais vídeos de referência (`video_1`, `video_2`, ...) que orientam a geração de vídeo; usado para edição e extensão de vídeo. | VIDEO | Não | Até 10 (Seedance 2.5)<br>Até 3 (modelos Seedance 2.0) |
| `reference_audios` | Slot expansível: conecte um ou mais clipes de áudio de referência (`audio_1`, `audio_2`, ...) que orientam a geração de vídeo. | AUDIO | Não | Até 10 (Seedance 2.5)<br>Até 3 (modelos Seedance 2.0) |
| `auto_downscale` | Reduz automaticamente a resolução de vídeos de referência que excedam o limite de pixels do modelo para a resolução selecionada. A proporção de aspecto é preservada; vídeos que já estão dentro dos limites não são alterados (padrão: True). | BOOLEAN | Não | `True`<br>`False` |
| `auto_upscale` | Aumenta automaticamente a resolução de vídeos de referência que estejam abaixo da contagem mínima de pixels do modelo para a resolução selecionada. A proporção de aspecto é preservada; vídeos que já atendem ao mínimo não são alterados. Observação: aumentar a resolução de uma fonte de baixa resolução não adiciona detalhes reais e pode gerar resultados de qualidade inferior (padrão: False). | BOOLEAN | Não | `True`<br>`False` |
| `reference_assets` | Slot expansível: IDs de ativos da biblioteca virtual do Seedance criados anteriormente (Imagem, Vídeo ou Áudio) para usar como referências (`asset_1`, `asset_2`, ...). Cada ativo deve existir e ter status ativo. No prompt, os ativos podem ser referidos como `asset1`, `asset 1`, etc.; o nó substitui esses tokens por rótulos como "Imagem 2". | STRING | Não | Até 30 (Seedance 2.5)<br>Até 9 (modelos Seedance 2.0) |

**Restrições importantes:**

* Pelo menos uma referência é necessária. Para Seedance 2.0, 2.0 Fast e 2.0 Mini, você deve fornecer pelo menos uma referência de imagem ou vídeo (por meio de `reference_images`, `reference_videos` ou uma entrada de imagem ou vídeo em `reference_assets`). O Seedance 2.5 também aceita referências somente de áudio (por meio de `reference_audios` ou uma entrada de áudio em `reference_assets`).
* Os limites de referências dependem do modelo e são validados considerando a combinação de entradas diretas e referências de ativos: o Seedance 2.5 permite até 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios` e 30 `reference_assets`; os modelos Seedance 2.0 permitem até 9 imagens, 3 vídeos, 3 clipes de áudio e 9 ativos.
* Cada vídeo de referência deve ter pelo menos 1,8 segundo de duração, e cada clipe de áudio de referência deve ter pelo menos 1,8 segundo de duração. A duração total de todos os vídeos de referência e de todos os áudios de referência deve permanecer dentro do limite do modelo selecionado (15,1 segundos para os modelos Seedance 2.0).
* Os vídeos de referência também devem atender aos limites de contagem de pixels do modelo para a resolução selecionada. Com `auto_downscale` ativado (padrão), vídeos acima do tamanho são redimensionados automaticamente; com `auto_upscale` ativado, vídeos abaixo do tamanho são ampliados. Se qualquer um dos ajustes automáticos estiver desativado, vídeos fora do limite correspondente geram um erro.
* Quando `video_editing` está ativado no Seedance 2.5, as entradas `duration` e `ratio` são ignoradas; a saída corresponde à duração e à proporção de aspecto do próprio vídeo de referência. Se o provedor interpretar o prompt como uma edição de um vídeo de referência, a geração falhará, a menos que `video_editing` esteja ativado ou que o prompt seja reformulado para descrever um novo vídeo.
* Se o provedor rejeitar a trilha de áudio gerada para o vídeo (por exemplo, uma possível correspondência de direitos autorais), a tarefa falha; desativar `generate_audio` produz um vídeo sem áudio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4a1b62f65ff3515cdb749c9b3916e631e53523fe144e8cdf71ca020825196ae6`

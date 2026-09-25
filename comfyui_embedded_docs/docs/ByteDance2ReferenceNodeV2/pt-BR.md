# ByteDance Seedance 2.5 Referência para Vídeo

O nó ByteDance Seedance 2.5 Reference to Video gera, edita ou estende vídeos usando modelos ByteDance Seedance (Seedance 2.5, 2.5 Draft, 2.0, 2.0 Fast e 2.0 Mini), guiado por um prompt de texto e por imagens, vídeos, áudios ou assets de biblioteca previamente enviados, todos opcionais, como referências. Ele faz upload das referências, envia uma tarefa de geração, aguarda a conclusão e retorna o arquivo de vídeo finalizado. Selecionar `Seedance 2.5 Draft` renderiza uma prévia rápida em 480p; conecte o `draft_task_id` resultante ao nó ByteDance Seedance 2.5 Draft to Final Video para renderizar o resultado final em 1080p.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Seletor de modelo. Seedance 2.5 para o modelo mais recente, vídeos de até 30 segundos e saída mp4/mov; Seedance 2.5 Draft para uma prévia rápida em 480p cuja saída `draft_task_id` renderiza o resultado final em 1080p no nó ByteDance Seedance 2.5 Draft to Final Video; Seedance 2.0 para qualidade máxima e 4k; Fast para otimização de velocidade; Mini para a geração mais rápida e de menor custo. Selecionar um modelo altera os widgets de entrada mostrados abaixo. | DYNAMIC_COMBO | Sim | "Seedance 2.5"<br>"Seedance 2.5 Draft"<br>"Seedance 2.0"<br>"Seedance 2.0 Fast"<br>"Seedance 2.0 Mini" |
| `seed` | A `seed` controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 0. | INT | Sim | 0 a 2147483647 |
| `watermark` | Se deve adicionar uma marca d'água ao vídeo. Padrão: False. Configuração avançada. | BOOLEAN | Sim | true<br>false |

### Entradas do Seedance 2.5

Estas entradas aparecem quando `model` está definido como "Seedance 2.5".

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. Coloque falas entre aspas duplas para orientar o diálogo gerado. Padrão: string vazia. | STRING | Sim | Texto multilinha |
| `resolution` | Resolução do vídeo de saída. Padrão: 720p. | COMBO | Sim | "480p"<br>"720p"<br>"1080p" |
| `ratio` | Proporção de aspecto do vídeo de saída. Padrão: 16:9. | COMBO | Sim | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Duração do vídeo de saída em segundos (4-30). Padrão: 5. | INT | Sim | 4 a 30 |
| `generate_audio` | Habilita a geração de áudio para o vídeo de saída. Padrão: True. | BOOLEAN | Sim | true<br>false |
| `task_type` | O que fazer com a mídia de referência. Todo valor exceto auto é validado quando a tarefa é enviada, portanto configurações incompatíveis falham antes de a geração começar.<br>auto: o modelo infere a tarefa a partir do prompt e das entradas, e configurações que entram em conflito com essa interpretação falham somente depois que a geração começou.<br>reference: gera um novo vídeo guiado pelas imagens, vídeos e áudios de referência.<br>edit: altera um vídeo de referência conectado (adicionar, remover, substituir); a saída mantém a duração e a proporção de aspecto do próprio clipe de origem, e os widgets `duration` e `ratio` são ignorados.<br>extend: continua um vídeo de referência conectado para frente ou para trás; o prompt deve dizer "extend forward", "extend backward" ou "continue"; a proporção de aspecto segue o clipe de origem, e a saída contém apenas o segmento recém-gerado com a duração que você definiu, não o clipe de origem. Padrão: auto. | COMBO | Sim | "auto"<br>"reference"<br>"edit"<br>"extend" |
| `output_format` | Formato de contêiner do vídeo de saída. Padrão: mp4. | COMBO | Sim | "mp4" |

### Entradas do Seedance 2.5 Draft

Estas entradas aparecem quando `model` está definido como "Seedance 2.5 Draft". O conjunto de parâmetros corresponde ao Seedance 2.5 acima, exceto que `resolution` oferece apenas `"480p"` (padrão `"480p"`).

### Entradas do Seedance 2.0

Estas entradas aparecem quando `model` está definido como "Seedance 2.0".

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. Padrão: string vazia. | STRING | Sim | Texto multilinha |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | "480p"<br>"720p"<br>"1080p"<br>"4k" |
| `ratio` | Proporção de aspecto do vídeo de saída. Padrão: adaptive. | COMBO | Sim | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Duração do vídeo de saída em segundos (4-15). Padrão: 7. | INT | Sim | 4 a 15 |
| `generate_audio` | Habilita a geração de áudio para o vídeo de saída. Padrão: True. | BOOLEAN | Sim | true<br>false |

### Entradas do Seedance 2.0 Fast e Seedance 2.0 Mini

Estas entradas aparecem quando `model` está definido como "Seedance 2.0 Fast" ou "Seedance 2.0 Mini". Ambos os modelos compartilham o mesmo conjunto de entradas.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. Padrão: string vazia. | STRING | Sim | Texto multilinha |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | "480p"<br>"720p" |
| `ratio` | Proporção de aspecto do vídeo de saída. Padrão: adaptive. | COMBO | Sim | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Duração do vídeo de saída em segundos (4-15). Padrão: 7. | INT | Sim | 4 a 15 |
| `generate_audio` | Habilita a geração de áudio para o vídeo de saída. Padrão: True. | BOOLEAN | Sim | true<br>false |

### Entradas de referência

Estes slots de referência expansíveis estão disponíveis para todos os modelos. O número máximo de slots varia por modelo: o Seedance 2.5 suporta até 30 imagens, 10 vídeos, 10 áudios e 30 assets; o Seedance 2.0, 2.0 Fast e 2.0 Mini suportam até 9 imagens, 3 vídeos, 3 áudios e 9 assets.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot expansível: conecte 1..N imagens de referência que guiam a saída. O limite de contagem é por modelo (consulte as seções do modelo). As imagens são validadas quanto à proporção de aspecto (0,4 a 2,5) e reduzidas automaticamente para um lado máximo de 6000 pixels. | IMAGE | Não | 1..9 slots (família Seedance 2.0)<br>1..30 slots (Seedance 2.5) |
| `reference_videos` | Slot expansível: conecte 1..N vídeos de referência. O limite de contagem é por modelo (consulte as seções do modelo). Cada vídeo deve ter pelo menos 1,8 segundos de duração e deve respeitar os limites de pixels do modelo e da resolução selecionados. | VIDEO | Não | 1..3 slots (família Seedance 2.0)<br>1..10 slots (Seedance 2.5) |
| `reference_audios` | Slot expansível: conecte 1..N faixas de áudio de referência. O limite de contagem é por modelo (consulte as seções do modelo). Cada áudio deve ter pelo menos 1,8 segundos de duração. | AUDIO | Não | 1..3 slots (família Seedance 2.0)<br>1..10 slots (Seedance 2.5) |
| `reference_assets` | Slot expansível: conecte 1..N strings de ID de asset para mídias já enviadas à biblioteca virtual do Seedance. Cada asset deve estar Active. Você pode se referir a um asset no prompt com tokens como `asset1` ou `asset 1`; o nó os substitui pelo rótulo posicional do asset (por exemplo, "Image 2" ou "Video 1"). | STRING | Não | 1..9 slots (família Seedance 2.0)<br>1..30 slots (Seedance 2.5) |
| `auto_downscale` | Reduz automaticamente a escala de vídeos de referência que excedem o orçamento de pixels do modelo para a resolução selecionada. A proporção de aspecto é preservada; vídeos que já estão dentro dos limites não são alterados. Padrão: True. | BOOLEAN | Não | true<br>false |
| `auto_upscale` | Aumenta automaticamente a escala de vídeos de referência que estão abaixo da contagem mínima de pixels do modelo para a resolução selecionada. A proporção de aspecto é preservada; vídeos que já atendem ao mínimo não são alterados. Observação: aumentar a escala de uma fonte de baixa resolução não adiciona detalhes reais e pode produzir gerações de qualidade inferior. Padrão: False. Configuração avançada. | BOOLEAN | Não | true<br>false |

**Observação:** Pelo menos uma imagem, vídeo ou asset de referência é necessário para executar o nó (o Seedance 2.5 também aceita referências somente de áudio). Vídeos e áudios de referência devem ter pelo menos 1,8 segundos de duração cada, e a duração combinada de todos os vídeos de referência (e, separadamente, de todos os áudios de referência) não deve exceder o total máximo de segundos do modelo selecionado. Imagens de referência devem ter uma proporção de aspecto entre aproximadamente 2:5 e 5:2 (0,4 a 2,5), ter pelo menos 300x300 pixels e são automaticamente reduzidas para um lado máximo de 6000 pixels. As opções "edit" e "extend" de `task_type` estão disponíveis apenas com o Seedance 2.5 e ambas exigem pelo menos um vídeo de referência; quando "edit" é usado, a saída mantém a duração e a proporção de aspecto do próprio clipe de origem, e os widgets `duration` e `ratio` são ignorados; quando "extend" é usado, a saída contém apenas o segmento recém-gerado com a duração que você definiu. Assets referenciados devem estar com status Active, caso contrário a tarefa falha. A saída `draft_task_id` é produzida apenas pelo `Seedance 2.5 Draft`; portanto, com qualquer outro modelo, ela deve ser deixada desconectada, caso contrário a execução falha.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `video` | O vídeo gerado, baixado do provedor quando a tarefa de geração é concluída. Contém áudio quando a geração de áudio está habilitada. | VIDEO |
| `draft_task_id` | ID da tarefa da execução de rascunho. Apenas o modelo Seedance 2.5 Draft o produz; conecte-o ao nó ByteDance Seedance 2.5 Draft to Final Video para renderizar o resultado final em 1080p. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `12fee29b280ff71e29f268f52131d1c15cf3066e0804356b735b61d97c80a6a9`

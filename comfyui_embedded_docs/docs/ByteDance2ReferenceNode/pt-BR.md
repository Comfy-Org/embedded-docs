# ByteDance Seedance 2.0 Referência para Vídeo

Este nó gera, edita ou estende vídeos usando os modelos de IA Seedance 2.5 ou 2.0 da ByteDance. Você descreve o vídeo em um prompt de texto e pode adicionar imagens, vídeos e áudio de referência para orientar o resultado. Ele suporta entradas de referência multimodais, edição de vídeo e extensão de vídeo.

## Entradas

Selecionar um `model` determina quais dos parâmetros abaixo estão disponíveis. `video_editing` e `output_format` aparecem somente quando Seedance 2.5 é selecionado.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de IA usado para gerar o vídeo. Seedance 2.5 é o modelo mais recente, com vídeos de até 30 segundos e saída em mp4/mov; Seedance 2.0 é para máxima qualidade e 1080p/4k; Fast é para otimização de velocidade; Mini é para a geração mais rápida e de menor custo. Selecionar um modelo revela as entradas específicas listadas abaixo. | COMBO | Sim | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `watermark` | Indica se deve adicionar uma marca d'água ao vídeo (padrão: False). | BOOLEAN | Sim | `True`<br>`False` |
| `prompt` | Prompt de texto para geração de vídeo. Para Seedance 2.5, coloque falas entre aspas duplas para direcionar o diálogo gerado. Deve conter pelo menos um caractere que não seja espaço em branco. | STRING | Sim | Qualquer texto |
| `resolution` | Resolução do vídeo de saída. Seedance 2.5, 2.0 Fast e 2.0 Mini oferecem 480p e 720p; Seedance 2.0 também oferece 1080p e 4k (padrão do Seedance 2.5: 720p). | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Proporção de aspecto do vídeo de saída (padrão do Seedance 2.5: `"16:9"`; modelos Seedance 2.0 têm como padrão: `"adaptive"`). | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos (Seedance 2.5: 4-30, padrão 5; modelos Seedance 2.0: 4-15, padrão 7). | INT | Sim | 4 a 30 (Seedance 2.5)<br>4 a 15 (Seedance 2.0)<br>Passo: 1 |
| `generate_audio` | Habilita a geração de áudio para o vídeo de saída (padrão: True). | BOOLEAN | Sim | `True`<br>`False` |
| `video_editing` | Somente Seedance 2.5. Ative quando o prompt editar um vídeo de referência conectado, por exemplo, substituindo um objeto nele. A saída então mantém a duração e a proporção de aspecto do clipe de origem, e os controles de duração e proporção são ignorados. Deixe desativado para gerar um novo vídeo ou para estender um até a duração definida (padrão: False). | BOOLEAN | Sim | `True`<br>`False` |
| `output_format` | Somente Seedance 2.5. Formato de contêiner do vídeo de saída (padrão: `"mp4"`). | COMBO | Sim | `"mp4"` |
| `reference_images` | Imagens de referência que orientam a geração do vídeo. As imagens são reduzidas automaticamente para um lado máximo de 6000 pixels e devem ter pelo menos 300x300 pixels, com proporção de aspecto entre 0,4 e 2,5. | IMAGE | Não | Até 30 (Seedance 2.5)<br>Até 9 (Seedance 2.0) |
| `reference_videos` | Vídeos de referência que orientam a geração do vídeo; usados para edição e extensão de vídeo. | VIDEO | Não | Até 10 (Seedance 2.5)<br>Até 3 (Seedance 2.0) |
| `reference_audios` | Clipes de áudio de referência que orientam a geração do vídeo. | AUDIO | Não | Até 10 (Seedance 2.5)<br>Até 3 (Seedance 2.0) |
| `auto_downscale` | Reduz automaticamente a escala de vídeos de referência que excedem o orçamento de pixels do modelo para a resolução selecionada. A proporção de aspecto é preservada; vídeos que já estão dentro dos limites não são alterados (padrão: True). | BOOLEAN | Não | `True`<br>`False` |
| `auto_upscale` | Aumenta automaticamente a escala de vídeos de referência que estão abaixo do mínimo de pixels do modelo para a resolução selecionada. A proporção de aspecto é preservada; vídeos que já atendem ao mínimo não são alterados. Observação: aumentar a escala de uma fonte de baixa resolução não adiciona detalhes reais e pode gerar resultados de qualidade inferior (padrão: False). | BOOLEAN | Não | `True`<br>`False` |
| `reference_assets` | IDs de ativos da biblioteca virtual do Seedance criados anteriormente (Image, Video ou Audio) para usar como referência. Cada ativo deve existir e ter status ativo. No prompt, os ativos podem ser referidos como asset1, asset 2, etc.; o nó substitui esses tokens por rótulos como Image 2. | STRING | Não | Até 30 (Seedance 2.5)<br>Até 9 (Seedance 2.0) |

**Restrições importantes:**

* Pelo menos uma referência é obrigatória. Para Seedance 2.0, 2.0 Fast e 2.0 Mini, você deve fornecer pelo menos uma imagem ou vídeo de referência (via `reference_images`, `reference_videos` ou uma entrada de `reference_assets` do tipo imagem/vídeo). O Seedance 2.5 também aceita referências somente de áudio.
* As contagens de referência dependem do modelo: Seedance 2.5 permite até 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios` e 30 `reference_assets`; modelos Seedance 2.0 permitem até 9 imagens, 3 vídeos, 3 clipes de áudio e 9 ativos. Os totais são contados somando as entradas diretas e as referências de ativos e são validadas antes da geração.
* Cada vídeo de referência deve ter pelo menos 1,8 segundo de duração, e cada clipe de áudio de referência deve ter pelo menos 1,8 segundo. A duração total de todos os vídeos de referência e de todos os áudios de referência deve permanecer dentro do limite do modelo selecionado (15,1 segundos para os modelos Seedance 2.0).
* Os vídeos de referência também devem atender aos limites de pixels do modelo para a resolução selecionada. Com `auto_downscale` ativado (padrão), vídeos acima do tamanho são redimensionados automaticamente; com `auto_upscale` ativado, vídeos abaixo do tamanho são ampliados. Se qualquer ajuste automático estiver desativado, vídeos fora do limite correspondente geram um erro.
* Quando `video_editing` está ativado no Seedance 2.5, as entradas `duration` e `ratio` são ignoradas; a saída corresponde à duração e à proporção de aspecto do próprio vídeo de referência.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4429306ac40b0f04ce7176cd805b34164de5e4e2b7204b008ea076b57663c200`

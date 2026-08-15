# Kling Omni Quadro Inicial-Final para Vídeo (Pro)

Este nó usa o modelo mais recente da Kling AI para gerar um vídeo a partir de um frame inicial, um frame final opcional ou imagens de referência. Ele pode criar um único vídeo ou um storyboard de múltiplos segmentos com prompts e durações individuais para cada segmento. O nó processa essas entradas para produzir um vídeo com duração e resolução especificadas, com geração opcional de áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_name` | O modelo específico da Kling AI a ser usado para geração de vídeo. | COMBO | Sim | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Um prompt de texto descrevendo o conteúdo do vídeo. Pode incluir descrições positivas e negativas. Ignorado quando storyboards estão habilitados. | STRING | Sim | - |
| `duration` | A duração desejada do vídeo gerado em segundos (padrão: 5). | INT | Sim | 3 a 15 |
| `first_frame` | A imagem inicial para a sequência de vídeo. | IMAGE | Sim | - |
| `end_frame` | Um frame final opcional para o vídeo. Não pode ser usado simultaneamente com `reference_images`. Não funciona com storyboards. | IMAGE | Não | - |
| `reference_images` | Até 6 imagens de referência adicionais. | IMAGE | Não | - |
| `resolution` | A resolução de saída para o vídeo gerado (padrão: "1080p"). | COMBO | Não | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Gera uma série de segmentos de vídeo com prompts e durações individuais. Compatível apenas com `kling-v3-omni`. Quando habilitado, cada storyboard exige um prompt e uma duração. | DYNAMIC_COMBO | Não | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `gerar_áudio` | Gera áudio para o vídeo (padrão: False). Compatível apenas com `kling-v3-omni`. | BOOLEAN | Não | True / False |
| `semente` | A `seed` controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da `seed` (padrão: 0). | INT | Não | 0 a 2147483647 |

### Entradas de Storyboard

Quando `storyboards` está definido com um valor diferente de `"disabled"`, as seguintes entradas são adicionadas para cada segmento selecionado (N varia de 1 até o número selecionado de storyboards):

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `storyboard_N_prompt` | Prompt para o segmento N do storyboard. Máximo de 512 caracteres. (padrão: "") | STRING | Sim | - |
| `storyboard_N_duration` | Duração do segmento N do storyboard em segundos (padrão: 4). | INT | Sim | 1 a 15 |

**Restrições importantes:**

* A entrada `end_frame` não pode ser usada ao mesmo tempo que a entrada `reference_images`.
* A entrada `end_frame` não pode ser usada simultaneamente com storyboards.
* O modelo `kling-video-o1` não suporta durações superiores a 10 segundos, geração de áudio, resolução 4k ou storyboards.
* Se você não fornecer `end_frame` nem `reference_images` com o modelo `kling-video-o1`, o `duration` só pode ser definido como 5 ou 10 segundos.
* Todas as imagens de entrada (`first_frame`, `end_frame` e `reference_images`, se houver) devem ter uma dimensão mínima de 300 pixels tanto na largura quanto na altura.
* A proporção de aspecto de todas as imagens de entrada deve estar entre 1:2.5 e 2.5:1.
* No máximo 6 imagens podem ser fornecidas por meio da entrada `reference_images`.
* O texto do `prompt` deve ter entre 1 e 2500 caracteres (0 caracteres são permitidos quando storyboards estão habilitados).
* O prompt pode fazer referência às imagens de entrada usando os placeholders `@image`, `@image1`, `@image2`, etc.; eles são convertidos automaticamente para o formato de referência de imagem compatível com a API.
* Quando storyboards estão habilitados, a duração total de todos os segmentos de storyboard deve ser igual ao valor global de `duration`.
* Cada prompt de storyboard deve ter entre 1 e 512 caracteres.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2b26914ba29c3d877a981e41acb44d15dfacc604d86d7cc232ebfa7fda0ae3b8`

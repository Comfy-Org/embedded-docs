# SyncTalkingImageNode

Anime um retrato estático em um vídeo falante guiado por áudio de fala, usando o modelo sync-3 da sync.so. A duração da saída corresponde à duração do áudio, e o custo é proporcional à duração da saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `image` | Uma única imagem com um rosto claramente visível, de até 4K (4096x2160). | IMAGE | Sim | Exatamente uma imagem necessária |
| `audio` | Áudio de fala que guia o vídeo falante; a duração da saída corresponde a ele. Conecte qualquer nó TTS aqui para gerar a animação a partir de texto. | AUDIO | Sim | Duração máxima: 600 segundos |
| `prompt` | Orientação opcional sobre como o retrato ganha vida, ex.: 'faça o sujeito sorrir e olhar para a câmera'. Deixe vazio para movimento natural de fala. (padrão: "") | STRING | Não | Texto multilinha |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Não | 0 a 2147483647 |
| `model` | Modelo de geração sync.so. A entrada de imagem é exclusiva do sync-3. | COMBO | Sim | `"sync-3"` |
| `speaker_selection` | Qual rosto animar quando várias pessoas estão visíveis. `default`: deixar o modelo decidir. `coordinates`: direcionar o rosto no pixel (speaker_x, speaker_y) na imagem. A detecção automática não é suportada para imagens. (padrão: "default") | COMBO | Não | `"default"`<br>`"coordinates"` |
| `speaker_x` | Coordenada X do pixel do rosto do falante. Usado apenas quando speaker_selection é 'coordinates'. (padrão: 0) | INT | Não | 0 a 4096 |
| `speaker_y` | Coordenada Y do pixel do rosto do falante. Usado apenas quando speaker_selection é 'coordinates'. (padrão: 0) | INT | Não | 0 a 4096 |
| `auto_downscale` | Redimensionar automaticamente a imagem se ela exceder o limite de entrada de 4K (4096x2160); as coordenadas do falante são escaladas para corresponder. Quando desabilitado, uma imagem muito grande gera um erro. (padrão: True) | BOOLEAN | Não | True<br>False |

**Nota:** Os parâmetros `speaker_x` e `speaker_y` são usados apenas quando `speaker_selection` está definido como `"coordinates"`. Quando `auto_downscale` está habilitado, as coordenadas do falante são automaticamente escaladas para corresponder às dimensões da imagem redimensionada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|---------------|
| `video` | O vídeo falante gerado com o retrato animado sincronizado com o áudio de entrada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SyncTalkingImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `21f722cdcc5ff017949887ed2252854feebb9b913034dc6a6c3ce196ad089468`

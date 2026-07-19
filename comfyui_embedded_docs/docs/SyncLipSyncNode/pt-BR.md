# SyncLipSyncNode

Este nó ressincroniza o movimento da boca em um vídeo com um novo áudio de fala usando a API sync.so. Ele lida automaticamente com closes, perfis e obstruções, preservando a expressão do falante. O custo é dimensionado de acordo com a duração da saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `video` | Gravação do falante a ser ressincronizada. Até 4K (4096x2160); uma taxa de quadros constante de 24/25/30 fps funciona melhor. | VIDEO | Sim | - |
| `audio` | Áudio de fala para sincronizar a boca. | AUDIO | Sim | - |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 42). | INT | Sim | 0 a 2147483647 |
| `model` | Modelo de geração sync.so. | COMBO | Sim | Veja abaixo |

O parâmetro `model` é uma combinação dinâmica que inclui os seguintes subparâmetros:

| Subparâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|---------------|-------------|-----------|----------|-------|
| `sync_mode` | Como lidar com uma incompatibilidade de duração entre vídeo e áudio; isso também define o comprimento da saída (padrão: "bounce"). | COMBO | Sim | `"bounce"`<br>`"cut_off"`<br>`"loop"`<br>`"silence"`<br>`"remap"` |
| `speaker_selection` | Qual rosto sincronizar quando várias pessoas estão visíveis (padrão: "default"). | COMBO | Sim | `"default"`<br>`"auto-detect"`<br>`"coordinates"` |
| `speaker_frame` | Quadro de vídeo usado para localizar o falante. Usado apenas quando `speaker_selection` é "coordinates" (padrão: 0). | INT | Não | 0 a 1000000 |
| `speaker_x` | Coordenada X em pixels do rosto do falante. Usado apenas quando `speaker_selection` é "coordinates" (padrão: 0). | INT | Não | 0 a 4096 |
| `speaker_y` | Coordenada Y em pixels do rosto do falante. Usado apenas quando `speaker_selection` é "coordinates" (padrão: 0). | INT | Não | 0 a 4096 |

**Opções do modo de sincronização:**
- `bounce`: O vídeo é reproduzido para frente e depois para trás até o áudio terminar (saída = duração do áudio)
- `loop`: O vídeo reinicia até o áudio terminar (saída = duração do áudio)
- `remap`: O vídeo é esticado no tempo para corresponder ao áudio (saída = duração do áudio)
- `cut_off`: A faixa mais longa é cortada (saída = duração mais curta)
- `silence`: Nada é cortado; a faixa mais curta é preenchida (saída = duração mais longa)

**Opções de seleção do falante:**
- `default`: Deixe o modelo decidir qual rosto sincronizar
- `auto-detect`: Detecta e segue o falante ativo
- `coordinates`: Segmenta o rosto nos pixels (`speaker_x`, `speaker_y`) no quadro escolhido por `speaker_frame`

**Restrições:**
- A resolução do vídeo não deve exceder 4K (4096x2160). Vídeos acima deste limite gerarão um erro.
- A duração do áudio não deve exceder 600 segundos (10 minutos).
- Os parâmetros `speaker_frame`, `speaker_x` e `speaker_y` são usados apenas quando `speaker_selection` está definido como "coordinates".

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `video` | O vídeo ressincronizado com o movimento da boca correspondente ao áudio fornecido. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SyncLipSyncNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b41f8c9bf0d55059f081a66af20636ec96462c3fd9caeb685cab10278f84678a`

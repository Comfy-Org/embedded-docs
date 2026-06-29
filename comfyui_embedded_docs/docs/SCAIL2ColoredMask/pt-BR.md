# SCAIL2ColoredMask

Este nó renderiza dados de rastreamento do SAM3 em máscaras coloridas que são consumidas pelo nó WanSCAILToVideo. Ele processa dados de rastreamento de um vídeo de pose condutor e opcionalmente uma imagem de referência, atribuindo cores consistentes a cada pessoa rastreada em ambas as saídas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `dados_de_rastreamento_driving` | Rastreamento SAM3 do vídeo de pose condutor. Será renderizado na saída pose_video_mask. | SAM3_TRACK_DATA | Sim | - |
| `dados_de_rastreamento_referência` | Rastreamento SAM3 da imagem de referência. | SAM3_TRACK_DATA | Não | - |
| `índices_de_objetos` | Lista separada por vírgulas de índices de pessoas a incluir (ex.: '0,2,3'). Aplicado tanto às máscaras de referência quanto às do vídeo de pose. Vazio = todas. | STRING | Sim | - |
| `ordenar_por` | Ordem na qual as cores da paleta são atribuídas aos objetos rastreados (aplicado tanto à referência quanto ao vídeo de pose para que cada identidade mantenha a mesma cor). left_to_right = objeto mais à esquerda (pelo centróide do primeiro quadro) recebe a primeira cor; area = objeto maior (pela área da máscara do primeiro quadro) recebe a primeira cor; none = manter a ordem do SAM3. (padrão: "left_to_right") | COMBO | Sim | `"none"`<br>`"left_to_right"`<br>`"area"` |
| `modo_de_substituição` | Falso = Modo Animação (pose_video_mask tem fundo preto, reference_image_mask tem fundo branco). Verdadeiro = Modo Substituição (pose_video_mask tem fundo branco, reference_image_mask tem fundo preto). (padrão: Falso) | BOOLEAN | Sim | Falso<br>Verdadeiro |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `pose_video_mask` | Máscara colorida renderizada a partir dos dados de rastreamento do vídeo de pose condutor. A cor de fundo segue a configuração de replacement_mode. | IMAGE |
| `reference_image_mask` | Máscara colorida renderizada a partir dos dados de rastreamento da imagem de referência. Sempre renderizada com fundo preto conforme convenção do modelo. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SCAIL2ColoredMask/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c9f6d87410b8bd4082ffb06ef1cf973829566ed222be643db3528cbc241d3c14`

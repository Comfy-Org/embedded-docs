# Criar Máscara Colorida SCAIL-2

Este nó renderiza dados de rastreamento SAM3 em máscaras coloridas que são consumidas pelo nó WanSCAILToVideo. Ele processa dados de rastreamento de um vídeo de pose de condução e, opcionalmente, de uma imagem de referência, atribuindo cores consistentes a cada pessoa rastreada em ambas as saídas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `driving_track_data` | Rastreamento SAM3 do vídeo de pose de condução. Será renderizado na saída pose_video_mask. | SAM3_TRACK_DATA | Sim | - |
| `ref_track_data` | Rastreamento SAM3 da(s) imagem(ns) de referência (uma identidade por objeto, colorida na ordem do lote), ou uma MASK simples do sujeito de referência (renderizada como uma única identidade). | SAM3_TRACK_DATA ou MASK | Não | - |
| `object_indices` | Lista separada por vírgulas de índices de pessoas a incluir (ex.: '0,2,3'). Aplicada tanto às máscaras de referência quanto às do vídeo de pose. Vazio = todos. (padrão: "") | STRING | Sim | - |
| `sort_by` | Ordem na qual as cores da paleta são atribuídas aos objetos rastreados (aplicada tanto à referência quanto ao vídeo de pose para que cada identidade mantenha a mesma cor). Objetos que aparecem em quadros anteriores sempre vêm primeiro; dentro de um quadro, left_to_right = o objeto mais à esquerda (pelo centroide na primeira aparição) recebe a primeira cor, area = o maior objeto (pela área da máscara na primeira aparição) recebe a primeira cor; none = mantém a ordem do SAM3. (padrão: "left_to_right") | COMBO | Sim | `"none"`<br>`"left_to_right"`<br>`"area"` |
| `replacement_mode` | False = Modo de Animação (pose_video_mask tem fundo preto, reference_image_mask tem fundo branco). True = Modo de Substituição (pose_video_mask tem fundo branco, reference_image_mask tem fundo preto). (padrão: False) | BOOLEAN | Sim | False<br>True |

Nota: `object_indices` aceita apenas dígitos separados por vírgulas; entradas não numéricas e índices fora do intervalo são ignorados. Quando `ref_track_data` não é fornecido, a saída `reference_image_mask` é um preenchimento sólido usando a cor de fundo de referência (branco no Modo de Animação, preto no Modo de Substituição).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `pose_video_mask` | Máscara colorida renderizada a partir dos dados de rastreamento do vídeo de pose de condução. A cor de fundo segue a configuração replacement_mode. | IMAGE |
| `reference_image_mask` | Máscara colorida renderizada a partir dos dados de rastreamento da imagem de referência. O fundo é preto no Modo de Substituição e branco no Modo de Animação. Se nenhum dado de referência for fornecido, retorna um preenchimento sólido correspondente à cor de fundo de referência. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SCAIL2ColoredMask/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ce0669ad0ed3c76cc18ef0ee7b620f5aa6eaa1e5b96c189941c0a5b744c3351f`

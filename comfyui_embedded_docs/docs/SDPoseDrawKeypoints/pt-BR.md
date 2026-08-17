# SDPoseDrawKeypoints

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `keypoints` | Os dados de pontos-chave da pose a serem desenhados. Esses dados normalmente vêm de um nó de detecção de pose. | POSE_KEYPOINT | Sim | - |
| `draw_body` | Controla se o esqueleto principal do corpo é desenhado (padrão: True). | BOOLEAN | Não | - |
| `draw_hands` | Controla se os pontos-chave das mãos são desenhados (padrão: True). | BOOLEAN | Não | - |
| `draw_face` | Controla se os pontos-chave do rosto são desenhados (padrão: True). | BOOLEAN | Não | - |
| `draw_feet` | Controla se os pontos-chave dos pés são desenhados (padrão: False). | BOOLEAN | Não | - |
| `stick_width` | A largura das linhas usadas para desenhar o esqueleto do corpo (padrão: 4). | INT | Não | 1 a 10 |
| `face_point_size` | O tamanho dos pontos usados para desenhar os pontos-chave do rosto (padrão: 3). | INT | Não | 1 a 10 |
| `score_threshold` | A pontuação de confiança mínima que um ponto-chave deve ter para ser desenhado. Pontos-chave com pontuações abaixo desse valor são ignorados (padrão: 0.3). | FLOAT | Não | 0.0 a 1.0 |
| `draw_head` | Controla se os pontos-chave da cabeça (nariz, olhos, orelhas) e as conexões da cabeça são desenhados (padrão: True). | BOOLEAN | Não | - |

**Nota:** Se a entrada `keypoints` estiver vazia ou for `None`, o nó produzirá uma imagem em branco de 64x64.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | Uma imagem com os pontos-chave da pose desenhados. As dimensões da imagem correspondem aos valores de `canvas_height` e `canvas_width` especificados nos dados de pontos-chave de entrada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2b2b9530b55c56e278666bd5d139bb6a1bb503b75b948a89266b9982b5a295e4`

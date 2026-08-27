# SDPoseDrawKeypoints

O nó SDPoseDrawKeypoints recebe dados de estimativa de pose (keypoints) e os desenha como um esqueleto visual em uma tela em branco. Ele permite desenhar seletivamente diferentes partes da pose, como corpo, cabeça, mãos, rosto e pés, com larguras de linha e tamanhos de ponto personalizáveis. A imagem resultante pode ser usada para visualização ou como entrada para outros nós que exigem uma imagem de pose.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `pontos-chave` | Os dados de keypoints da pose a serem desenhados. Esses dados geralmente vêm de um nó de detecção de pose e podem conter um ou mais quadros. | POSE_KEYPOINT | Sim | - |
| `desenhar_corpo` | Controla se o esqueleto principal do corpo é desenhado (padrão: True). | BOOLEAN | Não | - |
| `desenhar_mãos` | Controla se os keypoints das mãos são desenhados (padrão: True). | BOOLEAN | Não | - |
| `desenhar_rosto` | Controla se os keypoints do rosto são desenhados (padrão: True). | BOOLEAN | Não | - |
| `desenhar_pés` | Controla se os keypoints dos pés são desenhados (padrão: False). | BOOLEAN | Não | - |
| `largura_da_linha` | A largura das linhas usadas para desenhar o esqueleto do corpo e da cabeça (padrão: 4). | INT | Não | 1 a 10 |
| `tamanho_do_ponto_do_rosto` | O tamanho dos pontos usados para desenhar os keypoints do rosto (padrão: 3). | INT | Não | 1 a 10 |
| `limite_de_pontuação` | A pontuação de confiança mínima que um keypoint deve ter para ser desenhado. Keypoints com pontuações abaixo desse valor são ignorados (padrão: 0.3). | FLOAT | Não | 0.0 a 1.0 |
| `desenhar_cabeça` | Controla se os keypoints da cabeça (nariz, olhos, orelhas) são desenhados (padrão: True). | BOOLEAN | Não | - |

**Nota:** Se a entrada `keypoints` estiver vazia ou for `None`, o nó gerará uma imagem em branco de 64x64.

**Nota:** `draw_body` e `draw_head` funcionam de forma independente. Quando `draw_head` está desabilitado, os keypoints da cabeça não são desenhados mesmo se `draw_body` estiver habilitado. Quando `draw_body` está desabilitado, mas `draw_head` está habilitado, apenas os keypoints da cabeça e o ponto do pescoço são desenhados. Se ambos estiverem desabilitados, nenhum keypoint do corpo ou da cabeça é desenhado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | Uma imagem com os keypoints de pose desenhados. As dimensões da imagem correspondem aos valores de `canvas_height` e `canvas_width` especificados nos dados de keypoints de entrada. Quando a entrada contém múltiplos quadros, um lote de imagens é retornado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2b2b9530b55c56e278666bd5d139bb6a1bb503b75b948a89266b9982b5a295e4`

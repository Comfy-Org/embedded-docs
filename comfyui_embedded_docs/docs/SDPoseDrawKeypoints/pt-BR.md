O nó SDPoseDrawKeypoints recebe dados de estimativa de pose (pontos-chave) e os desenha como um esqueleto visual em uma tela em branco. Ele permite desenhar seletivamente diferentes partes da pose, como corpo, mãos, rosto e pés, com larguras de linha e tamanhos de ponto personalizáveis. A imagem resultante pode ser usada para visualização ou como entrada para outros nós que necessitam de uma imagem de pose.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `pontos-chave` | Os dados de pontos-chave da pose a serem desenhados. Esses dados geralmente vêm de um nó de detecção de pose. | POSE_KEYPOINT | Sim | - |
| `desenhar_corpo` | Controla se o esqueleto principal do corpo é desenhado (padrão: True). | BOOLEAN | Não | - |
| `desenhar_mãos` | Controla se os pontos-chave das mãos são desenhados (padrão: True). | BOOLEAN | Não | - |
| `desenhar_rosto` | Controla se os pontos-chave do rosto são desenhados (padrão: True). | BOOLEAN | Não | - |
| `desenhar_pés` | Controla se os pontos-chave dos pés são desenhados (padrão: False). | BOOLEAN | Não | - |
| `largura_da_linha` | A largura das linhas usadas para desenhar o esqueleto do corpo (padrão: 4). | INT | Não | 1 a 10 |
| `tamanho_do_ponto_do_rosto` | O tamanho dos pontos usados para desenhar os pontos-chave do rosto (padrão: 3). | INT | Não | 1 a 10 |
| `limite_de_pontuação` | A pontuação mínima de confiança que um ponto-chave deve ter para ser desenhado. Pontos-chave com pontuações abaixo deste valor são ignorados (padrão: 0.3). | FLOAT | Não | 0.0 a 1.0 |

**Observação:** Se a entrada `keypoints` estiver vazia ou for `None`, o nó produzirá uma imagem em branco de 64x64.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | Uma imagem com os pontos-chave da pose desenhados. As dimensões da imagem correspondem à `canvas_height` e `canvas_width` especificadas nos dados de pontos-chave de entrada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c01397ed3608b65b737b60c2ae50919e0217cfe63b3695b68f176c2d69faa9c1`

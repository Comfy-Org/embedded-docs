# SDPoseFaceBBoxes

O nó SDPoseFaceBBoxes processa dados de pontos-chave de pose para detectar e gerar caixas delimitadoras ao redor de rostos humanos. Ele analisa os pontos-chave faciais 2D de cada pessoa em um quadro, calcula uma caixa delimitadora com base nesses pontos e pode ajustar o tamanho e formato da caixa. As caixas delimitadoras resultantes são formatadas para serem compatíveis com outros nós no fluxo de trabalho SDPose, como o SDPoseKeypointExtractor.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `pontos-chave` | Os dados de pontos-chave de pose contendo informações sobre pessoas detectadas e seus marcos corporais/faciais por quadro. | POSE_KEYPOINT | Sim | - |
| `escala` | Multiplicador para a área da caixa delimitadora ao redor de cada rosto detectado. Um valor maior cria uma caixa maior. (padrão: 1,5) | FLOAT | Não | 1,0 - 10,0 |
| `forçar_quadrado` | Expande o eixo mais curto da caixa delimitadora para que a região de recorte seja sempre quadrada. (padrão: Verdadeiro) | BOOLEAN | Não | - |

**Observação:** A entrada `keypoints` deve estar no formato específico produzido por nós como SDPoseKeypointExtractor, contendo `canvas_height`, `canvas_width` e dados de `people` com `face_keypoints_2d` para cada pessoa.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `bboxes` | Uma lista de caixas delimitadoras faciais para cada quadro. Cada caixa delimitadora é definida por suas coordenadas do canto superior esquerdo (`x`, `y`), `width` e `height`. Esta saída é compatível com a entrada `bboxes` do nó SDPoseKeypointExtractor. | BOUNDINGBOX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseFaceBBoxes/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bffbcddb882f6743a6cace6a4884fa5a257b746897c79ba9260c15260fab874e`

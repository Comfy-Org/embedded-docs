> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseFaceBBoxes/pt-BR.md)

O nó SDPoseFaceBBoxes processa dados de pontos-chave de pose para detectar e gerar caixas delimitadoras ao redor de rostos humanos. Ele analisa os pontos-chave 2D do rosto para cada pessoa em um quadro, calcula uma caixa delimitadora com base nesses pontos e pode ajustar o tamanho e a forma da caixa. As caixas delimitadoras resultantes são formatadas para serem compatíveis com outros nós no fluxo de trabalho SDPose, como o SDPoseKeypointExtractor.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `keypoints` | POSE_KEYPOINT | Sim | - | Os dados de pontos-chave de pose contendo informações sobre pessoas detectadas e seus marcos corporais/faciais por quadro. |
| `scale` | FLOAT | Não | 1.0 - 10.0 | Multiplicador para a área da caixa delimitadora ao redor de cada rosto detectado. Um valor maior cria uma caixa maior. (padrão: 1.5) |
| `force_square` | BOOLEAN | Não | - | Expande o eixo mais curto da caixa delimitadora para que a região de corte seja sempre quadrada. (padrão: Verdadeiro) |

**Nota:** A entrada `keypoints` deve estar no formato específico produzido por nós como SDPoseKeypointExtractor, contendo dados de `canvas_height`, `canvas_width` e `people` com `face_keypoints_2d` para cada pessoa.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `bboxes` | BOUNDINGBOX | Uma lista de caixas delimitadoras de rosto para cada quadro. Cada caixa delimitadora é definida por suas coordenadas do canto superior esquerdo (`x`, `y`), `width` e `height`. Esta saída é compatível com a entrada `bboxes` do nó SDPoseKeypointExtractor. |
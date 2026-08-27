# Pixal3DConditioning

Este nó prepara o condicionamento de imagem para o pipeline de geração 3D Trellis2. Ele extrai características visuais da imagem de entrada com um modelo de visão DINOv3 em duas resoluções, organiza-as em mapas de características por estágio (opcionalmente aprimorados com um modelo NAF) e combina-os com dados de câmera derivados do campo de visão horizontal. Ele gera um par de condicionamentos positivo e negativo, onde o negativo usa características zeradas para orientação livre de classificador.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision. | CLIP_VISION | Sim | — |
| `imagem` | Imagem pré-processada de ImageCropToMask (pad_factor=1.1 para Pixal3D). | IMAGE | Sim | — |
| `camera_angle_x` | FOV horizontal em graus (nome de exibição: fov). Conecte um MoGeGeometryToFOV (axis='horizontal', unit='degrees') para um FoV por imagem (corresponde ao padrão original). Padrão: 49.13. | FLOAT | Sim | 1.0 – 170.0 |

Nota: O valor de `camera_angle_x` é convertido para radianos internamente e usado para calcular a distância da câmera para a matriz de transformação de projeção. Quando o modelo de visão fornecido inclui um componente NAF, o nó também produz mapas de características de alta resolução para as etapas de forma e textura.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positivo` | Condicionamento positivo contendo os mapas de características derivados da imagem e os dados de projeção para a geração Trellis2. | CONDITIONING |
| `negativo` | Condicionamento negativo com tensores de características zerados, usado para orientação livre de classificador. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3eba711620f6c56a21bbf7df89f8d406ce6f90908298b1a295a1dbbddd042472`

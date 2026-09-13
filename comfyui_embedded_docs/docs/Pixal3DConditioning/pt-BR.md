# Pixal3DConditioning

O nó Pixal3DConditioning prepara o condicionamento de imagem para o pipeline de geração 3D do Trellis2. Ele usa um modelo de visão DINOv3 para extrair características visuais da imagem de entrada em duas resoluções (512 e 1024) e, em seguida, organiza-as em mapas de características por estágio que podem ser opcionalmente aprimorados por um modelo NAF. As informações da câmera são derivadas do campo de visão horizontal para construir a matriz de transformação de projeção, e o nó produz um par de condicionamento positivo (características derivadas da imagem mais dados de projeção) e um par de condicionamento negativo (tensores de características zerados) para orientação livre de classificador.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision. | CLIP_VISION | Sim | — |
| `imagem` | Imagem pré-processada do ImageCropToMask (pad_factor=1.1 para Pixal3D). | IMAGE | Sim | — |
| `camera_angle_x` | FOV horizontal em graus (exibido como `fov`). Conecte um MoGeGeometryToFOV (axis='horizontal', unit='degrees') para um FoV por imagem (corresponde ao padrão upstream). Padrão: 49.13. | FLOAT | Sim | 1.0 – 170.0 (passo 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | A saída de condicionamento positivo contendo os mapas de características derivados da imagem e os dados de projeção para a geração do Trellis2. | CONDITIONING |
| `negative` | A saída de condicionamento negativo com tensores de características zerados, usada para orientação livre de classificador. | CONDITIONING |

Observação: O valor de `camera_angle_x` é convertido de graus para radianos internamente, e a distância da câmera é calculada a partir dele para construir a matriz de transformação de projeção. Quando o modelo de visão fornecido inclui um componente NAF, o nó também produz mapas de características de alta resolução para os estágios de forma e textura.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`

# Pixal3D Conditioning Multivisualização

O nó Pixal3D Multi-View Conditioning cria dados de condicionamento a partir de um rig de câmera em órbita fixa: vistas frontal, esquerda, traseira e direita posicionadas com 90 graus de separação, usadas exatamente como enquadradas. Conecte pelo menos uma vista quadrada do objeto e ele prepara condicionamentos positivo e negativo correspondentes para modelos Pixal3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision com pesos NAF inclusos. | CLIP_VISION | Sim | N/A |
| `fov` | FOV horizontal em graus das vistas conforme enquadradas: 20 para renders de rig e a maioria dos geradores multi-view, ou MoGeGeometryToFOV em uma das vistas para fotos. Padrão: 20.0. | FLOAT | Sim | 1.0 - 170.0 |
| `front` | Vista quadrada da parte frontal do objeto, com alfa ou sobre fundo preto, enquadrada como o rig: o objeto ocupa cerca de 1/1,1 do quadro em sua maior largura, na mesma escala em todas as vistas. A primeira vista conectada (na ordem front, left, back, right) é a frente para a qual a malha é posicionada. | IMAGE | Não | N/A |
| `left` | Vista quadrada do lado esquerdo do objeto, com alfa ou sobre fundo preto, enquadrada como o rig: o objeto ocupa cerca de 1/1,1 do quadro em sua maior largura, na mesma escala em todas as vistas. A primeira vista conectada (na ordem front, left, back, right) é a frente para a qual a malha é posicionada. | IMAGE | Não | N/A |
| `back` | Vista quadrada do lado traseiro do objeto, com alfa ou sobre fundo preto, enquadrada como o rig: o objeto ocupa cerca de 1/1,1 do quadro em sua maior largura, na mesma escala em todas as vistas. A primeira vista conectada (na ordem front, left, back, right) é a frente para a qual a malha é posicionada. | IMAGE | Não | N/A |
| `right` | Vista quadrada do lado direito do objeto, com alfa ou sobre fundo preto, enquadrada como o rig: o objeto ocupa cerca de 1/1,1 do quadro em sua maior largura, na mesma escala em todas as vistas. A primeira vista conectada (na ordem front, left, back, right) é a frente para a qual a malha é posicionada. | IMAGE | Não | N/A |

### Notas

- Pelo menos uma vista deve estar conectada; o nó gera um erro se todas as quatro entradas de vista estiverem vazias.
- A primeira vista conectada, na ordem front, left, back, right, é tratada como a frente, e a malha é posicionada em relação a essa vista. Se a primeira vista conectada não for `front`, um aviso é registrado informando que a malha será posicionada com essa vista como sua frente.
- As vistas são lidas na ordem front, left, back, right e são posicionadas na órbita em seus azimutes fixos relativos à primeira vista conectada.
- Vistas de entrada com canal alfa têm o alfa aplicado sobre preto. Vistas que não são 1024 x 1024 são redimensionadas para 1024 x 1024.
- O tamanho do lote é obtido da primeira vista conectada. Se as vistas conectadas tiverem tamanhos de lote diferentes, as menores são repetidas ciclicamente para corresponder.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | A saída de condicionamento positivo, construída a partir das vistas codificadas e de suas características projetadas. | CONDITIONING |
| `negative` | A saída de condicionamento negativo, construída a partir de embeddings zerados com as mesmas características projetadas. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DMultiViewConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e6319ebd1a557dbb48269bab8a667e78e48f446d87fffbd9df4c4ebfb62b0fac`

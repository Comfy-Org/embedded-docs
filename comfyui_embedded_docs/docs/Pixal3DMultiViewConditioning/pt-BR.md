# Pixal3DMultiViewConditioning

## Visão Geral

O nó Pixal3D Multi-View Conditioning é uma estrutura de órbita fixa que gera vistas frontal, esquerda, traseira e direita de um objeto em intervalos de 90 graus. Ele é usado para criar vistas em molduras para aplicações Pixal3D, onde o objeto ocupa aproximadamente 1/1.1 da moldura no seu ponto mais largo, mantendo a mesma escala em cada vista.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision com pesos NAF embutidos. | MODEL | Sim | N/A |
| `fov` | FOV horizontal em graus das vistas conforme molduradas. | FLOAT | Sim | 1.0 - 170.0 |
| `frente` | Vista quadrada do lado frontal do objeto, com alpha ou em fundo preto. | IMAGE | Não | N/A |
| `esquerda` | Vista quadrada do lado esquerdo do objeto, com alpha ou em fundo preto. | IMAGE | Opcional | N/A |
| `trás` | Vista quadrada do lado traseiro do objeto, com alpha ou em fundo preto. | IMAGE | Opcional | N/A |
| `direita` | Vista quadrada do lado direito do objeto, com alpha ou em fundo preto. | IMAGE | Opcional | N/A |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positivo` | Saída de condicionamento positivo para o nó Pixal3D Multi-View Conditioning. | CONDITIONING |
| `negativo` | Saída de condicionamento negativo para o nó Pixal3D Multi-View Conditioning. | CONDITIONING |

## Notas

- O parâmetro `fov` controla o campo de visão horizontal das vistas conforme molduradas. Um valor de 20 graus é típico para renders de estruturas e a maioria dos geradores de multi-vistas.
- A primeira vista conectada (frontal, esquerda, traseira, direita na ordem) é considerada frontal, e a malha é posedada para essa vista.
- Se nenhuma vista frontal for fornecida, um aviso é registrado e a malha será posedada com a primeira vista conectada como sua frontal.
- O nó assume que as vistas são quadradas e molduradas como a estrutura. O objeto deve ocupar aproximadamente 1/1.1 da moldura no seu ponto mais largo, e a mesma escala deve ser mantida em cada vista.
- O nó gera dois objetos de Conditioning, um para o condicionamento positivo e outro para o negativo. Esses podem ser usados para condicionar modelos Pixal3D ou outros nós que aceitam entradas de Conditioning.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DMultiViewConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e6319ebd1a557dbb48269bab8a667e78e48f446d87fffbd9df4c4ebfb62b0fac`

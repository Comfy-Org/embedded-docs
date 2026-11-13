# Create Camera Orbit

Cria um rig de câmeras ao redor do alvo da primeira câmera: um giro horizontal (turntable) por padrão, uma varredura inclinada quando `pitch` é definido e, opcionalmente, vistas diretamente para baixo e para cima. Render Mesh renderiza uma imagem por câmera, e Bake Texture From Views as projeta de volta na malha.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `camera_info` | Primeira câmera da órbita. Para uma lista de câmeras, orbita cada câmera presente nela. | LOAD3D_CAMERA | Sim | - |
| `count` | Câmeras espaçadas uniformemente ao longo da varredura. Padrão: 4. | INT | Sim | 1 a 64 |
| `yaw` | Giro total ao redor do alvo, na direção yaw do Create Camera Info. Voltas completas param um passo antes da primeira câmera; as demais varreduras terminam na última câmera. Padrão: 360.0. | FLOAT | Sim | -720.0 a 720.0 (passo: 1.0) |
| `pitch` | Inclinação total sobre o alvo, positiva subindo como o `pitch` do Create Camera Info; acima de 90 as câmeras passam por cima. Voltas completas fazem loop como `yaw`. Padrão: 0.0. | FLOAT | Sim | -720.0 a 720.0 (passo: 1.0) |
| `poles` | Vistas diretamente para baixo e/ou para cima em direção ao alvo, adicionadas após a órbita. O topo da imagem delas aponta para longe da primeira câmera. Padrão: `"none"`. | COMBO | Sim | `"none"`<br>`"top"`<br>`"bottom"`<br>`"top and bottom"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `camera_info` | A lista de câmeras do rig, na ordem da órbita seguida pelas vistas dos polos. | LOAD3D_CAMERA |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateCameraOrbit/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b251efc969f8db7cf03527594be3bbd2af037f1ebb56bdf508bf264ddd9f8c08`

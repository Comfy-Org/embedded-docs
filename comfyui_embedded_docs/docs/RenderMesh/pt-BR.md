# RenderMesh

Este nó renderiza uma malha 3D em uma imagem 2D por ray casting de uma única vista. Ele pode exibir a malha texturizada, cores de vértice, uma superfície sombreada sólida, normais de superfície ou profundidade. A câmera e a transformação opcional do modelo podem vir de um visualizador Load3D / Preview3D; se nenhuma câmera estiver conectada, uma vista frontal padrão é enquadrada automaticamente.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `mesh` | A malha 3D a ser renderizada. | MESH | Sim | — |
| `mode` | O que renderizar. auto: textura se presente, caso contrário cores de vértice, caso contrário argila sombreada. (padrão: "auto") | COMBO | Sim | `"auto"`<br>`"texture"`<br>`"vertex colors"`<br>`"solid"`<br>`"normal"`<br>`"depth"` |
| `width` | Largura da imagem renderizada em pixels. (padrão: 1024) | INT | Sim | 64 a 4096 (passo 8) |
| `height` | Altura da imagem renderizada em pixels. (padrão: 1024) | INT | Sim | 64 a 4096 (passo 8) |
| `background` | Cor de fundo usada para pixels que a malha não cobre. (padrão: "#000000") | COLOR | Sim | — |
| `model_3d_info` | Transformação do modelo do mesmo visualizador Load3D / Preview3D. Conecte-o com `camera_info` para corresponder ao enquadramento do visualizador. | LOAD3D_MODEL_INFO | Não | — |
| `camera_info` | Câmera de um visualizador Load3D / Preview3D ou de um nó Create Camera Info. Se nenhuma for conectada, uma vista frontal padrão é enquadrada automaticamente. | LOAD3D_CAMERA | Não | — |

Nota: Apenas o primeiro item de uma malha em lote é renderizado — se o lote de malhas contiver mais de um item, o nó registra um aviso e usa o primeiro. O modo `texture` exige que a malha tenha textura e UVs, e o modo `vertex colors` exige cores de vértice; se os dados para o modo selecionado não estiverem disponíveis, o nó usa a renderização sombreada sólida. `model_3d_info` e `camera_info` devem ser conectados juntos a partir do mesmo visualizador Load3D / Preview3D para que a renderização corresponda ao enquadramento do visualizador.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `image` | A imagem renderizada da malha. | IMAGE |
| `mask` | Uma máscara que é 1.0 onde a malha foi renderizada e 0.0 em outros lugares. | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d23e85a904520eb2dfed899eb3e6a9cf45c980df00c034503687ac4eccc66ac4`

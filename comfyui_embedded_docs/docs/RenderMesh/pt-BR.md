# Renderizar Malha

Este nó renderiza uma malha 3D em uma imagem 2D por ray casting de uma única vista. Ele pode gerar a malha texturizada, cores de vértice, uma superfície com sombreamento sólido, normais de superfície ou profundidade. A câmera e a transformação opcional do modelo podem vir de um visualizador Load3D / Preview3D; se nenhuma câmera estiver conectada, uma vista frontal padrão é enquadrada automaticamente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha 3D a ser renderizada. | MESH | Sim | — |
| `mode` | O que renderizar. auto: textura, se presente; caso contrário, cores de vértice; caso contrário, argila sombreada. (padrão: "auto") `world normal`: normais no espaço do mundo giradas pelo yaw da primeira câmera. | COMBO | Sim | `"auto"`<br>`"texture"`<br>`"vertex colors"`<br>`"solid"`<br>`"normal"`<br>`"world normal"`<br>`"depth"` |
| `width` | Largura da imagem renderizada em pixels. (padrão: 1024) | INT | Sim | 64 a 4096 (passo 8) |
| `height` | Altura da imagem renderizada em pixels. (padrão: 1024) | INT | Sim | 64 a 4096 (passo 8) |
| `background` | Cor de fundo usada para pixels que a malha não cobre. (padrão: "#000000") | COLOR | Sim | — |
| `model_3d_info` | Transformação do modelo do mesmo visualizador Load3D / Preview3D. Conecte-o com `camera_info` para corresponder ao enquadramento do visualizador. | LOAD3D_MODEL_INFO | Não | — |
| `camera_info` | Câmera de um visualizador Load3D / Preview3D ou de um nó Create Camera Info. Se nenhuma estiver conectada, uma vista frontal padrão é enquadrada automaticamente. Uma lista de câmeras renderiza uma imagem por câmera. | LOAD3D_CAMERA | Não | — |
| `texture` | Exibida no lugar da textura da malha, por exemplo uma saída de Bake Texture From Views sem Apply Texture to Mesh. | IMAGE | Não | — |

Observação: Apenas o primeiro item de uma malha em lote é renderizado — se o lote de malhas contiver mais de um item, o nó registra um aviso e usa o primeiro. O modo `texture` exige que a malha tenha tanto uma textura quanto UVs, e o modo `vertex colors` exige cores de vértice; se os dados para o modo selecionado não estiverem disponíveis, o nó recorre à renderização sólida sombreada. O modo `normal` usa as normais suaves dos vértices da malha quando presentes; caso contrário, usa a normal por face. No modo `depth`, superfícies mais próximas aparecem mais claras (perto = branco) e pixels não cobertos pela malha permanecem pretos. O `model_3d_info` e o `camera_info` devem ser conectados juntos a partir do mesmo visualizador Load3D / Preview3D para que a renderização corresponda ao enquadramento do visualizador.

## Saídas

| Nome de Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem renderizada da malha. | IMAGE |
| `mask` | Uma máscara que é 1.0 onde a malha foi renderizada e 0.0 em outros locais. | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ad7d2f861fd7370fd50de9a9a45f8d46279528e6f0a90f02b539dec6a62c74bf`

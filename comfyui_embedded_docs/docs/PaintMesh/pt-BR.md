# Paint Mesh

PaintMesh recebe uma malha 3D e um campo de cores de voxel. Ele atribui a cada vértice a cor do voxel mais próximo no campo e retorna a malha com essas cores de vértice aplicadas. Se o campo de voxels estiver vazio, a malha é pintada com cores de vértice padrão zero (preto).

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha a ser pintada. | MESH | Sim | N/A |
| `voxel_colors` | Campo de voxels contendo dados de cor usados para pintura. Apenas os canais RGB de cor base são usados do campo. | VOXEL | Sim | N/A |

Observação: Quando as coordenadas do campo de voxels incluem um canal de índice de lote e a malha de entrada contém vários itens de malha, o nó aplica as cores separadamente a cada item de malha no lote. Se um determinado item de malha não tiver voxels correspondentes, ele receberá cores de vértice padrão zero (preto). As cores amostradas são convertidas de sRGB para RGB linear para a malha de saída, já que o campo de voxels pode carregar dados PBR completos, mas apenas o RGB da cor base é usado para as cores de vértice.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-----------|-----------|
| `mesh` | A malha pintada com cores de vértice aplicadas. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PaintMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `55683bef55b18487ba660fe619d6ec176f786de346be12724751b71901c14116`

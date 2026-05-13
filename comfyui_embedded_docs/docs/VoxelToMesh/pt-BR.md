> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/en.md)

O nó VoxelToMeshBasic converte dados de voxel 3D em uma geometria de malha extraindo uma superfície em um valor de limite especificado. Ele processa cada grade de voxel na entrada e gera vértices e faces que formam uma representação de malha 3D.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `voxel` | VOXEL | Sim | - | Os dados de voxel de entrada para converter em geometria de malha |
| `threshold` | FLOAT | Sim | -1.0 a 1.0 | O valor de limite para extração de superfície (padrão: 0.6) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `MESH` | MESH | A malha 3D gerada contendo vértices e faces empilhados de todas as grades de voxel de entrada |

---
**Source fingerprint (SHA-256):** `36df962c84c99a83f243a59b6387874e42e7d05323bd84079dbab112d2f1b67c`

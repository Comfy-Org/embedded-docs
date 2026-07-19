# VoxelParaMalha

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/en.md)

O nó VoxelToMeshBasic converte dados de voxel 3D em uma geometria de malha extraindo uma superfície em um valor de limite especificado. Ele processa cada grade de voxel na entrada e gera vértices e faces que formam uma representação de malha 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `voxel` | Os dados de voxel de entrada para converter em geometria de malha | VOXEL | Sim | - |
| `limiar` | O valor de limite para extração de superfície (padrão: 0.6) | FLOAT | Sim | -1.0 a 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `MESH` | A malha 3D gerada contendo vértices e faces empilhados de todas as grades de voxel de entrada | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `36df962c84c99a83f243a59b6387874e42e7d05323bd84079dbab112d2f1b67c`

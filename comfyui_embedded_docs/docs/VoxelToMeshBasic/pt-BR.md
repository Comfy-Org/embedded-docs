> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMeshBasic/pt-BR.md)

O nó VoxelToMeshBasic converte dados de voxel 3D em geometria de malha. Ele processa volumes de voxel aplicando um valor de limite para determinar quais partes do volume se tornam superfícies sólidas na malha resultante. O nó gera uma estrutura de malha completa com vértices e faces que pode ser utilizada para renderização e modelagem 3D.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `voxel` | VOXEL | Sim | - | Os dados de voxel 3D a serem convertidos em malha |
| `threshold` | FLOAT | Sim | -1.0 a 1.0 | O valor de limite usado para determinar quais voxels farão parte da superfície da malha (padrão: 0,6) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `MESH` | MESH | A malha 3D gerada contendo vértices e faces |

---
**Source fingerprint (SHA-256):** `36df962c84c99a83f243a59b6387874e42e7d05323bd84079dbab112d2f1b67c`

# VoxelParaMalha

O nó VoxelToMesh converte dados de voxel 3D em geometria de malha extraindo uma superfície em um valor de limiar especificado. Ele oferece dois algoritmos para extração de superfície: um método básico que cria faces simples semelhantes a caixas, e um método surface net que produz malhas mais suaves e detalhadas. O nó processa cada grade de voxels na entrada e gera vértices e faces que formam uma representação de malha 3D.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `voxel` | Os dados de voxel de entrada a serem convertidos em geometria de malha | VOXEL | Sim | - |
| `algoritmo` | O algoritmo usado para extração de superfície. "surface net" produz malhas mais suaves, enquanto "basic" cria faces simples semelhantes a caixas (padrão: "surface net") | COMBO | Sim | `"surface net"`<br>`"basic"` |
| `limiar` | O valor de limiar para extração de superfície. Voxels com valores acima deste limiar são considerados sólidos (padrão: 0.6) | FLOAT | Sim | -1.0 a 1.0 |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `MESH` | A malha 3D gerada contendo vértices e faces de todas as grades de voxels de entrada. Se todas as grades de voxels produzirem malhas com formas idênticas, a saída é um tensor empilhado; caso contrário, um lote de comprimento variável é retornado | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b600be13f1a484d8c0cc1f9c3918630d00c15d35008bcac0f677b21ef64b5d98`

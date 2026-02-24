> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/pt-BR.md)

O nó VoxelToMesh converte dados de voxel 3D em geometria de malha usando diferentes algoritmos. Ele processa grades de voxel e gera vértices e faces que formam uma representação de malha 3D. O nó suporta múltiplos algoritmos de conversão e permite ajustar o valor de limite para controlar a extração da superfície.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `voxel` | VOXEL | Sim | - | Os dados de voxel de entrada a serem convertidos em geometria de malha |
| `algorithm` | COMBO | Sim | "surface net"<br>"basic" | O algoritmo usado para conversão de malha a partir dos dados de voxel |
| `threshold` | FLOAT | Sim | -1.0 a 1.0 | O valor de limite para extração da superfície (padrão: 0.6) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `MESH` | MESH | A malha 3D gerada contendo vértices e faces |

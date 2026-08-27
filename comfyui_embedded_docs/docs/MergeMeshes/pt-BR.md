# MergeMeshes

MergeMeshes combina várias entradas de mesh em um único mesh, empilhando seus vértices, faces, coordenadas UV e cores de vértice, e ajustando os índices das faces para que o resultado seja um único mesh contínuo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `meshes` | Slot expansível: conecte de 2 a 50 objetos de mesh (nomeados `mesh_1`, `mesh_2`, ..., `mesh_50`). Todos os meshes conectados são mesclados em um único mesh de saída. | MESH | Sim | 2 a 50 meshes |

**Nota:** Apenas o primeiro item de mesh do lote de cada mesh de entrada é usado. Se algum mesh de entrada tiver dados de UV, a saída incluirá UVs e os meshes sem UVs receberão valores de UV preenchidos com zero. Se algum mesh de entrada tiver cores de vértice, a saída incluirá cores de vértice; meshes sem cores recebem cor branca (valor 1), e os canais de cor são preenchidos até a maior contagem de canais encontrada entre as entradas. Apenas a textura da primeira entrada que fornecer uma é mantida; texturas adicionais são descartadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | O mesh mesclado contendo todos os vértices, faces, UVs e cores das entradas combinados em um único mesh. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeMeshes/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0ce49b522f6348d524df20d6c27eb8bd9575c4a781790f6f8e3ac4f3ee255d38`

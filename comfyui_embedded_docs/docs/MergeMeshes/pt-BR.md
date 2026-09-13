# Mesclar malhas

MergeMeshes combina várias entradas de malha em uma única malha, empilhando seus vértices, faces, coordenadas UV e cores de vértice, e deslocando os índices das faces para que todas as partes se unam corretamente em uma malha contínua.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `malhas` | Slot expansível: conecte de 2 a 50 objetos de malha (nomeados `mesh_1`, `mesh_2`, ..., `mesh_50`). Todas as malhas conectadas são mescladas em uma malha de saída. | MESH | Sim | 2 a 50 malhas |

**Nota:** Pelo menos uma malha deve ser fornecida; caso contrário, o nó gera um erro. Apenas o primeiro item de malha do lote de cada malha de entrada é usado. As malhas de entrada são movidas para a CPU antes da mesclagem. Se alguma malha de entrada tiver dados UV, a saída incluirá UVs, e malhas sem UVs receberão valores UV preenchidos com zero. Se alguma malha de entrada tiver cores de vértice, a saída incluirá cores de vértice; malhas sem cores receberão cores brancas (valor 1), e os canais de cor serão preenchidos até a maior contagem de canais encontrada entre as entradas. Apenas a textura da primeira entrada que fornecer uma é mantida; texturas adicionais são descartadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha mesclada contendo todos os vértices, faces, UVs e cores de entrada combinados em uma única malha. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeMeshes/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0ce49b522f6348d524df20d6c27eb8bd9575c4a781790f6f8e3ac4f3ee255d38`

# MergeMeshes

MergeMeshes combina múltiplas malhas de entrada em uma única malha, empilhando seus vértices, faces, coordenadas UV e cores de vértice, e ajustando os índices de face para que o resultado seja uma malha contínua.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `malhas` | Slot expansível: conecte de 2 a 50 objetos de malha (nomeados `mesh_1`, `mesh_2`, ..., `mesh_50`). Todas as malhas conectadas são mescladas em uma única malha de saída. | MESH | Sim | 2 a 50 malhas |

**Nota:** Apenas o primeiro item de malha de cada lote de malha de entrada é usado. Se alguma malha de entrada tiver dados de UV, a saída inclui UVs e malhas sem UVs recebem valores de UV preenchidos com zeros. Se alguma malha de entrada tiver cores de vértice, a saída inclui cores de vértice; malhas sem cores recebem cores brancas (valor 1), e os canais de cor são preenchidos até a maior contagem de canais encontrada entre as entradas. Apenas a textura da primeira entrada que fornecer uma é mantida; texturas adicionais são descartadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `malha` | A malha mesclada contendo todos os vértices, faces, UVs e cores de entrada combinados em uma única malha. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeMeshes/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0ce49b522f6348d524df20d6c27eb8bd9575c4a781790f6f8e3ac4f3ee255d38`

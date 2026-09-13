# Desembrulhar UVs da malha

Gera um atlas UV para uma malha 3D. A superfície da malha é dividida em charts, cada chart é achatado em duas dimensões, e os charts achatados são empacotados em um atlas UV [0,1]. Os vértices nas costuras dos charts são duplicados (uma cópia por chart, mesma posição, UV próprio), então a malha de saída pode conter mais vértices que a malha de entrada, e o número de faces da saída pode diferir do da entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha de entrada a ser desdobrada. Aceita uma única malha ou um lote de malhas; lotes são processados um item por vez. | MESH | Sim | — |
| `segmenter` | Algoritmo de geração de charts a usar. `pec`: geração de charts rápida por colapso de arestas paralelas na GPU. `adaptive`: CPU, mais lento. (padrão: "pec") | COMBO | Sim | "pec"<br>"adaptive" |
| `resolution` | Resolução alvo do atlas para autoescala de densidade de texels (0 = ajustar ao conteúdo). (padrão: 1024) | INT | Sim | 0 a 8192 (passo 256) |
| `padding` | Preenchimento de texels entre charts. (padrão: 1) | INT | Sim | 0 a 16 |
| `weld_distance` | Raio de fusão de vértices coincidentes como uma fração da extensão da malha (0 = automático). Aumente para ~0.001 se forem gerados charts por triângulo (entrada não soldada). (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 (passo 0.0001) |

Nota: se a malha de entrada contiver vértices não soldados, o nó pode avisar que a adjacência de faces está baixa e produzir charts UV por face; aumentar `weld_distance` funde vértices coincidentes antes do desdobramento. Faces degeneradas (faces que reutilizam o mesmo índice de vértice) são descartadas durante o processamento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha de entrada com um atlas UV gerado no intervalo [0,1]. Os vértices de costura são duplicados, então a contagem de vértices de saída pode exceder a de entrada. As cores dos vértices e a textura da malha de entrada são preservadas. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fcab6f0b621693d862ee74b5ec498498d2f1f247a66f478704377598a6b39388`

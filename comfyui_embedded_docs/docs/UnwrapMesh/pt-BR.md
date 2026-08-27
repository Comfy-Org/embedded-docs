# UnwrapMesh

Gera um atlas UV para uma malha 3D. A superfície é dividida em ilhas, cada ilha é achatada em duas dimensões e os resultados são empacotados em um atlas UV [0,1]. Vértices nas costuras das ilhas são duplicados, portanto a malha de saída pode conter mais vértices do que a entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha de entrada para desembrulhar. Aceita uma única malha ou um lote de malhas. | MESH | Sim | — |
| `segmenter` | Algoritmo de geração de ilhas a ser usado. pec: particionamento rápido por colapso de arestas paralelas na GPU. adaptive: CPU, mais lento. (padrão: "pec") | COMBO | Sim | "pec"<br>"adaptive" |
| `resolution` | Resolução alvo do atlas para escala automática de densidade de texel (0 = ajustar ao conteúdo). (padrão: 1024) | INT | Sim | 0 a 8192 (passo 256) |
| `padding` | Espaçamento (padding) de texel entre as ilhas. (padrão: 1) | INT | Sim | 0 a 16 |
| `weld_distance` | Raio de fusão de vértices coincidentes como uma fração da extensão da malha (0 = automático). Aumente para ~0.001 se você obtiver ilhas por triângulo (entrada sem fusão). (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 (passo 0.0001) |

Nota: se a malha de entrada contiver vértices sem fusão (sopa de triângulos), o nó pode avisar que a adjacência de faces é baixa e produzir ilhas UV por face; aumentar `weld_distance` funde os vértices coincidentes antes do desembrulhamento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha de entrada com um atlas UV gerado em [0,1]. Vértices de costura são duplicados, portanto a contagem de vértices da saída pode exceder a da entrada. As cores de vértice e a textura da malha de entrada são preservadas. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cf0dbbe43df507921e6e9795b42d5cb5691ccc2ae98a8bb17e02e3928ea0b815`

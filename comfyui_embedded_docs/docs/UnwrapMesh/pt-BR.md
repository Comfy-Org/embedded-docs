# UnwrapMesh

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-----------|--------------|-------------|-----------|
| `mesh` | A malha de entrada para desembrulhar. Aceita uma única malha ou um lote de malhas. | MESH | Sim | — |
| `segmenter` | Algoritmo de criação de ilhas a ser usado. pec: criação rápida de ilhas por colapso de arestas paralelas na GPU. adaptive: CPU, mais lento. (padrão: "pec") | COMBO | Sim | "pec"<br>"adaptive" |
| `resolution` | Resolução alvo do atlas para escala automática de densidade de texel (0 = ajustar ao conteúdo). (padrão: 1024) | INT | Sim | 0 a 8192 (passo 256) |
| `padding` | Preenchimento de texel entre ilhas. (padrão: 1) | INT | Sim | 0 a 16 |
| `weld_distance` | Raio de mesclagem de vértices coincidentes como fração da extensão da malha (0 = automático). Aumente para ~0.001 se você obtiver ilhas por triângulo (entrada não soldada). (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 (passo 0.0001) |

Nota: se a malha de entrada contiver vértices não soldados (sopa de triângulos), o nó pode avisar que a adjacência de faces é baixa e produzir ilhas UV por face; aumentar `weld_distance` mescla vértices coincidentes antes de desembrulhar.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `mesh` | A malha de entrada com um atlas UV gerado em [0,1]. Vértices de emenda são duplicados, portanto a contagem de vértices da saída pode exceder a da entrada. As cores dos vértices e a textura da malha de entrada são preservadas. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cf0dbbe43df507921e6e9795b42d5cb5691ccc2ae98a8bb17e02e3928ea0b815`

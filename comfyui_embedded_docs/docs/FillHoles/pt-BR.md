# Preencher Buracos

Este nó preenche buracos em uma malha 3D detectando arestas de contorno abertas e criando novas faces para fechá-las. Ele é executado na GPU, preserva a geometria e as UVs existentes e pode processar malhas individuais, listas de malhas ou lotes de malhas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|----------|-------|
| `mesh` | A malha 3D a processar. Aceita uma malha individual, uma lista de malhas ou uma malha em lote. | MESH | Sim | - |
| `max_perimeter` | Perímetro máximo do buraco a preencher. 0 desativa. (padrão: 0.03) | FLOAT | Sim | 0.0 até sem limite superior (passo 0.0001) |
| `weld_epsilon_rel` | Tolerância de pré-soldagem (fração da diagonal da caixa delimitadora); a detecção de contorno precisa de vértices soldados. 0 ignora. (padrão: 1e-5) | FLOAT | Sim | 0.0 até sem limite superior (passo 1e-6) |
| `max_vertices` | Limita os vértices de contorno por ciclo; o preenchimento centroid-fan só funciona para buracos pequenos e quase planares. Mantenha ≤16. (padrão: 16) | INT | Sim | 3 a 1024 |
| `fill_chains` | Também preenche cadeias abertas (não apenas ciclos). Ruidoso; OFF corresponde ao cumesh. (padrão: False) | BOOLEAN | Sim | True ou False |

Nota: Quando `max_perimeter` é maior que 0, o nó preenche buracos; quando é 0, o preenchimento de buracos é totalmente ignorado. Quando `weld_epsilon_rel` é maior que 0, o nó pré-solda vértices duplicados antes de detectar buracos. A tolerância de soldagem começa na fração fornecida da diagonal da caixa delimitadora e aumenta automaticamente, dobrando, até que a malha seja considerada soldada ou a tolerância atinja um limite de 1e-2. Buracos com mais de 8 vértices de contorno usam um preenchimento centroid-fan (em leque a partir do centroide), inserindo um novo vértice de centroide, enquanto buracos menores usam um preenchimento vertex-fan (em leque a partir de vértice), que reutiliza um vértice de contorno existente. Por padrão, apenas ciclos de contorno fechados são preenchidos; defina `fill_chains` como True para também fechar cadeias abertas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha com os buracos preenchidos, correspondendo ao formato de lote da entrada. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FillHoles/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c0fd7f0c2d6eea098efb1dcfd80eaa52997e185b9c442b483f75318eea082196`

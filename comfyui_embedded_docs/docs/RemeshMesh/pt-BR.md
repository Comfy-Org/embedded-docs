# RemeshMesh

Remesh Mesh reconstrói uma malha com uma tesselação limpa e uniforme, amostrando um campo de distância de banda estreita ao redor da superfície original e extraindo-o com Dual Contouring. Isso normaliza topologias bagunçadas, não manifold ou com autointersecções, e deve ser executado antes do Decimate Mesh para atingir uma contagem exata de faces. O processamento roda no dispositivo de computação ativo e a malha de saída permanece soldada.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha de entrada a ser remalhada. | MESH | Sim | — |
| `resolution` | Resolução da grade de voxels (densidade de saída). 256 ~ 100 mil faces, 512 ~ 1 milhão. Para uma contagem exata de faces, prossiga com o Decimate Mesh. (padrão: 512) | INT | Sim | 32 - 2048 |
| `sign_mode` | Modo de distância sinalizada usado para extração de superfície. `"udf"` é robusto a entradas bagunçadas/não manifold; `"sdf"` produz uma única superfície limpa com recuperação de arestas vivas via QEF (Quadratic Error Function), mas exige orientação (winding) consistente. Selecionar um modo revela suas subopções específicas. (padrão: `"udf"`) | DYNAMIC_COMBO | Sim | `"udf"`<br>`"sdf"` |
| `band` | Largura da banda estreita em unidades de voxel. No modo UDF, também desloca a superfície. (avançado, padrão: 1.0) | FLOAT | Sim | 0.5 - 4.0 |
| `project_back` | Interpola linearmente os vértices em direção à superfície original (0 = DC puro, 1 = encaixado na superfície). (avançado, padrão: 0.0) | FLOAT | Sim | 0.0 - 1.0 |
| `fix_poles` | Colapsa pares de vértices de valência 3 (artefato de junção em T do DC). (avançado, padrão: false) | BOOLEAN | Sim | true / false |
| `smooth_iters` | Iterações de suavização de Taubin (0 = desligado). 2 a 3 removem artefatos em escada do DC; valores maiores suavizam demais as arestas QEF. (padrão: 0) | INT | Sim | 0 - 20 |
| `drop_small_components` | Remove componentes abaixo desta fração da contagem de faces do maior componente. 0 desativa. (avançado, padrão: 0.01) | FLOAT | Sim | 0.0 - 0.5 |
| `precluster_max_verts` | Limita a contagem de vértices de entrada antes das consultas de campo; entradas acima deste valor são primeiro decimadas por cluster até esse limite. Evita falta de memória (OOM) em malhas enormes. (avançado, padrão: 20.000.000) | INT | Sim | 0 - 100,000,000 |

### Entradas do modo `"udf"`

Estes parâmetros aparecem quando `sign_mode` está definido como `"udf"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `qef` | Posicionamento de vértices duais via QEF (Quadratic Error Function) para arestas mais nítidas. (padrão: false) | BOOLEAN | Não | true / false |
| `drop_inverted_components` | Remove componentes fechados com normal voltada para dentro (volume negativo) — a casca interna da UDF. (padrão: false) | BOOLEAN | Não | true / false |
| `drop_enclosed_components` | Remove componentes dentro do bbox do maior que falham em um raycast de ponto na malha. Desative para peças aninhadas legítimas. (padrão: false) | BOOLEAN | Não | true / false |

### Entradas do modo `"sdf"`

Estes parâmetros aparecem quando `sign_mode` está definido como `"sdf"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `qef` | Posicionamento de vértices duais via QEF (Quadratic Error Function) (recupera arestas vivas) em vez do centróide de cruzamento de arestas. (padrão: true) | BOOLEAN | Não | true / false |
| `manifold` | Dual Contouring manifold: 1 a 4 vértices duais por voxel para casos de múltiplas folhas. Mais lento. (padrão: false) | BOOLEAN | Não | true / false |

Nota: A opção `qef` tem um padrão diferente dependendo do modo selecionado — false no modo `"udf"`, true no modo `"sdf"`. Quando `precluster_max_verts` é maior que 0 e a malha de entrada tem mais vértices que esse valor, a malha é decimada por cluster até esse alvo antes das consultas de campo. Após o processamento, o nó exibe a variação do número de faces da entrada para a saída no próprio nó (por exemplo, `"faces: 1.23M → 200K (-84%)"`).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha remalhada com tesselação uniforme e topologia soldada. As cores de vértice são preservadas quando presentes na entrada; UVs, normais e tangentes não são transferidos. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `33b9603aad2aa8f4122dab75aa9d60caa0ab7ed81300461f3b773bb997251d99`

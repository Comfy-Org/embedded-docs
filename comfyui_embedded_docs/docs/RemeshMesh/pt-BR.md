# Remesh Mesh (Narrow-Band DC)

Remesh Mesh reconstrói uma malha com uma tesselação limpa e uniforme, amostrando um campo de distância de banda estreita ao redor da superfície original e extraindo-o com Dual Contouring. Isso normaliza topologias bagunçadas, não-manifold ou com autointerseção, e deve ser executado antes de Decimate Mesh para alcançar uma contagem exata de faces. O processamento é executado no dispositivo de computação ativo e a malha de saída permanece soldada.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `malha` | A malha de entrada a ser remalhada. | MESH | Sim | — |
| `resolução` | Resolução da grade de voxels (densidade de saída). 256 ~ 100 mil faces, 512 ~ 1M. Para uma contagem exata de faces, prossiga com Decimate Mesh. (padrão: 512) | INT | Sim | 32 - 2048 |
| `sign_mode` | Modo de extração de superfície. "udf" é robusto para entradas bagunçadas/não-manifold; "sdf" produz uma superfície única limpa com recuperação de características nítidas por QEF (Função de Erro Quadrático), mas exige ordem de winding consistente. "solid" constrói um único sólido estanque a partir de uma entrada bagunçada: um corte de grafo global interno/externo (CelloCut) remove as cascas duplas e fecha os furos pequenos. Mais lento. Selecionar um modo revela suas subopções específicas. (padrão: "udf") | DYNAMIC_COMBO | Sim | "udf"<br>"sdf"<br>"solid" |
| `banda` | Largura da banda estreita em unidades de voxel. No modo UDF, também desloca a superfície. No modo solid é o raio de fechamento: as dobras são arredondadas e as lacunas preenchidas nesse tamanho, e a superfície fica meio voxel para fora. (avançado, padrão: 1.0) | FLOAT | Sim | 0.5 - 4.0 |
| `project_back` | Interpola linearmente os vértices em direção à superfície original (0 = DC puro, 1 = ajustado). (avançado, padrão: 0.0) | FLOAT | Sim | 0.0 - 1.0 |
| `fix_poles` | Colapsa pares de vértices de valência 3 (artefato de junção em T do DC). (avançado, padrão: false) | BOOLEAN | Sim | true / false |
| `smooth_iters` | Iterações de suavização de Taubin (0 = desativado). 2-3 limpam artefatos semelhantes a escadas do DC; valores mais altos suavizam demais as arestas QEF. (padrão: 0) | INT | Sim | 0 - 20 |
| `drop_small_components` | Descarta componentes abaixo desta fração da contagem de faces do maior componente. 0 desativa. (avançado, padrão: 0.01) | FLOAT | Sim | 0.0 - 0.5 |
| `precluster_max_verts` | Limita a contagem de vértices de entrada antes das consultas de campo; entradas acima disso são reduzidas por cluster para esse valor primeiro. Evita OOM em malhas enormes. (avançado, padrão: 20,000,000) | INT | Sim | 0 - 100,000,000 |

### Entradas do modo "udf"

Esses parâmetros aparecem quando `sign_mode` está definido como `"udf"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `qef` | Posicionamento de vértices por QEF (Função de Erro Quadrático): arestas nítidas em entradas de superfície dura e dobras irregulares em entradas orgânicas. (avançado, padrão: false) | BOOLEAN | Não | true / false |
| `drop_inverted_components` | Descarta componentes fechados com normal voltada para dentro (volume negativo) — a casca interna do UDF. (avançado, padrão: false) | BOOLEAN | Não | true / false |
| `drop_enclosed_components` | Descarta componentes dentro da bbox do maior componente que falham em um raycast de ponto na malha. Desative para peças aninhadas legítimas. (avançado, padrão: false) | BOOLEAN | Não | true / false |

### Entradas do modo "sdf"

Esses parâmetros aparecem quando `sign_mode` está definido como `"sdf"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `qef` | Posicionamento de vértice dual por QEF (Função de Erro Quadrático) (recupera características nítidas) vs. centroide de cruzamento de aresta. (padrão: true) | BOOLEAN | Não | true / false |
| `manifold` | Dual Contouring manifold: 1-4 vértices duais/voxel para casos de múltiplas folhas. Mais lento. (padrão: false) | BOOLEAN | Não | true / false |

### Entradas do modo "solid"

Esses parâmetros aparecem quando `sign_mode` está definido como `"solid"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `fill` | Custo de fechar uma abertura em relação a seguir a superfície. Quanto menor, maiores são as aberturas fechadas (0 coloca uma tampa em uma xícara); quanto maior, apenas furos e rachaduras pequenos são fechados. (padrão: 20.0) | FLOAT | Não | 0.0 - 1000.0 |
| `qef` | Posicionamento de vértices por QEF (Função de Erro Quadrático): arestas nítidas em entradas de superfície dura e dobras irregulares em entradas orgânicas. (avançado, padrão: false) | BOOLEAN | Não | true / false |

Observação: A opção `qef` tem um padrão diferente dependendo do modo selecionado — false nos modos "udf" e "solid", true no modo "sdf". Quando `precluster_max_verts` é maior que 0 e a malha de entrada tem mais vértices que esse valor, a malha é reduzida por cluster até esse alvo antes das consultas de campo. Após o processamento, o nó exibe a mudança na contagem de faces da entrada para a saída no próprio nó (por exemplo, "faces: 1.23M → 200K (-84%)").

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `mesh` | A malha remalhada com tesselação uniforme e topologia soldada. As cores dos vértices são preservadas quando presentes na entrada; quaisquer UVs, normais e tangentes não são transferidas. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d2869c681e0485f5946a53f0582188ded2183ecd741ea1ff6a591932b18b5abe`

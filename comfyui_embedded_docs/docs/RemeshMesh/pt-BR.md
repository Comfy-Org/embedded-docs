# Remesh Mesh (Narrow-Band DC)

Remesh Mesh reconstrói uma malha com uma tesselação limpa e uniforme, amostrando um campo de distância de banda estreita ao redor da superfície original e extraindo-o com Dual Contouring. Isso normaliza topologias bagunçadas, não-manifold ou com autointerseção, e deve ser executado antes de Decimate Mesh para alcançar uma contagem exata de faces. O processamento é executado no dispositivo de computação ativo e a malha de saída permanece soldada.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha de entrada a ser remalhada. | MESH | Sim | — |
| `resolution` | Resolução da grade de voxels (densidade de saída). 256 ~ 100 mil faces, 512 ~ 1M. Para uma contagem exata de faces, prossiga com Decimate Mesh. (padrão: 512) | INT | Sim | 32 - 2048 |
| `sign_mode` | Modo de extração de superfície. "udf" é robusto para entradas bagunçadas/não-manifold; "sdf" produz uma superfície única limpa com recuperação de características nítidas por QEF (Função de Erro Quadrático), mas exige ordem de winding consistente. Selecionar um modo revela suas subopções específicas. (padrão: "udf") | DYNAMIC_COMBO | Sim | "udf"<br>"sdf" |
| `band` | Largura da banda estreita em unidades de voxel. No modo UDF, também desloca a superfície. (avançado, padrão: 1.0) | FLOAT | Sim | 0.5 - 4.0 |
| `project_back` | Interpola linearmente os vértices em direção à superfície original (0 = DC puro, 1 = ajustado). (avançado, padrão: 0.0) | FLOAT | Sim | 0.0 - 1.0 |
| `fix_poles` | Colapsa pares de vértices de valência 3 (artefato de junção em T do DC). (avançado, padrão: false) | BOOLEAN | Sim | true / false |
| `smooth_iters` | Iterações de suavização de Taubin (0 = desativado). 2-3 limpam artefatos semelhantes a escadas do DC; valores mais altos suavizam demais as arestas QEF. (padrão: 0) | INT | Sim | 0 - 20 |
| `drop_small_components` | Descarta componentes abaixo desta fração da contagem de faces do maior componente. 0 desativa. (avançado, padrão: 0.01) | FLOAT | Sim | 0.0 - 0.5 |
| `precluster_max_verts` | Limita a contagem de vértices de entrada antes das consultas de campo; entradas acima disso são reduzidas por cluster para esse valor primeiro. Evita OOM em malhas enormes. (avançado, padrão: 20,000,000) | INT | Sim | 0 - 100,000,000 |

### Entradas do modo "udf"

Esses parâmetros aparecem quando `sign_mode` está definido como `"udf"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `qef` | Posicionamento de vértice dual por QEF (Função de Erro Quadrático) para arestas mais nítidas. (avançado, padrão: false) | BOOLEAN | Não | true / false |
| `drop_inverted_components` | Descarta componentes fechados com normal voltada para dentro (volume negativo) — a casca interna do UDF. (avançado, padrão: false) | BOOLEAN | Não | true / false |
| `drop_enclosed_components` | Descarta componentes dentro da bbox do maior componente que falham em um raycast de ponto na malha. Desative para peças aninhadas legítimas. (avançado, padrão: false) | BOOLEAN | Não | true / false |

### Entradas do modo "sdf"

Esses parâmetros aparecem quando `sign_mode` está definido como `"sdf"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `qef` | Posicionamento de vértice dual por QEF (Função de Erro Quadrático) (recupera características nítidas) vs. centroide de cruzamento de aresta. (padrão: true) | BOOLEAN | Não | true / false |
| `manifold` | Dual Contouring manifold: 1-4 vértices duais/voxel para casos de múltiplas folhas. Mais lento. (padrão: false) | BOOLEAN | Não | true / false |

Observação: A opção `qef` tem um padrão diferente dependendo do modo selecionado — false no modo "udf", true no modo "sdf". Quando `precluster_max_verts` é maior que 0 e a malha de entrada tem mais vértices que esse valor, a malha é reduzida por cluster até esse alvo antes das consultas de campo. Após o processamento, o nó exibe a mudança na contagem de faces da entrada para a saída no próprio nó (por exemplo, "faces: 1.23M → 200K (-84%)").

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `mesh` | A malha remalhada com tesselação uniforme e topologia soldada. As cores dos vértices são preservadas quando presentes na entrada; quaisquer UVs, normais e tangentes não são transferidas. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `aa9b7e4465196fab81a4a484ca9dd03d999b4621a611aed2b39d618e53702a06`

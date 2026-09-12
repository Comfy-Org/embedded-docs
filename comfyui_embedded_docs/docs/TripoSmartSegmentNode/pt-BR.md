# TripoSmartSegmentNode

Divide um modelo 3D em partes semanticamente significativas e dá um nome a cada parte. Ele pode segmentar um modelo existente (fornecido por meio de um ID de tarefa) ou primeiro gerar um modelo a partir de uma imagem e depois segmentá-lo. O `segment task_id` resultante pode ser usado por outros nós do Tripo, como Complete Mesh Parts, Retopology, Texture model e Convert model, da mesma forma que um resultado de Tripo: Segment Model.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|-----------|----------|-------|
| `source` | Segmenta um modelo existente ou gera um modelo a partir de uma imagem e o segmenta. A opção selecionada determina quais entradas adicionais aparecem. | DYNAMIC_COMBO | Sim | `"model"`<br>`"image"` |

### Entradas do modelo

Exibido quando `source` está definido como `"model"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|-----------|----------|-------|
| `model_task_id` | Um resultado GLB. Malhas quad (FBX) precisam passar primeiro por Tripo: Convert model (GLTF). | MODEL_TASK_ID | Sim | - |
| `granularity` | Com que nível de detalhe o modelo é dividido em partes (padrão: "medium"). | COMBO | Não | `"coarse"`<br>`"medium"`<br>`"fine"` |
| `hint` | Texto opcional nomeando as partes a procurar, por exemplo, 'personagem de jogo com espada e armadura' (padrão: vazio). | STRING | Não | - |

### Entradas de imagem

Exibido quando `source` está definido como `"image"`. O Tripo primeiro gera um modelo a partir da imagem e depois o segmenta.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|-----------|----------|-------|
| `image` | A imagem usada para gerar o modelo que será segmentado. | IMAGE | Sim | - |
| `granularity` | Com que nível de detalhe o modelo é dividido em partes (padrão: "medium"). | COMBO | Não | `"coarse"`<br>`"medium"`<br>`"fine"` |
| `hint` | Texto opcional nomeando as partes a procurar, por exemplo, 'personagem de jogo com espada e armadura' (padrão: vazio). | STRING | Não | - |

**Notas:**

- `granularity` e `hint` são compartilhados por ambas as opções de `source` e são opcionais. Quando `hint` é deixado vazio, nenhuma dica é enviada ao serviço.
- Quando `source` é `"model"`, apenas modelos GLB são aceitos. Outros formatos, como malhas quad (FBX), devem ser convertidos primeiro com Tripo: Convert model (GLTF).
- A tarefa é consultada periodicamente até atingir um estado terminal, com duração estimada de cerca de 180 segundos. Se o Tripo retornar um resultado de segmentação incompleto, o nó reporta um erro.
- Selo de preço: aproximadamente 0,85 USD quando `source` é `"image"` e aproximadamente 0,55 USD quando `source` é `"model"` (valores exibidos como aproximados).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `task_id de segmentação` | ID da tarefa de segmentação, utilizável como entrada para outros nós do Tripo. | SEGMENT_TASK_ID |
| `task_id do modelo` | O modelo que foi segmentado (gerado a partir da imagem ou importado). | MODEL_TASK_ID |
| `GLB` | O arquivo de modelo 3D segmentado. | FILE3DGLB |
| `part_names` | Nomes das partes separados por vírgula. | STRING |
| `parts` | Descrição do Tripo das partes que ele encontrou. | STRING |
| `máscara` | Imagem de máscara produzida pela segmentação. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartSegmentNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ba041da49e20b1ac085770078cce6ac87ef70eee927ba0ee9e5655a058893f1c`

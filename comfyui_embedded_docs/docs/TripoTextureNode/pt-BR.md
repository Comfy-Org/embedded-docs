# Tripo: Aplicar textura ao modelo (Legado)

## Visão geral

O nó Tripo: Texture model (Legacy) adiciona texturas a um modelo 3D Tripo existente por meio da API do Tripo. Ele recebe o ID da tarefa de um modelo criado por outro nó do Tripo e retorna um modelo GLB ou FBX texturizado quando o trabalho de texturização termina. Você pode controlar os mapas de material, a qualidade da textura, o alinhamento e a semente, além de orientar as texturas com um prompt de texto, uma imagem de estilo ou imagens de referência. Este nó é uma versão legada da ferramenta de textura.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | O ID da tarefa do Tripo para o modelo a ser texturizado. Aceita IDs de tarefa de modelo e IDs de tarefa de segmentação. | MODEL_TASK_ID, SEGMENT_TASK_ID | Sim | - |
| `texture` | Ignorado: este nó sempre gera texturas. Mantido para fluxos de trabalho mais antigos. (padrão: True) | BOOLEAN | Não | true<br>false |
| `pbr` | Mapas de material PBR (cor base, metálico, rugosidade, normal); desativado gera uma textura de cor plana. (padrão: True) | BOOLEAN | Não | true<br>false |
| `texture_seed` | Semente aleatória para geração de textura. (padrão: 42) | INT | Não | 0 – 2147483647 |
| `texture_quality` | Qualidade de resolução da textura: detailed = texturas HD, extreme = texturas 8K Ultra. (padrão: "standard"). Custo aproximado: standard $0.10, detailed $0.20, extreme $0.30. | COMBO | Não | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Método usado para alinhar as texturas geradas ao modelo. (padrão: "original_image") | COMBO | Não | "original_image"<br>"geometry" |
| `texture_prompt` | Orientação textual opcional para texturização. Obrigatória na prática para modelos importados (Tripo: Import Model), que não possuem imagem de origem para inferir cores. Não pode ser combinada com imagens de referência. (padrão: "") | STRING | Não | - |
| `model_version` | Modelo de textura: v3.0 para malhas geradas com v3.x, v2.5 para malhas geradas com v2.5. (padrão: v3.0_20250812) | COMBO | Não | Várias opções disponíveis |
| `style_image` | Imagem de referência para o estilo artístico das texturas. Usada apenas junto com `texture_prompt`. | IMAGE | Não | - |
| `reference` | Imagens de referência que orientam as texturas. Não podem ser combinadas com `texture_prompt` ou `style_image`. (padrão: "none") | DYNAMIC_COMBO | Não | "none"<br>"image"<br>"multiview" |
| `part_names` | Nomes de partes separados por vírgula do nó Tripo: Segment Model que devem ser texturizadas. Vazio texturiza todas as partes. (padrão: "") | STRING | Não | - |

### Entradas de referência para `image`

Estas entradas estão disponíveis quando `reference` está definido como `"image"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | Imagem de referência única que as texturas devem seguir. | IMAGE | Sim | - |

### Entradas de referência para `multiview`

Estas entradas estão disponíveis quando `reference` está definido como `"multiview"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image_front` | Vista frontal (0°). | IMAGE | Sim | - |
| `image_left` | Vista esquerda (90°). | IMAGE | Sim | - |
| `image_back` | Vista traseira (180°). | IMAGE | Sim | - |
| `image_right` | Vista direita (270°). | IMAGE | Sim | - |

**Nota:** Os modos de referência `"image"` e `"multiview"` não podem ser combinados com um `texture_prompt` não vazio ou com `style_image`. A entrada `style_image` exige um `texture_prompt` não vazio. Quando `texture_prompt` é deixado vazio, o modelo de origem já deve ter sua própria imagem de origem (por exemplo, modelos produzidos por text-to-model, image-to-model, multiview-to-model ou uma tarefa de texturização anterior). Modelos que não possuem imagem de origem — como modelos importados, segmentados, concluídos ou retopologizados — devem ser texturizados com um `texture_prompt`; imagens de referência são aceitas apenas para modelos gerados pela própria API do Tripo. A entrada `part_names` pode ser deixada vazia para texturizar todas as partes.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `model_file` | O arquivo de modelo gerado (apenas para compatibilidade com versões anteriores). | STRING |
| `model task_id` | O ID da tarefa concluída de geração de textura, utilizável como entrada para outros nós do Tripo. | MODEL_TASK_ID |
| `GLB` | O modelo texturizado gerado no formato GLB. Vazio quando a origem é uma malha quad ou uma importação FBX. | FILE3DGLB |
| `FBX` | O modelo texturizado gerado no formato FBX. O Tripo retorna FBX para malhas quad e importações FBX; vazio caso contrário. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `850685123b5f14cded5829d86a7307452a1e812e78d11f52806e64ea41d66350`

# TripoTextureNodeV2

Este nó adiciona texturas a um modelo 3D existente de um fluxo de trabalho Tripo, identificado por um ID de tarefa de uma etapa de geração anterior. Ele pode produzir mapas de material PBR ou uma textura de cor sólida, e o resultado pode ser orientado por um prompt de texto, uma imagem de estilo ou imagens de referência.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `model_task_id` | ID de tarefa do modelo de origem produzido por um nó Tripo anterior (geração de modelo ou segmentação de modelo). | MODEL_TASK_ID / SEGMENT_TASK_ID | Sim | - |
| `pbr` | Mapas de material PBR (cor base, metálico, rugosidade, normal); desativado gera uma textura de cor sólida. (padrão: true) | BOOLEAN | Não | true<br>false |
| `texture_seed` | Semente usada para geração de textura. (padrão: 42) Entrada avançada. | INT | Não | 0 a 2147483647 |
| `texture_quality` | Qualidade das texturas geradas. `detailed` = texturas HD, `extreme` = texturas 8K Ultra. (padrão: "standard") Entrada avançada. | COMBO | Não | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Como as texturas são alinhadas ao modelo. (padrão: "original_image") Entrada avançada. | COMBO | Não | "original_image"<br>"geometry" |
| `texture_prompt` | Orientação textual opcional para texturização. Obrigatório na prática para modelos importados (Tripo: Import Model), que não possuem imagem de origem para inferir cores. Não pode ser combinado com imagens de referência. (padrão: vazio) | STRING | Não | - |
| `model_version` | Modelo de textura: v3.0 para malhas geradas com v3.x, v2.5 para malhas geradas com v2.5. (padrão: v3_0_20250812) | COMBO | Não | Versões do modelo de textura Tripo, padrão "v3_0_20250812" |
| `style_image` | Imagem de referência para o estilo artístico das texturas. Usada apenas junto com `texture_prompt`. | IMAGE | Não | - |
| `reference` | Imagens de referência que orientam as texturas. Não pode ser combinado com `texture_prompt` ou `style_image`. (padrão: "none") | DYNAMIC_COMBO | Não | "none"<br>"image"<br>"multiview" |
| `part_names` | Nomes de partes separados por vírgula do Tripo: Segment Model a serem texturizadas. Vazio texturiza todas as partes. (padrão: vazio) Entrada avançada. | STRING | Não | - |

### Entradas de referência de imagem

Exibidas quando `reference` está definido como "image".

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `reference_image` | Imagem de referência única que as texturas devem seguir. | IMAGE | Sim | - |

### Entradas de referência multivisão

Exibidas quando `reference` está definido como "multiview".

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `image_front` | Vista frontal (0°). | IMAGE | Sim | - |
| `image_left` | Vista esquerda (90°). | IMAGE | Sim | - |
| `image_back` | Vista traseira (180°). | IMAGE | Sim | - |
| `image_right` | Vista direita (270°). | IMAGE | Sim | - |

**Notas sobre restrições de parâmetros:**

- Imagens de referência (modos de referência "image" ou "multiview") não podem ser combinadas com `texture_prompt` ou `style_image`.
- `style_image` exige que um `texture_prompt` seja fornecido.
- Quando nenhum `texture_prompt` é fornecido, o modelo de origem deve vir de uma tarefa text-to-model, image-to-model, multiview-to-model ou texture-model. Modelos sem imagem de origem (modelos importados, segmentados, concluídos ou retopologizados) exigem um `texture_prompt`, porque o Tripo aceita imagens de referência apenas para modelos que ele mesmo gerou.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---------------|-----------|---------------|
| `model task_id` | ID da tarefa da operação de texturização, que pode ser passado para outros nós Tripo. | MODEL_TASK_ID |
| `GLB` | Modelo texturizado no formato GLB. Vazio quando a origem é uma malha quad ou uma importação FBX. | FILE_3D_GLB |
| `FBX` | Modelo texturizado no formato FBX. O Tripo retorna FBX para malhas quad e importações FBX; vazio caso contrário. | FILE_3D_FBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dd9b05e37fcdd29896a50451b92a267862ad94b59abfb8680c8b648390cca091`

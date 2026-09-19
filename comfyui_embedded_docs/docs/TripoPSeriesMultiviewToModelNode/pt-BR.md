# Tripo P2: Multivisualização para Modelo

Gera um modelo 3D low-poly com topologia limpa a partir de várias vistas do mesmo objeto usando o modelo P2 da Tripo. A vista frontal é obrigatória, e de uma a três das vistas esquerda, traseira e direita podem ser adicionadas para melhorar o resultado. O modelo retorna como uma malha triangular (GLB) ou, quando `model.quad` está habilitado, como uma malha com predominância de quads (FBX).

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo Tripo da série P a ser usado. Selecionar um modelo revela suas próprias entradas abaixo. | DYNAMIC_COMBO | Sim | `"P2"` |

### Entradas do P2

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model.image` | Vista frontal (0°) do objeto. | IMAGE | Sim | - |
| `model.image_left` | Vista esquerda (90°), o lado esquerdo do próprio objeto. | IMAGE | Não | - |
| `model.image_back` | Vista traseira (180°). | IMAGE | Não | - |
| `model.image_right` | Vista direita (270°), o lado direito do próprio objeto. | IMAGE | Não | - |
| `quad` | Retorna uma malha com predominância de quads na saída FBX em vez de uma malha triangular na saída GLB (padrão: False). | BOOLEAN | Sim | True/False |
| `face_limit` | Contagem alvo de faces. `-1` permite que a Tripo escolha. Com `model.quad` habilitado, o limite é de 48 a 25.000; caso contrário, de 48 a 50.000 (padrão: -1). | INT | Sim | -1, ou 48 a 50000 |
| `textura` | Resolução da textura de cor base: standard é 2K, detailed é 4K e extreme é 8K. `"none"` retorna uma malha sem textura (padrão: `"standard"`). | COMBO | Sim | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `pbr` | Adiciona mapas de metalicidade, rugosidade e normal à cor base. Ignorado quando `model.texture` é `"none"` (padrão: True). | BOOLEAN | Sim | True/False |
| `model_seed` | Semente para a geometria (padrão: 42). | INT | Sim | 0 a 2147483647 |
| `texture_alignment` | Fazer com que as cores correspondam às das imagens de entrada, ou ajustar as texturas à geometria gerada. Ignorado quando `model.texture` é `"none"` (padrão: `"original_image"`). Configuração avançada. | COMBO | Sim | `"original_image"`<br>`"geometry"` |
| `orientation` | `"align_image"` rotaciona o modelo para o ponto de vista das imagens de entrada. Ignorado quando `model.texture` é `"none"` (padrão: `"default"`). Configuração avançada. | COMBO | Sim | `"default"`<br>`"align_image"` |
| `texture_seed` | Semente para as texturas (padrão: 42). Configuração avançada. | INT | Sim | 0 a 2147483647 |
| `auto_size` | Dimensiona o modelo para seu tamanho real em metros por meio da transformação de cena. Ignorado quando `model.texture` é `"none"` (padrão: False). Configuração avançada. | BOOLEAN | Sim | True/False |
| `export_uv` | Desdobra UV da malha quando ela não tem textura. Malhas texturizadas são sempre desdobradas (padrão: True). Configuração avançada. | BOOLEAN | Sim | True/False |
| `compress_geometry` | Aplica compressão de geometria meshopt: arquivos muito menores, mas a pré-visualização 3D do ComfyUI não consegue exibi-los. Ignorado para malhas de quads (padrão: False). Configuração avançada. | BOOLEAN | Sim | True/False |

**Notas:**

- `model.image` é obrigatório, e pelo menos uma das entradas `model.image_left`, `model.image_back` ou `model.image_right` também precisa estar conectada; o nó gera um erro se a vista frontal for a única imagem.
- Apenas a primeira imagem de cada lote é usada.
- `model.face_limit` é um alvo, e não um limite rígido, então o resultado pode conter mais faces do que o solicitado. `-1` deixa a escolha para a Tripo.
- `model.quad` decide qual saída carrega a malha. Com ele habilitado, o modelo chega na saída FBX e a saída GLB permanece vazia; com ele desabilitado, o modelo chega em GLB e FBX permanece vazio. O nó gera um erro se a saída vazia for a que você conectou.
- `model.texture`, `model.pbr`, `model.texture_seed`, `model.auto_size`, `model.texture_alignment` e `model.orientation` se aplicam apenas a modelos com textura: com `"none"`, o nó não envia configurações de textura e retorna geometria sem textura.
- `model.compress_geometry` não tem efeito sobre malhas de quads.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `model task_id` | O ID de tarefa exclusivo para a solicitação de geração do modelo. | MODEL_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB. Vazio quando `model.quad` está habilitado. | FILE3DGLB |
| `FBX` | O modelo 3D gerado no formato FBX. Só é preenchido quando `model.quad` está habilitado. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesMultiviewToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cea0a65ca001bc8298af9fbe2a83f592abf497987e634b0126482f3d2a18571c`

# Tripo P2: Texto para Modelo

Gera um modelo 3D low-poly com topologia limpa a partir de um prompt de texto usando o modelo P2 da Tripo. O resultado retorna como uma malha triangular (GLB) ou, quando `model.quad` está habilitado, como uma malha com predominância de quads (FBX).

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | Modelo da série P da Tripo a ser usado. Selecionar um modelo revela suas próprias entradas abaixo. | DYNAMIC_COMBO | Sim | `"P2"` |

### Entradas do P2

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `prompt` | Descrição textual do modelo 3D a ser gerado. Não pode ficar vazio, até 1024 caracteres (padrão: vazio). | STRING | Sim | Até 1024 caracteres |
| `negative_prompt` | Descrição textual do que evitar no modelo gerado (padrão: vazio). | STRING | Não | Até 255 caracteres |
| `quad` | Retorna uma malha com predominância de quads na saída FBX em vez de uma malha triangular na saída GLB (padrão: False). | BOOLEAN | Sim | True/False |
| `face_limit` | Contagem alvo de faces. `-1` deixa a Tripo escolher. Com `model.quad` habilitado, o limite é de 48 a 25.000; caso contrário, de 48 a 50.000 (padrão: -1). | INT | Sim | -1, ou 48 a 50000 |
| `textura` | Resolução da textura de cor base: standard é 2K, detailed é 4K e extreme é 8K. `"none"` retorna uma malha sem textura (padrão: `"standard"`). | COMBO | Sim | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `pbr` | Adiciona mapas de metalicidade, rugosidade e normais à cor base. Ignorado quando `model.texture` é `"none"` (padrão: True). | BOOLEAN | Sim | True/False |
| `model_seed` | Semente para a geometria (padrão: 42). | INT | Sim | 0 a 2147483647 |
| `image_seed` | Semente para a imagem que a Tripo gera a partir do prompt antes da modelagem (padrão: 42). Configuração avançada. | INT | Sim | 0 a 2147483647 |
| `texture_seed` | Semente para as texturas (padrão: 42). Configuração avançada. | INT | Sim | 0 a 2147483647 |
| `auto_size` | Dimensiona o modelo para seu tamanho no mundo real em metros por meio da transformação de cena (padrão: False). Configuração avançada. | BOOLEAN | Sim | True/False |
| `export_uv` | Faz o desdobramento UV da malha quando ela não tem textura. Malhas com textura sempre são desdobradas (padrão: True). Configuração avançada. | BOOLEAN | Sim | True/False |
| `compress_geometry` | Aplica compressão de geometria meshopt: arquivos muito menores, mas a pré-visualização 3D do ComfyUI não consegue exibi-los. Ignorado para malhas de quads (padrão: False). Configuração avançada. | BOOLEAN | Sim | True/False |

**Observações:**

- `model.prompt` é obrigatório; `model.negative_prompt` é opcional e limitado a 255 caracteres.
- `model.face_limit` é um alvo, não um limite rígido, então o resultado pode conter mais faces do que o solicitado. `-1` deixa a escolha para a Tripo.
- `model.quad` decide qual saída carrega a malha. Com ele habilitado, o modelo chega à saída FBX e a saída GLB permanece vazia; com ele desabilitado, o modelo chega à saída GLB e a saída FBX permanece vazia. O nó gera um erro se a saída vazia for a que você conectou.
- `model.texture`, `model.pbr`, `model.texture_seed` e `model.auto_size` só se aplicam a modelos com textura: com `"none"`, o nó não envia configurações de textura e retorna geometria sem textura.
- `model.compress_geometry` não tem efeito sobre malhas de quads.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `model task_id` | O ID de tarefa exclusivo para a solicitação de geração do modelo. | MODEL_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB. Vazio quando `model.quad` está habilitado. | FILE3DGLB |
| `FBX` | O modelo 3D gerado no formato FBX. Só é preenchido quando `model.quad` está habilitado. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesTextToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e55596c1a237cf6b92e3bdead4359f380c6cba60992dcc61b5ee4e6b1bdd843b`

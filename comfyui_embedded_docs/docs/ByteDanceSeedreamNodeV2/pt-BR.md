# ByteDance Seedream 4.5 & 5.0 (Legado)

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | A versão do modelo Seedream a ser usada para geração. Cada modelo tem capacidades e preços diferentes. | DYNAMIC_COMBO | Sim | `"seedream 5.0 pro"`<br>`"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `prompt` | Prompt de texto para criar ou editar uma imagem (padrão: string vazia). | STRING | Sim | N/A |
| `semente` | Semente a ser usada para geração (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `marca d'água` | Indica se deve adicionar uma marca d'água "AI generated" à imagem (padrão: False). | BOOLEAN | Sim | True / False |
| `thinking` | Ativa o raciocínio de otimização de prompt do modelo ('thinking') para melhor aderência. Pode aumentar substancialmente o tempo de geração — notavelmente no Seedream 5.0 Pro. Só pode ser desativado para texto-para-imagem (não quando imagens de referência são fornecidas) (padrão: True). | BOOLEAN | Não | True / False |

### Entradas do `seedream 5.0 pro`

| Parâmetro | Descrição | Tipo de dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. | COMBO | Sim | Vários presets específicos do modelo disponíveis, inclui `Custom` |
| `width` | Largura personalizada da imagem. O valor funciona somente se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 3136 (passo 2) |
| `height` | Altura personalizada da imagem. O valor funciona somente se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 2496 (passo 2) |

### Entradas do `seedream 5.0 lite`

| Parâmetro | Descrição | Tipo de dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. | COMBO | Sim | Vários presets específicos do modelo disponíveis, inclui `Custom` |
| `width` | Largura personalizada da imagem. O valor funciona somente se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 6240 (passo 2) |
| `height` | Altura personalizada da imagem. O valor funciona somente se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 4992 (passo 2) |
| `max_images` | Número máximo de imagens a gerar. Com 1, exatamente uma imagem é produzida. Com >1, o modelo gera entre 1 e max_images imagens relacionadas (ex.: cenas de história, variações de personagem). O total de imagens (entrada + geradas) não pode exceder 15. (padrão: 1) | INT | Sim | 1 a 14 |
| `fail_on_partial` | Se ativado, aborta a execução se alguma imagem solicitada estiver ausente ou retornar um erro. (padrão: False) | BOOLEAN | Sim | True / False |

### Entradas do `seedream-4-5-251128`

| Parâmetro | Descrição | Tipo de dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. | COMBO | Sim | Vários presets específicos do modelo disponíveis, inclui `Custom` |
| `width` | Largura personalizada da imagem. O valor funciona somente se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 6240 (passo 2) |
| `height` | Altura personalizada da imagem. O valor funciona somente se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 4992 (passo 2) |
| `max_images` | Número máximo de imagens a gerar. Com 1, exatamente uma imagem é produzida. Com >1, o modelo gera entre 1 e max_images imagens relacionadas (ex.: cenas de história, variações de personagem). O total de imagens (entrada + geradas) não pode exceder 15. (padrão: 1) | INT | Sim | 1 a 10 |
| `fail_on_partial` | Se ativado, aborta a execução se alguma imagem solicitada estiver ausente ou retornar um erro. (padrão: False) | BOOLEAN | Sim | True / False |

### Entradas do `seedream-4-0-250828`

| Parâmetro | Descrição | Tipo de dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. | COMBO | Sim | Vários presets específicos do modelo disponíveis, inclui `Custom` |
| `width` | Largura personalizada da imagem. O valor funciona somente se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 6240 (passo 2) |
| `height` | Altura personalizada da imagem. O valor funciona somente se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 4992 (passo 2) |
| `max_images` | Número máximo de imagens a gerar. Com 1, exatamente uma imagem é produzida. Com >1, o modelo gera entre 1 e max_images imagens relacionadas (ex.: cenas de história, variações de personagem). O total de imagens (entrada + geradas) não pode exceder 15. (padrão: 1) | INT | Sim | 1 a 10 |
| `fail_on_partial` | Se ativado, aborta a execução se alguma imagem solicitada estiver ausente ou retornar um erro. (padrão: False) | BOOLEAN | Sim | True / False |

### Entradas de referência

| Parâmetro | Descrição | Tipo de dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | Slot expansível: conecte 1..N itens (ex.: `image_1`, `image_2`, ...); o limite de quantidade depende do modelo selecionado (consulte as seções do modelo). Imagem(ns) de referência opcional(is) para geração imagem-para-imagem ou com múltiplas referências. Sem imagens de referência, o nó opera no modo texto-para-imagem. | IMAGE | Não | 0 a 10 imagens (`seedream 5.0 pro`, `seedream-4-5-251128`, `seedream-4-0-250828`)<br>0 a 14 imagens (`seedream 5.0 lite`) |

### Notas sobre restrições

- `width` e `height` só têm efeito quando `size_preset` está definido como `Custom`.
- O número total de imagens de referência mais imagens geradas não pode exceder 15.
- `thinking` só pode ser desativado para geração texto-para-imagem, não quando imagens de referência são fornecidas.
- O Seedream 5.0 Pro não oferece suporte à geração em lote: ele sempre produz uma única imagem, então `max_images` e `fail_on_partial` não estão disponíveis para este modelo.

## Saídas

| Nome da saída | Descrição | Tipo de dado |
|-------------|-------------|-----------|
| `image` | A imagem gerada ou editada como um tensor. Se várias imagens foram solicitadas, elas são concatenadas em um único lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f1a84171d94c602ec5417e43857ddf511ab1e54caa089b1928f740d3a38423f8`

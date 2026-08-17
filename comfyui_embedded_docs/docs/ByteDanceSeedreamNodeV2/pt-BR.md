# ByteDance Seedream 4.5 & 5.0

Este nó cria ou edita imagens usando os modelos Seedream da ByteDance (4.0, 4.5, 5.0 Lite e 5.0 Pro). Ele gera novas imagens a partir de um prompt de texto e pode editar imagens existentes com base em imagens de referência e uma instrução de frase única, suportando resoluções de até 4K.

## Entradas

O seletor `model` determina quais entradas específicas do modelo estão disponíveis. As tabelas abaixo listam as entradas comuns, as entradas para cada modelo e os slots expansíveis de imagens de referência.

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | A versão do modelo Seedream a ser usada para geração. Cada modelo possui diferentes capacidades, limites e preços. | DYNAMIC_COMBO | Sim | `"seedream 5.0 pro"`<br>`"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `prompt` | Prompt de texto para criar ou editar uma imagem. | STRING | Sim | Qualquer texto (não vazio) |
| `seed` | Semente para geração (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `watermark` | Se deve adicionar uma marca d'água 'AI generated' à imagem (padrão: False). | BOOLEAN | Sim | True / False |
| `thinking` | Habilite o raciocínio de otimização de prompt do modelo ("thinking") para melhor aderência. Pode aumentar substancialmente o tempo de geração — especialmente no Seedream 5.0 Pro. Só pode ser desativado para texto-para-imagem (não quando imagens de referência são fornecidas). (padrão: True) | BOOLEAN | Não | True / False |

### Entradas do seedream 5.0 pro

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. | COMBO | Sim | Predefinições específicas do modelo (inclui Custom) |
| `width` | Largura personalizada da imagem. O valor só funciona se `size_preset` estiver definido como Custom (padrão: 2048). | INT | Sim | 1024 a 3136 (passo 2) |
| `height` | Altura personalizada da imagem. O valor só funciona se `size_preset` estiver definido como Custom (padrão: 2048). | INT | Sim | 1024 a 2496 (passo 2) |

### Entradas do seedream 5.0 lite

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. | COMBO | Sim | Predefinições específicas do modelo (inclui Custom) |
| `width` | Largura personalizada da imagem. O valor só funciona se `size_preset` estiver definido como Custom (padrão: 2048). | INT | Sim | 1024 a 6240 (passo 2) |
| `height` | Altura personalizada da imagem. O valor só funciona se `size_preset` estiver definido como Custom (padrão: 2048). | INT | Sim | 1024 a 4992 (passo 2) |
| `max_images` | Número máximo de imagens a gerar. Com 1, exatamente uma imagem é produzida. Com >1, o modelo gera entre 1 e max_images imagens relacionadas (ex.: cenas de história, variações de personagem). O total de imagens (entrada + geradas) não pode exceder 15. (padrão: 1) | INT | Sim | 1 a 14 |
| `fail_on_partial` | Se ativado, interrompe a execução se alguma imagem solicitada estiver ausente ou retornar um erro. (padrão: False) | BOOLEAN | Sim | True / False |

### Entradas do seedream-4-5-251128

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. | COMBO | Sim | Predefinições específicas do modelo (inclui Custom) |
| `width` | Largura personalizada da imagem. O valor só funciona se `size_preset` estiver definido como Custom (padrão: 2048). | INT | Sim | 1024 a 6240 (passo 2) |
| `height` | Altura personalizada da imagem. O valor só funciona se `size_preset` estiver definido como Custom (padrão: 2048). | INT | Sim | 1024 a 4992 (passo 2) |
| `max_images` | Número máximo de imagens a gerar. Com 1, exatamente uma imagem é produzida. Com >1, o modelo gera entre 1 e max_images imagens relacionadas (ex.: cenas de história, variações de personagem). O total de imagens (entrada + geradas) não pode exceder 15. (padrão: 1) | INT | Sim | 1 a 10 |
| `fail_on_partial` | Se ativado, interrompe a execução se alguma imagem solicitada estiver ausente ou retornar um erro. (padrão: False) | BOOLEAN | Sim | True / False |

### Entradas do seedream-4-0-250828

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. | COMBO | Sim | Predefinições específicas do modelo (inclui Custom) |
| `width` | Largura personalizada da imagem. O valor só funciona se `size_preset` estiver definido como Custom (padrão: 2048). | INT | Sim | 1024 a 6240 (passo 2) |
| `height` | Altura personalizada da imagem. O valor só funciona se `size_preset` estiver definido como Custom (padrão: 2048). | INT | Sim | 1024 a 4992 (passo 2) |
| `max_images` | Número máximo de imagens a gerar. Com 1, exatamente uma imagem é produzida. Com >1, o modelo gera entre 1 e max_images imagens relacionadas (ex.: cenas de história, variações de personagem). O total de imagens (entrada + geradas) não pode exceder 15. (padrão: 1) | INT | Sim | 1 a 10 |
| `fail_on_partial` | Se ativado, interrompe a execução se alguma imagem solicitada estiver ausente ou retornar um erro. (padrão: False) | BOOLEAN | Sim | True / False |

### Entradas de Referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | Imagem(ns) de referência opcional(is) para geração imagem-para-imagem ou multi-referência. Slot expansível: conecte 1..N itens (`image_1`, `image_2`, ..., `image_N`); o número máximo depende do modelo selecionado (10 para seedream 5.0 pro, seedream-4-5-251128 e seedream-4-0-250828; 14 para seedream 5.0 lite). | IMAGE | Não | 0 a 10<br>0 a 14 (seedream 5.0 lite) |

### Notas

- Os valores personalizados de `width` e `height` só têm efeito quando `size_preset` está definido como Custom.
- Limites de resolução (baseados em largura × altura):
  - seedream 5.0 pro: mínimo 0.92 MP, máximo 4.19 MP.
  - seedream 5.0 lite e seedream-4-5-251128: mínimo 3.68 MP.
  - seedream-4-0-250828: mínimo 0.92 MP.
  - seedream 5.0 lite, seedream-4-5-251128 e seedream-4-0-250828: máximo 16.78 MP.
- As imagens de referência devem ter uma proporção de aspecto entre 1:3 e 3:1.
- Quando `max_images` é maior que 1 (disponível no seedream 5.0 lite, seedream-4-5-251128 e seedream-4-0-250828), o número total de imagens (imagens de referência mais imagens geradas) não pode exceder 15.
- `thinking` só pode ser desativado para texto-para-imagem; ele deve estar ativado quando imagens de referência são fornecidas.
- O seedream 5.0 pro sempre gera uma única imagem e não exibe as entradas `max_images` ou `fail_on_partial`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem gerada ou editada. Se várias imagens forem solicitadas com `max_images`, elas são retornadas concatenadas em um único lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b57e0d85a586aaeb7cf02ceaaddcd2d36cdac20f5251cba48de602a979420f1c`

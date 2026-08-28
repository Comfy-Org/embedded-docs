# ByteDance Seedream 4.5 & 5.0

Este nó gera ou edita imagens usando os modelos Seedream da ByteDance (versões 4.0, 4.5, 5.0 Lite e 5.0 Pro). Ele oferece geração unificada de texto para imagem e edição precisa de imagens por meio de uma única frase, com resolução de até 4K. Esta é a versão legada (V2) do nó Seedream.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `modelo` | A versão do modelo Seedream a ser usada na geração. Cada modelo tem diferentes capacidades e preços. | DYNAMIC_COMBO | Sim | `"seedream 5.0 pro"`<br>`"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `prompt` | Prompt de texto para criar ou editar uma imagem (padrão: string vazia). | STRING | Sim | N/A |
| `semente` | Semente usada na geração (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `marca d'água` | Se deve adicionar uma marca d'água "gerado por IA" à imagem (padrão: False). | BOOLEAN | Sim | True / False |
| `thinking` | Ativa o raciocínio de otimização do prompt do modelo ("thinking") para melhor aderência ao prompt. Pode aumentar substancialmente o tempo de geração — especialmente no Seedream 5.0 Pro. Só pode ser desativado no modo texto para imagem (não quando imagens de referência são fornecidas) (padrão: True). | BOOLEAN | Não | True / False |

### Entradas do `seedream 5.0 pro`

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. | COMBO | Sim | Várias predefinições específicas do modelo disponíveis, incluindo `Custom` |
| `width` | Largura personalizada para a imagem. O valor só funciona se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 3136 (passo 2) |
| `height` | Altura personalizada para a imagem. O valor só funciona se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 2496 (passo 2) |

### Entradas do `seedream 5.0 lite`

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. | COMBO | Sim | Várias predefinições específicas do modelo disponíveis, incluindo `Custom` |
| `width` | Largura personalizada para a imagem. O valor só funciona se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 6240 (passo 2) |
| `height` | Altura personalizada para a imagem. O valor só funciona se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 4992 (passo 2) |
| `max_images` | Número máximo de imagens a gerar. Com 1, exatamente uma imagem é produzida. Com >1, o modelo gera entre 1 e max_images imagens relacionadas (ex.: cenas de história, variações de personagem). O total de imagens (entrada + geradas) não pode exceder 15. (padrão: 1) | INT | Sim | 1 a 14 |
| `fail_on_partial` | Se ativado, interrompe a execução se alguma imagem solicitada estiver ausente ou retornar erro. (padrão: False) | BOOLEAN | Sim | True / False |

### Entradas do `seedream-4-5-251128`

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. | COMBO | Sim | Várias predefinições específicas do modelo disponíveis, incluindo `Custom` |
| `width` | Largura personalizada para a imagem. O valor só funciona se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 6240 (passo 2) |
| `height` | Altura personalizada para a imagem. O valor só funciona se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 4992 (passo 2) |
| `max_images` | Número máximo de imagens a gerar. Com 1, exatamente uma imagem é produzida. Com >1, o modelo gera entre 1 e max_images imagens relacionadas (ex.: cenas de história, variações de personagem). O total de imagens (entrada + geradas) não pode exceder 15. (padrão: 1) | INT | Sim | 1 a 10 |
| `fail_on_partial` | Se ativado, interrompe a execução se alguma imagem solicitada estiver ausente ou retornar erro. (padrão: False) | BOOLEAN | Sim | True / False |

### Entradas do `seedream-4-0-250828`

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. | COMBO | Sim | Várias predefinições específicas do modelo disponíveis, incluindo `Custom` |
| `width` | Largura personalizada para a imagem. O valor só funciona se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 6240 (passo 2) |
| `height` | Altura personalizada para a imagem. O valor só funciona se `size_preset` estiver definido como `Custom` (padrão: 2048). | INT | Sim | 1024 a 4992 (passo 2) |
| `max_images` | Número máximo de imagens a gerar. Com 1, exatamente uma imagem é produzida. Com >1, o modelo gera entre 1 e max_images imagens relacionadas (ex.: cenas de história, variações de personagem). O total de imagens (entrada + geradas) não pode exceder 15. (padrão: 1) | INT | Sim | 1 a 10 |
| `fail_on_partial` | Se ativado, interrompe a execução se alguma imagem solicitada estiver ausente ou retornar erro. (padrão: False) | BOOLEAN | Sim | True / False |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `images` | Slot expansível: conecte de 1 a N itens (ex.: `image_1`, `image_2`, ...); o limite de contagem depende do modelo selecionado (veja as seções dos modelos). Uma ou mais imagens de referência opcionais para geração de imagem para imagem ou com múltiplas referências. Sem imagens de referência, o nó funciona no modo texto para imagem. | IMAGE | Não | 0 a 10 imagens (`seedream 5.0 pro`, `seedream-4-5-251128`, `seedream-4-0-250828`)<br>0 a 14 imagens (`seedream 5.0 lite`) |

### Notas sobre restrições

- `width` e `height` só têm efeito quando `size_preset` está definido como `Custom`.
- O número total de imagens de referência mais as imagens geradas não pode exceder 15.
- `thinking` só pode ser desativado para geração de texto para imagem, não quando imagens de referência são fornecidas.
- O Seedream 5.0 Pro não suporta geração em lote: ele sempre produz uma única imagem, portanto `max_images` e `fail_on_partial` não estão disponíveis para este modelo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem gerada ou editada como um tensor. Se várias imagens forem solicitadas, elas são concatenadas em um único lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f1a84171d94c602ec5417e43857ddf511ab1e54caa089b1928f740d3a38423f8`

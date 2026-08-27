# ByteDanceSeedreamNodeV3

O ByteDance Seedream 4.5 & 5.0 gera imagens a partir de um prompt de texto (texto para imagem) ou gera/edita imagens guiadas por imagens de referência opcionais, usando os modelos ByteDance Seedream 4.0, 4.5 e 5.0 em resolução de até 4K. O nó envia o prompt e quaisquer imagens de referência para a API da ByteDance, aguarda a conclusão da tarefa de geração e retorna o tensor ou os tensores de imagem resultantes.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para criar ou editar uma imagem. Não pode ficar vazio após a remoção de espaços em branco. | STRING | Sim | Texto de múltiplas linhas |
| `model` | Seleciona o modelo Seedream a ser usado. Cada modelo expõe seu próprio conjunto de subparâmetros e limites nas seções abaixo. | DYNAMIC_COMBO | Sim | "seedream 5.0 pro"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |

### Entradas do Seedream 5.0 Pro (seedream 5.0 pro)

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. Padrão: primeira predefinição recomendada para este modelo. | COMBO | Não | Predefinições de tamanho recomendadas específicas do modelo<br>"Custom" |
| `width` | Largura personalizada da imagem. O valor só é aplicado se `size_preset` estiver definido como `Custom`. Padrão: 2048. | INT | Não | 1024 a 3136 (passo 2) |
| `height` | Altura personalizada da imagem. O valor só é aplicado se `size_preset` estiver definido como `Custom`. Padrão: 2048. | INT | Não | 1024 a 2496 (passo 2) |
| `prompt_optimization` | Modo de otimização do prompt quando imagens de referência são fornecidas: 'standard' oferece maior qualidade, 'fast' menor tempo de geração. Padrão: "standard". | COMBO | Não | "standard"<br>"fast" |
| `seed` | Semente a ser usada na geração. Padrão: 42. | INT | Não | 0 a 2147483647 |
| `watermark` | Se deve adicionar uma marca d'água "gerado por IA" à imagem. Padrão: false. | BOOLEAN | Não | true / false |
| `thinking` | Ativa o raciocínio de otimização do prompt do modelo ('thinking') para melhor aderência. Pode aumentar substancialmente o tempo de geração — especialmente no Seedream 5.0 Pro. Só pode ser desativado para geração de texto para imagem (não quando imagens de referência são fornecidas). Padrão: true. | BOOLEAN | Não | true / false |

### Entradas do Seedream 5.0 Lite (seedream 5.0 lite)

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. Padrão: primeira predefinição recomendada para este modelo. | COMBO | Não | Predefinições de tamanho recomendadas específicas do modelo<br>"Custom" |
| `width` | Largura personalizada da imagem. O valor só é aplicado se `size_preset` estiver definido como `Custom`. Padrão: 2048. | INT | Não | 1024 a 6240 (passo 2) |
| `height` | Altura personalizada da imagem. O valor só é aplicado se `size_preset` estiver definido como `Custom`. Padrão: 2048. | INT | Não | 1024 a 4992 (passo 2) |
| `max_images` | Número máximo de imagens a gerar. Com 1, exatamente uma imagem é produzida. Com mais de 1, o modelo gera entre 1 e max_images imagens relacionadas (ex.: cenas de história, variações de personagem). O total de imagens (entrada + geradas) não pode exceder 15. Padrão: 1. | INT | Não | 1 a 14 |
| `fail_on_partial` | Se ativado, aborta a execução se alguma imagem solicitada estiver ausente ou retornar erro. Padrão: false. | BOOLEAN | Não | true / false |
| `seed` | Semente a ser usada na geração. Padrão: 42. | INT | Não | 0 a 2147483647 |
| `watermark` | Se deve adicionar uma marca d'água "gerado por IA" à imagem. Padrão: false. | BOOLEAN | Não | true / false |
| `thinking` | Ativa o raciocínio de otimização do prompt do modelo ('thinking') para melhor aderência. Pode aumentar substancialmente o tempo de geração — especialmente no Seedream 5.0 Pro. Só pode ser desativado para geração de texto para imagem (não quando imagens de referência são fornecidas). Padrão: true. | BOOLEAN | Não | true / false |

### Entradas do Seedream 4.5 (seedream-4-5-251128)

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. Padrão: primeira predefinição recomendada para este modelo. | COMBO | Não | Predefinições de tamanho recomendadas específicas do modelo<br>"Custom" |
| `width` | Largura personalizada da imagem. O valor só é aplicado se `size_preset` estiver definido como `Custom`. Padrão: 2048. | INT | Não | 1024 a 6240 (passo 2) |
| `height` | Altura personalizada da imagem. O valor só é aplicado se `size_preset` estiver definido como `Custom`. Padrão: 2048. | INT | Não | 1024 a 4992 (passo 2) |
| `max_images` | Número máximo de imagens a gerar. Com 1, exatamente uma imagem é produzida. Com mais de 1, o modelo gera entre 1 e max_images imagens relacionadas (ex.: cenas de história, variações de personagem). O total de imagens (entrada + geradas) não pode exceder 15. Padrão: 1. | INT | Não | 1 a 10 |
| `fail_on_partial` | Se ativado, aborta a execução se alguma imagem solicitada estiver ausente ou retornar erro. Padrão: false. | BOOLEAN | Não | true / false |
| `seed` | Semente a ser usada na geração. Padrão: 42. | INT | Não | 0 a 2147483647 |
| `watermark` | Se deve adicionar uma marca d'água "gerado por IA" à imagem. Padrão: false. | BOOLEAN | Não | true / false |
| `thinking` | Ativa o raciocínio de otimização do prompt do modelo ('thinking') para melhor aderência. Pode aumentar substancialmente o tempo de geração — especialmente no Seedream 5.0 Pro. Só pode ser desativado para geração de texto para imagem (não quando imagens de referência são fornecidas). Padrão: true. | BOOLEAN | Não | true / false |

### Entradas do Seedream 4.0 (seedream-4-0-250828)

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Escolha um tamanho recomendado. Selecione Custom para usar a largura e a altura abaixo. Padrão: primeira predefinição recomendada para este modelo. | COMBO | Não | Predefinições de tamanho recomendadas específicas do modelo<br>"Custom" |
| `width` | Largura personalizada da imagem. O valor só é aplicado se `size_preset` estiver definido como `Custom`. Padrão: 2048. | INT | Não | 1024 a 6240 (passo 2) |
| `height` | Altura personalizada da imagem. O valor só é aplicado se `size_preset` estiver definido como `Custom`. Padrão: 2048. | INT | Não | 1024 a 4992 (passo 2) |
| `max_images` | Número máximo de imagens a gerar. Com 1, exatamente uma imagem é produzida. Com mais de 1, o modelo gera entre 1 e max_images imagens relacionadas (ex.: cenas de história, variações de personagem). O total de imagens (entrada + geradas) não pode exceder 15. Padrão: 1. | INT | Não | 1 a 10 |
| `fail_on_partial` | Se ativado, aborta a execução se alguma imagem solicitada estiver ausente ou retornar erro. Padrão: false. | BOOLEAN | Não | true / false |
| `seed` | Semente a ser usada na geração. Padrão: 42. | INT | Não | 0 a 2147483647 |
| `watermark` | Se deve adicionar uma marca d'água "gerado por IA" à imagem. Padrão: false. | BOOLEAN | Não | true / false |
| `thinking` | Ativa o raciocínio de otimização do prompt do modelo ('thinking') para melhor aderência. Pode aumentar substancialmente o tempo de geração — especialmente no Seedream 5.0 Pro. Só pode ser desativado para geração de texto para imagem (não quando imagens de referência são fornecidas). Padrão: true. | BOOLEAN | Não | true / false |

### Entradas de Referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `images` | Slot expansível: imagem(ns) de referência opcional(is) para geração de imagem para imagem ou com múltiplas referências. Conecte de 1 a N imagens (por exemplo, `image_1`, `image_2`, ...); o limite de contagem é por modelo (consulte as notas abaixo). Se uma imagem conectada contiver um lote de imagens, cada imagem do lote conta para o limite. | IMAGE | Não | 0 a 10 (Seedream 5.0 Pro, Seedream 4.5, Seedream 4.0)<br>0 a 14 (Seedream 5.0 Lite) |

**Notas:**

- O `prompt` não pode ficar vazio após a remoção de espaços em branco.
- Número máximo de imagens de referência: 10 para Seedream 5.0 Pro, Seedream 4.5 e Seedream 4.0; 14 para Seedream 5.0 Lite.
- Cada imagem de referência deve ter uma proporção de aspecto entre 1:3 e 3:1.
- Quando `max_images` for maior que 1 (não disponível no Seedream 5.0 Pro), o número total de imagens de referência mais as imagens geradas não pode exceder 15.
- `thinking` só pode ser desativado para geração de texto para imagem. Quando imagens de referência são fornecidas, `thinking` deve estar ativado.
- `width` e `height` são usados somente quando `size_preset` está definido como "Custom".
- `prompt_optimization` está disponível somente no Seedream 5.0 Pro.
- `max_images` e `fail_on_partial` estão disponíveis somente no Seedream 5.0 Lite, Seedream 4.5 e Seedream 4.0; o Seedream 5.0 Pro sempre solicita uma única imagem.
- Requisitos de resolução (largura x altura):
  - Seedream 5.0 Pro: entre 0,92 MP (921.600 pixels) e 4,19 MP (4.194.304 pixels).
  - Seedream 5.0 Lite e Seedream 4.5: pelo menos 3,68 MP (3.686.400 pixels).
  - Seedream 4.0: pelo menos 0,92 MP (921.600 pixels).
  - Todos os modelos não Pro: no máximo 16,78 MP (16.777.216 pixels).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | O tensor de imagem gerado. Quando várias imagens são geradas, elas são concatenadas em um único tensor IMAGE em lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `68dd23afdb5720491cef784b22ad66ff0baf80984ea652ea4c13e6c264c029ac`

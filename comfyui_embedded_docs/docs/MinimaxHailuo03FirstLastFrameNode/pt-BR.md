# MiniMax H3 Primeiro-Último-Frame para Vídeo

Este nó gera um vídeo a partir de uma imagem de primeiro quadro e, opcionalmente, de uma imagem de último quadro usando os modelos MiniMax H3. O seletor `model` altera quais configurações e restrições de geração se aplicam, e a proporção de aspecto do vídeo gerado segue as imagens fornecidas.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado para geração de vídeo. Selecionar um modelo revela suas configurações específicas do modelo abaixo. | DYNAMIC_COMBO | Sim | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `first_frame` | Imagem do primeiro quadro do vídeo. O vídeo gerado segue a proporção de aspecto desta imagem. | IMAGE | Sim | - |
| `last_frame` | Imagem opcional do último quadro do vídeo. Quando fornecida, o vídeo é gerado a partir do primeiro quadro em direção a este último quadro. | IMAGE | Não | - |
| `seed` | Semente aleatória. A mesma solicitação com a mesma semente fornece resultados semelhantes, mas não necessariamente idênticos. Inclui uma opção "control after generate". Padrão: 42. | INT | Sim | 0 a 4294967295 |
| `watermark` | Se deve adicionar uma marca d'água AIGC ao vídeo. Este é um parâmetro avançado. Suportado apenas pelo modelo `MiniMax H3`. Padrão: False. | BOOLEAN | Sim | True<br>False |

### Entradas do MiniMax H3

Estas configurações são exibidas quando `MiniMax H3` é selecionado no seletor `model`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. Deve conter pelo menos um caractere que não seja espaço em branco. | STRING | Sim | Texto multilinha |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | "768P"<br>"2K" |
| `duration` | Duração do vídeo de saída em segundos. Padrão: 5. | INT | Sim | 4 a 15 |

### Entradas do MiniMax H3 Max e do MiniMax H3 Max Turbo

Estas configurações são compartilhadas por `MiniMax H3 Max` e `MiniMax H3 Max Turbo`. Selecionar qualquer um dos modelos revela as mesmas configurações.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. Não deve estar vazio nem conter apenas espaços em branco, e é limitado a 50.000 caracteres. | STRING | Sim | Texto multilinha |
| `resolution` | Resolução do vídeo de saída. Padrão: 768P. | COMBO | Sim | "480P"<br>"768P" |
| `duration` | Duração do vídeo de saída em segundos. Padrão: 5. | INT | Sim | 5 a 15 |
| `prompt_expansion_mode` | Quanto esforço é gasto reescrevendo o prompt antes da geração. Padrão: balanced. | COMBO | Sim | "balanced"<br>"quality" |

**Notas sobre restrições:**

- O prompt deve conter texto: prompts vazios ou contendo apenas espaços em branco são rejeitados.
- Qualquer imagem de quadro fornecida deve ter pelo menos 256 pixels de largura e 256 pixels de altura, com uma proporção de aspecto entre largura e altura entre 0,4 e 2,5 (aproximadamente 2:5 a 5:2). Este requisito se aplica a `first_frame` e, quando fornecido, a `last_frame`.
- Quando `last_frame` é omitido, o vídeo é gerado apenas a partir do primeiro quadro.
- O vídeo de saída segue a proporção de aspecto das imagens fornecidas.
- `watermark` é suportado apenas pelo `MiniMax H3`. Habilitá-lo com `MiniMax H3 Max` ou `MiniMax H3 Max Turbo` gera um erro.
- A duração varia de 4 a 15 segundos para `MiniMax H3` e de 5 a 15 segundos para `MiniMax H3 Max` e `MiniMax H3 Max Turbo`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo gerado criado a partir do primeiro quadro e do último quadro opcional usando o modelo MiniMax H3 selecionado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6eaf895e6e9e46b9a1efb1dd13e951040e12e865cc73d7741ab7546f5f8f9ec0`

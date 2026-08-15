# QwenImageEditApi

Este nó usa os modelos Qwen-Image 3.0 para editar ou combinar até 3 imagens de referência guiadas por um prompt de texto. Você fornece o prompt de texto e as imagens de referência, e o nó retorna o resultado gerado como uma ou mais imagens.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado. Essa seleção também inclui o prompt de texto, até 3 entradas de imagens de referência e um prompt negativo opcional. | MODEL | Sim | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `size` | Resolução de saída. "match input" reutiliza o tamanho da primeira imagem de referência, "auto" permite que o modelo escolha um tamanho com a mesma proporção, "custom" define largura e altura explícitas. | COMBO | Sim | "match input"<br>"auto"<br>"custom" |
| `n` | Número de imagens a gerar, retornadas em lote. (padrão: 1) | INT | Não | 1 a 6 |
| `seed` | Semente a ser usada para a geração. (padrão: 42) | INT | Não | 0 a 2147483647 |
| `prompt_extend` | Se deve aprimorar o prompt com assistência de IA. (padrão: True) | BOOLEAN | Não | True<br>False |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado. (padrão: False) | BOOLEAN | Não | True<br>False |

### Entradas de qwen-image-3.0-pro e qwen-image-3.0

Ambos os modelos compartilham os mesmos subparâmetros.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Instruções de edição. Suporta inglês e chinês, e referências no estilo @Image1 às imagens de entrada. (padrão: "") | STRING | Sim | - |
| `negative_prompt` | Prompt negativo que descreve o que evitar. (padrão: "") | STRING | Não | - |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `images` | Slot expansível: conecte de 1 a 3 imagens de referência (`image_1`, `image_2`, `image_3`). Consulte-as no prompt como @Image1, @Image2, @Image3, numeradas na ordem de entrada; uma entrada em lote é contada uma vez por imagem. | IMAGE | Sim | 1 a 3 |

### Entradas de tamanho personalizado

Exibidas quando `size` é definido como "custom".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `width` | Largura de saída. A área total de pixels deve estar entre 512x512 e 2560x2560; a proporção deve estar entre 1:8 e 8:1. (padrão: 1024) | INT | Sim (quando `size` é "custom") | 256 a 2560, passo 16 |
| `height` | Altura de saída. A área total de pixels deve estar entre 512x512 e 2560x2560; a proporção deve estar entre 1:8 e 8:1. (padrão: 1024) | INT | Sim (quando `size` é "custom") | 256 a 2560, passo 16 |

### Restrições

- O prompt de texto é obrigatório e deve conter pelo menos um caractere.
- Há suporte para no máximo 3 imagens de referência; um erro é gerado se mais forem fornecidas (uma entrada em lote é contada uma vez por imagem).
- Quando `size` está definido como "custom", valores explícitos de largura e altura devem ser fornecidos e são validados: a área total de pixels deve estar entre 262.144 (512x512) e 6.553.600 (2560x2560) pixels, e a proporção deve estar entre 1:8 e 8:1.
- Quando `size` está definido como "match input", pelo menos uma imagem de referência é obrigatória, pois as dimensões da primeira imagem de referência são usadas; as dimensões são redimensionadas para se ajustarem à área e à faixa de proporção suportadas.
- Quando `size` está definido como "auto", o modelo escolhe o tamanho de saída preservando a proporção de entrada.
- As referências do prompt usam @Image1, @Image2, @Image3, numeradas na ordem de entrada; uma referência a um índice maior que o número de imagens conectadas gera um erro. As tags são reconhecidas apenas em limites de palavras, portanto endereços como user@image1.com não são alterados.
- As imagens de referência de entrada são reduzidas para no máximo 2048x2048 pixels antes de serem enviadas à API.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem ou as imagens geradas, retornadas em lote. Até `n` imagens são retornadas. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`

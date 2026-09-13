# Qwen Image 3 Edit

Este nó usa os modelos Qwen-Image 3.0 para editar ou combinar até 3 imagens de referência guiadas por um prompt de texto. Você seleciona um modelo, fornece o prompt e as imagens de referência, e o nó retorna uma ou mais imagens geradas.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar. Esta seleção também inclui o prompt de texto, até 3 entradas de imagem de referência e um prompt negativo opcional. | DYNAMIC_COMBO | Sim | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `size` | Resolução de saída. "match input" reutiliza o tamanho da primeira imagem de referência, "auto" permite que o modelo escolha um tamanho com a mesma proporção de aspecto, "custom" define uma largura e altura explícitas. | DYNAMIC_COMBO | Sim | "match input"<br>"auto"<br>"custom" |
| `n` | Número de imagens a gerar, retornadas como um lote. (padrão: 1) | INT | Não | 1 a 6 |
| `seed` | Semente a usar para geração. (padrão: 42) | INT | Não | 0 a 2147483647 |
| `prompt_extend` | Se deve aprimorar o prompt com assistência de IA. (padrão: True) | BOOLEAN | Não | True<br>False |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado. (padrão: False) | BOOLEAN | Não | True<br>False |

### Entradas do qwen-image-3.0-pro e qwen-image-3.0

Ambos os modelos compartilham os mesmos subparâmetros.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Instruções de edição. Suporta inglês e chinês, e referências no estilo @Image1 às imagens de entrada. (padrão: "") | STRING | Sim | - |
| `negative_prompt` | Prompt negativo descrevendo o que evitar. (padrão: "") | STRING | Não | - |

### Entradas de referência

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | Slot expansível: conecte de 1 a 3 imagens de referência (`image_1`, `image_2`, `image_3`). Consulte-as no prompt como @Image1, @Image2, @Image3, numeradas na ordem de entrada; uma entrada em lote conta uma vez por imagem. | IMAGE | Sim | 1 a 3 |

### Entradas de tamanho personalizado

Exibidas quando `size` está definido como "custom".

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `width` | Largura de saída. A área total de pixels deve estar entre 512x512 e 2560x2560; qualquer proporção de aspecto dentro dessa área funciona. (padrão: 1024) | INT | Sim (quando `size` é "custom") | 256 a 2560, passo 16 |
| `height` | Altura de saída. A área total de pixels deve estar entre 512x512 e 2560x2560; qualquer proporção de aspecto dentro dessa área funciona. (padrão: 1024) | INT | Sim (quando `size` é "custom") | 256 a 2560, passo 16 |

### Restrições

- O prompt de texto é obrigatório e deve conter pelo menos um caractere.
- No máximo 3 imagens de referência são suportadas; um erro é gerado se mais forem fornecidas (uma entrada em lote conta uma vez por imagem).
- Quando `size` está definido como "custom", valores explícitos de largura e altura devem ser fornecidos e são validados: a área total de pixels deve estar entre 262.144 (512x512) e 6.553.600 (2560x2560) pixels, e a proporção de aspecto deve estar entre 1:8 e 8:1.
- Quando `size` está definido como "match input", pelo menos uma imagem de referência é necessária porque as dimensões da primeira imagem de referência são usadas; as dimensões são redimensionadas para se ajustarem à área suportada e à faixa de proporção de aspecto.
- Quando `size` está definido como "auto", o modelo escolhe o tamanho de saída (1,9-4,2 megapixels) preservando a proporção de aspecto da entrada.
- As referências no prompt usam @Image1, @Image2, @Image3, numeradas na ordem de entrada; uma referência a um índice maior que o número de imagens conectadas gera um erro. As tags são reconhecidas apenas em limites de palavra, então endereços como user@image1.com são deixados inalterados.
- As imagens de referência de entrada são reduzidas para no máximo 2048x2048 pixels antes de serem enviadas à API. Se a codificação PNG exceder o limite de tamanho da API, uma codificação JPEG será usada em vez disso.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem ou imagens geradas retornadas como um lote. Até `n` imagens são retornadas. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`

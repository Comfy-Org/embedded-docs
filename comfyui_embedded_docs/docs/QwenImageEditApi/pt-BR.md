# QwenImageEditApi

Este nó usa os modelos Qwen-Image 3.0 para editar ou combinar até 3 imagens de referência guiadas por um prompt de texto. Você fornece o prompt de texto e as imagens de referência, e o nó retorna o resultado gerado como uma ou mais imagens.
## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `model` | Modelo a ser usado. Essa seleção também inclui o prompt de texto, até 3 entradas de imagens de referência e um prompt negativo opcional. | DYNAMIC_COMBO | Sim | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `size` | Resolução de saída. "match input" reutiliza o tamanho da primeira imagem de referência, "auto" permite que o modelo escolha um tamanho com a mesma proporção, "custom" define largura e altura explícitas. | DYNAMIC_COMBO | Sim | "match input"<br>"auto"<br>"custom" |
| `n` | Número de imagens a gerar, retornadas em lote. (padrão: 1) | INT | Não | 1 to 6 |
| `seed` | Semente a ser usada para a geração. (padrão: 42) | INT | Não | 0 to 2147483647 |
| `prompt_extend` | Se deve aprimorar o prompt com assistência de IA. (padrão: True) | BOOLEAN | Não | True<br>False |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado. (padrão: False) | BOOLEAN | Não | True<br>False |

### Entradas de qwen-image-3.0-pro e qwen-image-3.0

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `prompt` | Instruções de edição. Suporta inglês e chinês, e referências no estilo @Image1 às imagens de entrada. (padrão: "") | STRING | Sim | - |
| `negative_prompt` | Prompt negativo que descreve o que evitar. (padrão: "") | STRING | Não | - |

### Entradas de referência

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `images` | Slot expansível: conecte de 1 a 3 imagens de referência (`image_1`, `image_2`, `image_3`). Consulte-as no prompt como @Image1, @Image2, @Image3, numeradas na ordem de entrada; uma entrada em lote é contada uma vez por imagem. | IMAGE | Sim | 1 to 3 |

### Entradas de tamanho personalizado

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `width` | Largura de saída. A área total de pixels deve estar entre 512x512 e 2560x2560; a proporção deve estar entre 1:8 e 8:1. (padrão: 1024) | INT | Não | 256 to 2560, step 16 |
| `height` | Altura de saída. A área total de pixels deve estar entre 512x512 e 2560x2560; a proporção deve estar entre 1:8 e 8:1. (padrão: 1024) | INT | Não | 256 to 2560, step 16 |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---|---|---|
| `IMAGE` | The generated image or images returned as a batch. Up to `n` images are returned. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`

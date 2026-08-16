# QwenImageTextToImageApi

Qwen Image 3 Text to Image gera uma ou mais imagens a partir de um prompt de texto usando os modelos Qwen-Image 3.0. Você seleciona um modelo e fornece um prompt, e o nó retorna as imagens geradas como um lote.
## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `model` | Modelo a ser usado (padrão: "qwen-image-3.0-pro"). Este seletor composto também fornece o prompt, a largura da imagem, a altura da imagem e o prompt negativo opcional. | DYNAMIC_COMBO | Sim | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | Número de imagens a gerar, retornadas como um lote (padrão: 1). | INT | Não | 1 to 6 |
| `seed` | Semente a ser usada para a geração (padrão: 42). Pode ser configurada para atualizar automaticamente após cada geração. | INT | Não | 0 to 2147483647 |
| `prompt_extend` | Se deve aprimorar o prompt com assistência de IA (padrão: true). Opção avançada. | BOOLEAN | Não | true<br>false |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: false). Opção avançada. | BOOLEAN | Não | true<br>false |

### Entradas do qwen-image-3.0-pro e qwen-image-3.0

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `prompt` | Prompt descrevendo a imagem. Suporta inglês e chinês. Deve conter pelo menos 1 caractere. | STRING | Sim | Free text |
| `negative_prompt` | Prompt negativo descrevendo o que evitar (padrão: ""). | STRING | Não | Free text |
| `width` | A área total de pixels deve estar entre 512x512 e 2560x2560; a proporção de aspecto deve estar entre 1:8 e 8:1. (padrão: 1024) | INT | Não | 256 to 2560 (step 16) |
| `height` | A área total de pixels deve estar entre 512x512 e 2560x2560; a proporção de aspecto deve estar entre 1:8 e 8:1. (padrão: 1024) | INT | Não | 256 to 2560 (step 16) |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---|---|---|
| `image` | The generated image or images, returned as a batch. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`

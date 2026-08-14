# QwenImageTextToImageApi

Qwen Image 3 Text to Image gera uma ou mais imagens a partir de um prompt de texto usando os modelos Qwen-Image 3.0. Você seleciona um modelo e fornece um prompt, e o nó retorna as imagens geradas como um lote.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar (padrão: "qwen-image-3.0-pro"). Este seletor composto também fornece o prompt, a largura da imagem, a altura da imagem e o prompt negativo opcional. | MODEL | Sim | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | Número de imagens a gerar, retornadas como um lote (padrão: 1). | INT | Não | 1 a 6 |
| `seed` | Semente a usar para a geração (padrão: 42). Pode ser configurada para atualizar automaticamente após cada geração. | INT | Não | 0 a 2147483647 |
| `prompt_extend` | Se deve aprimorar o prompt com assistência de IA (padrão: true). Opção avançada. | BOOLEAN | Não | true<br>false |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: false). Opção avançada. | BOOLEAN | Não | true<br>false |

Nota: A entrada `model` é um seletor composto com os seguintes subcampos: `model` (ID do modelo), `prompt` (o prompt de texto, que deve conter pelo menos 1 caractere), `width` e `height` (dimensões da imagem, validadas pelo nó) e `negative_prompt` (prompt negativo opcional).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem ou imagens geradas, retornadas como um lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`

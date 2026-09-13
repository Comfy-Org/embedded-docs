# Qwen Image 3 Text to Image

Qwen Image 3 Text to Image gera uma ou mais imagens a partir de um prompt de texto usando os modelos Qwen-Image 3.0. Você seleciona um modelo e fornece um prompt, e o nó retorna as imagens geradas como um lote.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado (padrão: "qwen-image-3.0-pro"). Este seletor composto também fornece o prompt, o prompt negativo, a largura e a altura da imagem. | DYNAMIC_COMBO | Sim | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | Número de imagens a serem geradas, retornadas como um lote (padrão: 1). | INT | Não | 1 a 6 |
| `seed` | Seed a ser usado para a geração (padrão: 42). Pode ser configurado para atualizar automaticamente após cada geração. | INT | Não | 0 a 2147483647 |
| `prompt_extend` | Se deve aprimorar o prompt com assistência de IA (padrão: true). Opção avançada. | BOOLEAN | Não | true<br>false |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: false). Opção avançada. | BOOLEAN | Não | true<br>false |

### Entradas de qwen-image-3.0-pro e qwen-image-3.0

Compartilhadas por qwen-image-3.0-pro e qwen-image-3.0.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt que descreve a imagem. Suporta inglês e chinês. Deve conter pelo menos 1 caractere. | STRING | Sim | Texto livre |
| `negative_prompt` | Prompt negativo que descreve o que evitar (padrão: ""). | STRING | Não | Texto livre |
| `width` | A área total em pixels deve estar entre 512x512 e 2560x2560; qualquer proporção dentro dessa área funciona. (padrão: 1024) | INT | Não | 256 a 2560 (passo 16) |
| `height` | A área total em pixels deve estar entre 512x512 e 2560x2560; qualquer proporção dentro dessa área funciona. (padrão: 1024) | INT | Não | 256 a 2560 (passo 16) |

Observação: A entrada `model` é um seletor composto com os subcampos `model` (ID do modelo), `prompt` (obrigatório, deve conter pelo menos 1 caractere), `negative_prompt` (opcional), `width` e `height`. A área combinada em pixels de `width` e `height` deve estar entre 262.144 pixels (512x512) e 6.553.600 pixels (2560x2560), e a proporção deve permanecer entre 1:8 e 8:1.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `image` | A imagem ou as imagens geradas, retornadas como um lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`

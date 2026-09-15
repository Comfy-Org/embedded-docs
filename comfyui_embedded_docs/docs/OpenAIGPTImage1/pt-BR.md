# OpenAI GPT Image 2

Gera imagens de forma síncrona por meio do endpoint GPT Image da OpenAI. Ele pode criar novas imagens a partir de um prompt de texto ou editar imagens existentes quando uma imagem de entrada e uma máscara opcional são fornecidas. O nó oferece suporte aos modelos `gpt-image-1`, `gpt-image-1.5` e `gpt-image-2` e está marcado como obsoleto.

## Entradas

| Parâmetro | Descrição | Tipo de dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para o GPT Image (padrão: "") | STRING | Sim | - |
| `seed` | Semente aleatória para geração; ainda não implementada no backend (padrão: 0) | INT | Não | 0 a 2147483647 |
| `qualidade` | Qualidade da imagem; afeta o custo e o tempo de geração (padrão: "low") | COMBO | Não | "low"<br>"medium"<br>"high" |
| `fundo` | Retorna a imagem com ou sem fundo (padrão: "auto") | COMBO | Não | "auto"<br>"opaque"<br>"transparent" |
| `tamanho` | Tamanho da imagem. Selecione "Custom" para usar a largura e a altura personalizadas (somente GPT Image 2) (padrão: "auto") | COMBO | Não | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `n` | Quantidade de imagens a gerar (padrão: 1) | INT | Não | 1 a 8 |
| `imagem` | Imagem de referência opcional para edição de imagem | IMAGE | Não | - |
| `mask` | Máscara opcional para inpainting (áreas brancas serão substituídas) | MASK | Não | - |
| `modelo` | Modelo GPT Image a usar (padrão: "gpt-image-2") | COMBO | Não | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `custom_width` | Usado apenas quando `size` for "Custom". Deve ser um múltiplo de 16 (somente GPT Image 2) (padrão: 1024) | INT | Não | 1024 a 3840, passo 16 |
| `custom_height` | Usado apenas quando `size` for "Custom". Deve ser um múltiplo de 16 (somente GPT Image 2) (padrão: 1024) | INT | Não | 1024 a 3840, passo 16 |

**Restrições dos parâmetros:**

- Quando `image` é fornecido, o nó usa o endpoint de edição de imagem.
- O parâmetro `mask` só pode ser usado quando `image` é fornecido.
- Ao usar `mask`, apenas imagens individuais são suportadas (o tamanho do lote deve ser 1).
- `mask` e `image` devem ter o mesmo tamanho.
- Resolução personalizada (`size` = "Custom") só é suportada pelo modelo `gpt-image-2`.
- A largura e a altura personalizadas devem ser múltiplos de 16.
- O lado mais longo de uma resolução personalizada deve ser 3840 ou menor.
- A proporção de aspecto de uma resolução personalizada não deve exceder 3:1.
- O total de pixels de uma resolução personalizada deve estar entre 655.360 e 8.294.400.
- Fundo transparente não é suportado pelo modelo `gpt-image-2`.
- Os modelos `gpt-image-1` e `gpt-image-1.5` só suportam os tamanhos `auto`, `1024x1024`, `1024x1536` e `1536x1024`. Outros tamanhos só são suportados pelo modelo `gpt-image-2`.

## Saídas

| Nome da saída | Descrição | Tipo de dado |
|-------------|-------------|-----------|
| `IMAGE` | Imagem(ns) gerada(s) ou editada(s). Várias imagens são retornadas como um lote; se as imagens retornadas tiverem dimensões diferentes, elas são redimensionadas para corresponder à primeira imagem. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bf588bffced6e66536b4cb54655ef6ebb9cf988d9739e3c379a8ebda1486e20a`

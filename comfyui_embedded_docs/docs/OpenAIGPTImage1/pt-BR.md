> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/pt-BR.md)

Gera imagens de forma síncrona por meio do endpoint GPT Image da OpenAI. Este nó pode criar novas imagens a partir de prompts de texto ou editar imagens existentes quando uma imagem de entrada e uma máscara opcional são fornecidas. Ele suporta vários modelos GPT Image, incluindo gpt-image-1, gpt-image-1.5 e gpt-image-2.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | - | Prompt de texto para o GPT Image (padrão: "") |
| `seed` | INT | Não | 0 a 2147483647 | Semente aleatória para geração (padrão: 0) - ainda não implementada no backend |
| `quality` | COMBO | Não | "low"<br>"medium"<br>"high" | Qualidade da imagem, afeta o custo e o tempo de geração (padrão: "low") |
| `background` | COMBO | Não | "auto"<br>"opaque"<br>"transparent" | Retorna a imagem com ou sem fundo (padrão: "auto") |
| `size` | COMBO | Não | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" | Tamanho da imagem. Selecione "Custom" para usar largura e altura personalizadas (apenas GPT Image 2) (padrão: "auto") |
| `n` | INT | Não | 1 a 8 | Quantas imagens gerar (padrão: 1) |
| `image` | IMAGE | Não | - | Imagem de referência opcional para edição de imagem |
| `mask` | MASK | Não | - | Máscara opcional para inpaint (áreas brancas serão substituídas) |
| `model` | COMBO | Não | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" | Modelo GPT Image a ser usado (padrão: "gpt-image-2") |
| `custom_width` | INT | Não | 1024 a 3840 | Usado apenas quando `size` é "Custom". Deve ser um múltiplo de 16 (apenas GPT Image 2) (padrão: 1024) |
| `custom_height` | INT | Não | 1024 a 3840 | Usado apenas quando `size` é "Custom". Deve ser um múltiplo de 16 (apenas GPT Image 2) (padrão: 1024) |

**Restrições dos Parâmetros:**

- Quando `image` é fornecida, o nó alterna para o modo de edição de imagem
- `mask` só pode ser usada quando `image` é fornecida
- Ao usar `mask`, apenas imagens individuais são suportadas (o tamanho do lote deve ser 1)
- `mask` e `image` devem ter o mesmo tamanho
- A resolução personalizada (`size` = "Custom") é suportada apenas pelo modelo gpt-image-2
- A largura e altura personalizadas devem ser múltiplos de 16
- A proporção da resolução personalizada não deve exceder 3:1
- O total de pixels da resolução personalizada deve estar entre 655.360 e 8.294.400
- Fundo transparente não é suportado para o modelo gpt-image-2
- Tamanhos maiores que 1536x1024 (por exemplo, 2048x2048, 3840x2160) são suportados apenas pelo modelo gpt-image-2

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `IMAGE` | IMAGE | Imagem(ns) gerada(s) ou editada(s) |

---
**Source fingerprint (SHA-256):** `44b258d6afcb388db3836427abdd5a7cb5c09a0328efceef7e114dd61a38eae1`

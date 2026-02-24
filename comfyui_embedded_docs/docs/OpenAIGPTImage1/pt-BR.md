> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/pt-BR.md)

Gera imagens de forma síncrona através do endpoint GPT Image 1 da OpenAI. Este nó pode criar novas imagens a partir de prompts de texto ou editar imagens existentes quando fornecida uma imagem de entrada e uma máscara opcional.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Prompt de texto para o GPT Image 1 (padrão: "") |
| `seed` | INT | Não | 0 a 2147483647 | Semente aleatória para a geração (padrão: 0) - ainda não implementada no backend |
| `quality` | COMBO | Não | "low"<br>"medium"<br>"high" | Qualidade da imagem, afeta o custo e o tempo de geração (padrão: "low") |
| `background` | COMBO | Não | "opaque"<br>"transparent" | Retorna a imagem com ou sem fundo (padrão: "opaque") |
| `size` | COMBO | Não | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024" | Tamanho da imagem (padrão: "auto") |
| `n` | INT | Não | 1 a 8 | Quantas imagens gerar (padrão: 1) |
| `image` | IMAGE | Não | - | Imagem de referência opcional para edição de imagem (padrão: None) |
| `mask` | MASK | Não | - | Máscara opcional para inpainting (as áreas brancas serão substituídas) (padrão: None) |

**Restrições dos Parâmetros:**

- Quando `image` é fornecido, o nó muda para o modo de edição de imagem
- `mask` só pode ser usada quando `image` é fornecido
- Ao usar `mask`, apenas imagens únicas são suportadas (o tamanho do lote deve ser 1)
- `mask` e `image` devem ter o mesmo tamanho

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Imagem(ns) gerada(s) ou editada(s) |

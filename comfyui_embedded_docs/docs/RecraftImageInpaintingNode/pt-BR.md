> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/pt-BR.md)

Este nó modifica imagens com base em um prompt de texto e uma máscara. Ele usa a API Recraft para editar de forma inteligente áreas específicas de uma imagem que você define com uma máscara, mantendo o restante da imagem inalterado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser modificada |
| `mask` | MASK | Sim | - | A máscara que define quais áreas da imagem devem ser modificadas |
| `prompt` | STRING | Sim | - | Prompt para a geração da imagem (padrão: string vazia) |
| `n` | INT | Sim | 1-6 | O número de imagens a serem geradas (padrão: 1, mínimo: 1, máximo: 6) |
| `seed` | INT | Sim | 0-18446744073709551615 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0, mínimo: 0, máximo: 18446744073709551615) |
| `recraft_style` | STYLEV3 | Não | - | Parâmetro de estilo opcional para a API Recraft |
| `negative_prompt` | STRING | Não | - | Uma descrição textual opcional de elementos indesejados em uma imagem (padrão: string vazia) |

*Nota: A `image` e a `mask` devem ser fornecidas juntas para que a operação de inpainting funcione. A máscara será redimensionada automaticamente para corresponder às dimensões da imagem.*

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A(s) imagem(ns) modificada(s) gerada(s) com base no prompt e na máscara |

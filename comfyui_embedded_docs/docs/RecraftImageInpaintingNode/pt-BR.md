# Recraft Preenchimento de Imagem

Este nó modifica áreas específicas de uma imagem com base em um prompt de texto e uma máscara. Ele usa a API Recraft para editar de forma inteligente apenas as regiões mascaradas, mantendo o restante da imagem inalterado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A imagem de entrada a ser modificada | IMAGE | Sim | - |
| `máscara` | A máscara que define quais áreas da imagem devem ser modificadas | MASK | Sim | - |
| `prompt` | Prompt para a geração da imagem (padrão: string vazia, comprimento máximo: 1000 caracteres) | STRING | Sim | - |
| `n` | O número de imagens a serem geradas (padrão: 1, mínimo: 1, máximo: 6) | INT | Sim | 1-6 |
| `semente` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0) | INT | Sim | 0-18446744073709551615 |
| `recraft_style` | Parâmetro de estilo opcional para a API Recraft. Se não for fornecido, o padrão é o estilo "realistic_image" | STYLEV3 | Não | - |
| `negative_prompt` | Uma descrição textual opcional de elementos indesejados em uma imagem (padrão: string vazia) | STRING | Não | - |

*Observação: os parâmetros `image` e `mask` devem ser fornecidos juntos para que a operação de inpainting funcione. A máscara será redimensionada automaticamente para corresponder às dimensões da imagem. O parâmetro `prompt` é validado e tem comprimento máximo de 1000 caracteres. Se um `style_id` da Infinite Style Library for usado, certifique-se de que não seja um estilo de arte vetorial, pois isso pode fazer com que a API retorne dados SVG em vez de uma imagem.*

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A(s) imagem(ns) modificada(s) gerada(s) com base no prompt e na máscara. Retorna uma imagem para cada imagem de entrada multiplicada pelo parâmetro `n` | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `539a49aec582f529a13059388222c3998e22d52618738843d9b2b6e0fb1ea5c3`

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/en.md)

Este nó modifica áreas específicas de uma imagem com base em um prompt de texto e uma máscara. Ele utiliza a API Recraft para editar de forma inteligente apenas as regiões mascaradas, mantendo o restante da imagem inalterado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem de entrada a ser modificada | IMAGE | Sim | - |
| `máscara` | A máscara que define quais áreas da imagem devem ser modificadas | MASK | Sim | - |
| `prompt` | Prompt para a geração da imagem (padrão: string vazia, comprimento máximo: 1000 caracteres) | STRING | Sim | - |
| `n` | O número de imagens a serem geradas (padrão: 1, mínimo: 1, máximo: 6) | INT | Sim | 1-6 |
| `semente` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0) | INT | Sim | 0-18446744073709551615 |
| `recraft_style` | Parâmetro de estilo opcional para a API Recraft. Se não for fornecido, o padrão é o estilo "realistic_image" | STYLEV3 | Não | - |
| `negative_prompt` | Uma descrição textual opcional de elementos indesejados na imagem (padrão: string vazia) | STRING | Não | - |

*Nota: A `image` e a `mask` devem ser fornecidas juntas para que a operação de inpaint funcione. A máscara será redimensionada automaticamente para corresponder às dimensões da imagem. O `prompt` é validado e possui um comprimento máximo de 1000 caracteres.*

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A(s) imagem(ns) modificada(s) gerada(s) com base no prompt e na máscara. Retorna uma imagem por imagem de entrada multiplicada pelo parâmetro `n` | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3eb6505a19173d8e4ea4216348f9592fd996cdfe2f07a9e79ccec5f738a8fb93`

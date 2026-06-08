Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/en.md)

## Visão Geral

Modifica uma imagem existente com base em um prompt de texto. Este nó envia suas imagens e uma descrição textual para a API Grok, que edita as imagens de acordo com suas instruções e retorna o resultado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | O prompt de texto usado para gerar a imagem. Deve ter pelo menos 1 caractere após a remoção de espaços em branco. | STRING | Sim | N/A |
| `modelo` | O modelo de imagem Grok a ser utilizado. Este parâmetro possui várias subopções que aparecem após a seleção de um modelo. Modelos disponíveis: `grok-imagine-image-quality`, `grok-imagine-image-pro`, `grok-imagine-image`. Cada modelo possui capacidades diferentes (veja a nota abaixo). | MODEL | Sim | Ver Descrição |
| `semente` | Semente para determinar se o nó deve ser reexecutado; os resultados reais são não determinísticos, independentemente da semente. (padrão: 0) | INT | Sim | 0 a 2147483647 |

**Nota sobre as restrições do parâmetro `model`:**
- O parâmetro `model` é uma combinação dinâmica que inclui subopções para `resolution`, `number_of_images`, `images` e `aspect_ratio`.
- **`grok-imagine-image-quality`**: Suporta até 3 imagens de entrada e permite proporção de aspecto personalizada.
- **`grok-imagine-image-pro`**: Suporta apenas 1 imagem de entrada e não permite proporção de aspecto personalizada.
- **`grok-imagine-image`**: Suporta até 3 imagens de entrada e permite proporção de aspecto personalizada.
- **Pelo menos uma imagem de entrada é necessária** para edição. O nó gerará um erro se nenhuma imagem for fornecida.
- **Proporção de aspecto personalizada** (subopção `aspect_ratio`) só é permitida quando múltiplas imagens estão conectadas à entrada de imagem. Se apenas uma imagem for fornecida, a proporção de aspecto deve ser definida como "auto".

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | A(s) imagem(ns) editada(s) retornada(s) pela API Grok. Se uma única imagem for gerada, ela é retornada diretamente. Se múltiplas imagens forem geradas, elas são concatenadas em um único tensor de lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b041b40bb5712a67b09dcb0c841f00cbdd9ef77b9e4f3fdc6b2c4038be447ba5`

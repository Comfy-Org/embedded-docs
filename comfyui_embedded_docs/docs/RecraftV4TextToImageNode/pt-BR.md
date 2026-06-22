# Recraft V4 Texto para Imagem

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/en.md)

Este nó gera imagens a partir de descrições textuais usando os modelos de IA Recraft V4 ou V4 Pro. Ele envia seu prompt para uma API externa e retorna as imagens geradas. Você pode controlar a saída especificando o modelo, o tamanho da imagem e a quantidade de imagens a serem criadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt para a geração da imagem. Máximo de 10.000 caracteres. | STRING | Sim | N/A |
| `prompt_negativo` | Uma descrição textual opcional de elementos indesejados em uma imagem. | STRING | Não | N/A |
| `modelo` | O modelo a ser usado para a geração. A seleção de um modelo determina os tamanhos de imagem disponíveis. | COMBO | Sim | `"recraftv4"`<br>`"recraftv4_pro"` |
| `size` | O tamanho da imagem gerada. As opções disponíveis dependem do modelo selecionado. Para `recraftv4`, o padrão é "1024x1024". Para `recraftv4_pro`, o padrão é "2048x2048". | COMBO | Sim | Varia conforme o modelo |
| `n` | O número de imagens a serem geradas (padrão: 1). | INT | Sim | 1 a 6 |
| `semente` | Semente para determinar se o nó deve ser reexecutado; os resultados reais são não determinísticos, independentemente da semente (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |
| `recraft_controls` | Controles adicionais opcionais sobre a geração, por meio do nó Recraft Controls. | CUSTOM | Não | N/A |

**Observação:** O parâmetro `size` é uma entrada dinâmica cujas opções disponíveis mudam com base no `model` selecionado. O valor de `seed` não garante resultados de imagem reproduzíveis.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A imagem gerada ou lote de imagens. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `77d549a43aeee670b6c42069654017fb6b202ed83ca330389573b790bad6ae6e`

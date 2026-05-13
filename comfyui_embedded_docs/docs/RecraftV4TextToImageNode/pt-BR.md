> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/en.md)

Este nó gera imagens a partir de descrições textuais usando os modelos de IA Recraft V4 ou V4 Pro. Ele envia seu prompt para uma API externa e retorna as imagens geradas. Você pode controlar a saída especificando o modelo, o tamanho da imagem e a quantidade de imagens a serem criadas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | N/A | Prompt para a geração da imagem. Máximo de 10.000 caracteres. |
| `prompt_negativo` | STRING | Não | N/A | Uma descrição textual opcional de elementos indesejados em uma imagem. |
| `modelo` | COMBO | Sim | `"recraftv4"`<br>`"recraftv4_pro"` | O modelo a ser usado para a geração. A seleção de um modelo determina os tamanhos de imagem disponíveis. |
| `size` | COMBO | Sim | Varia conforme o modelo | O tamanho da imagem gerada. As opções disponíveis dependem do modelo selecionado. Para `recraftv4`, o padrão é "1024x1024". Para `recraftv4_pro`, o padrão é "2048x2048". |
| `n` | INT | Sim | 1 a 6 | O número de imagens a serem geradas (padrão: 1). |
| `semente` | INT | Sim | 0 a 18446744073709551615 | Semente para determinar se o nó deve ser reexecutado; os resultados reais são não determinísticos, independentemente da semente (padrão: 0). |
| `recraft_controls` | CUSTOM | Não | N/A | Controles adicionais opcionais sobre a geração, por meio do nó Recraft Controls. |

**Observação:** O parâmetro `size` é uma entrada dinâmica cujas opções disponíveis mudam com base no `model` selecionado. O valor de `seed` não garante resultados de imagem reproduzíveis.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | IMAGE | A imagem gerada ou lote de imagens. |

---
**Source fingerprint (SHA-256):** `77d549a43aeee670b6c42069654017fb6b202ed83ca330389573b790bad6ae6e`

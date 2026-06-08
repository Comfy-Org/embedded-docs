Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/en.md)

O nó Grok Image gera uma ou mais imagens com base em uma descrição textual usando o modelo de IA Grok. Ele envia seu prompt para um serviço externo e retorna as imagens geradas como tensores que podem ser utilizados em seu fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo Grok específico a ser usado para geração de imagens. Diferentes modelos podem oferecer qualidade, velocidade ou recursos variados. | COMBO | Sim | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"`<br>`"grok-imagine-image-beta"` |
| `prompt` | O prompt de texto usado para gerar a imagem. Esta descrição orienta a IA sobre o que criar. Deve ter pelo menos 1 caractere. | STRING | Sim | N/A |
| `aspect_ratio` | A proporção desejada entre largura e altura para a imagem gerada. | COMBO | Sim | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `number_of_images` | Número de imagens a serem geradas (padrão: 1). | INT | Não | 1 a 10 |
| `seed` | Um valor de semente para determinar se o nó deve ser executado novamente. Os resultados reais da imagem são não determinísticos e variarão mesmo com a mesma semente (padrão: 0). | INT | Não | 0 a 2147483647 |
| `resolução` | A resolução de saída desejada para as imagens geradas (padrão: "1K"). | COMBO | Não | `"1K"`<br>`"2K"` |

**Nota:** O parâmetro `seed` é usado principalmente para controlar quando o nó é reexecutado dentro de um fluxo de trabalho. Devido à natureza do serviço de IA externo, as imagens geradas não serão reproduzíveis ou idênticas entre execuções, mesmo com uma semente idêntica.

**Nota sobre preços:** O custo da geração de imagens depende do `model`, `resolution` e `number_of_images` selecionados. Por exemplo, o modelo "grok-imagine-image-quality" com resolução "1K" custa $0,05 por imagem, enquanto a resolução "2K" custa $0,07 por imagem. O modelo "grok-imagine-image-pro" custa $0,07 por imagem, e outros modelos custam $0,02 por imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A imagem gerada ou um lote de imagens. Se `number_of_images` for 1, um único tensor de imagem é retornado. Se for maior que 1, um lote de tensores de imagem é retornado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5c8a76d3636dea8bcc6ade0d8adb6e6d1610b518a31e15fc7fce3f107fe63953`

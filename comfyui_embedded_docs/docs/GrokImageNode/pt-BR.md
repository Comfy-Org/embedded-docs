# Grok Image

O nó Grok Image gera uma ou mais imagens com base em uma descrição em texto usando o modelo de IA Grok. Ele envia seu prompt para um serviço externo e retorna as imagens geradas como tensores que podem ser usados no seu fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo Grok específico a ser usado para geração de imagens. Modelos diferentes podem oferecer qualidade, velocidade ou recursos variados. | COMBO | Sim | `"grok-imagine-image-2.0"`<br>`"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `prompt` | O prompt de texto usado para gerar a imagem. Esta descrição orienta a IA sobre o que criar. Deve ter pelo menos 1 caractere. | STRING | Sim | N/A |
| `aspect_ratio` | A proporção largura-altura desejada para a imagem gerada. | COMBO | Sim | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `number_of_images` | Número de imagens a serem geradas (padrão: 1). | INT | Sim | 1 a 10 |
| `seed` | Semente para determinar se o nó deve ser reexecutado; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `resolução` | A resolução de saída desejada para as imagens geradas (padrão: "1K"). | COMBO | Não | `"1K"`<br>`"2K"` |
| `qualidade` | Nível de qualidade, suportado apenas pelo modelo `grok-imagine-image-2.0` (padrão: "medium"; "low" é uma das opções disponíveis). Para todos os outros modelos, essa configuração é ignorada. | COMBO | Não | Múltiplas opções disponíveis |

**Nota:** O parâmetro `seed` é usado principalmente para controlar quando o nó é reexecutado em um fluxo de trabalho. Devido à natureza do serviço externo de IA, as imagens geradas não serão reproduzíveis ou idênticas entre execuções, mesmo com uma semente idêntica.

**Nota sobre preços:** O custo da geração de imagens depende do `model`, `resolution`, `quality` e `number_of_images` selecionados. Para o modelo `grok-imagine-image-2.0`, a qualidade "low" custa US$ 0,04 por imagem na resolução 1K e US$ 0,06 por imagem na resolução 2K; os outros níveis de qualidade custam US$ 0,06 por imagem em 1K e US$ 0,08 por imagem em 2K. O modelo `grok-imagine-image-quality` custa US$ 0,05 por imagem na resolução 1K e US$ 0,07 por imagem na resolução 2K. O modelo `grok-imagine-image-pro` custa US$ 0,07 por imagem. O modelo `grok-imagine-image` custa US$ 0,02 por imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A imagem gerada ou um lote de imagens. Se `number_of_images` for 1, um único tensor de imagem é retornado. Se for maior que 1, um lote de tensores de imagem é retornado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a89f5df0d4827f45013f1af92541d36b5b8c8edc8626e07af4fe2d85ee5486e7`

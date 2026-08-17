# Grok Image

O nó Grok Image gera uma ou mais imagens com base em um prompt de texto usando os modelos de imagem Grok AI. Ele envia o prompt e as configurações para um serviço externo e retorna as imagens geradas como tensores, que podem ser usados em outras partes do fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo Grok específico a ser usado para geração de imagens. Modelos diferentes podem oferecer qualidade, velocidade ou recursos variados. | COMBO | Sim | `"grok-imagine-image-2.0"`<br>`"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `prompt` | O prompt de texto usado para gerar a imagem. Essa descrição orienta a IA sobre o que criar. Deve conter pelo menos 1 caractere que não seja espaço em branco. | STRING | Sim | N/A |
| `aspect_ratio` | A proporção largura-altura desejada para a imagem gerada. | COMBO | Sim | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `number_of_images` | Número de imagens a gerar (padrão: 1). | INT | Sim | 1 a 10 |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos, independentemente da semente (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `resolution` | A resolução de saída desejada para as imagens geradas (padrão: "1K"). | COMBO | Não | `"1K"`<br>`"2K"` |
| `quality` | Nível de qualidade, suportado apenas pelo modelo grok-imagine-image-2.0 (padrão: "medium"). | COMBO | Não | Múltiplas opções disponíveis |

**Nota:** O parâmetro `quality` é aplicado somente quando `model` está definido como "grok-imagine-image-2.0". Para todos os outros modelos, essa configuração é ignorada.

**Nota:** O parâmetro `seed` é usado principalmente para controlar quando o nó é executado novamente dentro de um fluxo de trabalho. Devido à natureza do serviço de IA externo, as imagens geradas não são reproduzíveis entre execuções, mesmo com uma semente idêntica.

**Nota sobre preços:** O custo da geração de imagens depende do `model`, `resolution`, `quality` e `number_of_images` selecionados; o preço total é a taxa por imagem multiplicada por `number_of_images`. Para o modelo "grok-imagine-image-2.0", a taxa por imagem é de $0,04 na resolução "1K" e $0,06 em "2K" com qualidade "low", ou $0,06 em "1K" e $0,08 em "2K" com outros níveis de qualidade. O modelo "grok-imagine-image-quality" custa $0,05 por imagem em "1K" e $0,07 por imagem em "2K". O modelo "grok-imagine-image-pro" custa $0,07 por imagem. Os outros modelos custam $0,02 por imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A imagem gerada ou um lote de imagens. Se `number_of_images` for 1, um único tensor de imagem é retornado. Se for maior que 1, um lote de tensores de imagem é retornado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a89f5df0d4827f45013f1af92541d36b5b8c8edc8626e07af4fe2d85ee5486e7`

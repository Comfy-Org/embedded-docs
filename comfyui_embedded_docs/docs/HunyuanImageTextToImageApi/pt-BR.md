# Tencent HY Image: Text to Image

O nó Tencent HY Image: Text to Image gera uma imagem a partir de uma descrição de texto com o modelo Hunyuan Image da Tencent. O prompt é enviado à API, que o reescreve e o expande antes da renderização, e a imagem finalizada é retornada como um lote de imagens.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo usado para geração. O modelo selecionado determina quais entradas adicionais são exibidas. | DYNAMIC_COMBO | Sim | `"hy-image-3.5-preview"` |

### Entradas do hy-image-3.5-preview

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descreve a imagem a ser gerada. O modelo a reescreve e expande antes da renderização. Não deve estar vazio (padrão: vazio). | STRING | Sim | Qualquer texto |
| `aspect_ratio` | Proporção da saída. `"auto"` permite que o modelo escolha a proporção a partir do prompt e não está disponível em 4K. Ignorado quando `resolution` é `"custom"`. | COMBO | Sim | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"` (padrão: `"auto"`) |
| `resolution` | Área em pixels da imagem: 1K é cerca de 1024x1024, 2K cerca de 2048x2048 e 4K cerca de 4096x4096. Qualquer valor acima de 2K é renderizado em 2K e ampliado pelo modelo. Defina como `"custom"` para usar `width` e `height` em vez de uma área predefinida. | COMBO | Sim | `"1K"`<br>`"2K"`<br>`"4K"`<br>`"custom"` (padrão: `"2K"`) |
| `width` | Largura da imagem em pixels. Usada apenas quando `resolution` é `"custom"`. | INT | Sim | 256-8192, incrementos de 16 (padrão: 2048) |
| `height` | Altura da imagem em pixels. Usada apenas quando `resolution` é `"custom"`. | INT | Sim | 256-8192, incrementos de 16 (padrão: 2048) |
| `seed` | Semente usada para geração. Os resultados ainda variam entre execuções com a mesma semente. | INT | Sim | 0-2147483647 (padrão: 42) |
| `watermark` | Define se deve adicionar uma marca d'água gerada por IA ao resultado. Este é um parâmetro avançado. | BOOLEAN | Não | true<br>false (padrão: false) |

`prompt` não deve estar vazio. Com a resolução `"custom"`, `width` e `height` devem ser ambos múltiplos de 16 e seu produto não deve exceder o limite de área de 4096 x 4096 pixels (cerca de 16,7 megapixels); qualquer proporção funciona, embora além de aproximadamente 6:1 o modelo comece a repetir o assunto. A proporção `"auto"` precisa que o modelo escolha um tamanho, então só funciona dentro do limite de área de 2K: em 4K, escolha uma proporção explícita ou use `"custom"`.

## Saídas

| Nome da Saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem gerada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageTextToImageApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1d4e70d688c5aa4e79b81447da559e201078454077da34769f2a4f544fbba63f`

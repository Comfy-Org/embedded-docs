# Tencent HY Image: Edit

O nó Tencent HY Image: Edit edita ou combina imagens de referência a partir de uma instrução de texto com o modelo Hunyuan Image da Tencent. Conecte de uma a cinco imagens, descreva a alteração no prompt e consulte as imagens como `@Image1`, `@Image2` e assim por diante. O nó envia as imagens de referência por upload, envia a solicitação para a API e retorna o resultado editado.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo usado para edição. O modelo selecionado determina quais entradas adicionais são exibidas. | DYNAMIC_COMBO | Sim | `"hy-image-3.5-preview"` |

### Entradas do hy-image-3.5-preview

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | As instruções de edição. Suporta referências no estilo `@Image1` para as imagens conectadas. Não pode estar vazio (padrão: vazio). | STRING | Sim | Qualquer texto |
| `aspect_ratio` | Proporção da saída. `"auto"` segue a proporção da primeira imagem de referência e não está disponível em 4K. Ignorado quando `resolution` é `"custom"`. | COMBO | Sim | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"` (padrão: `"auto"`) |
| `resolution` | Área em pixels da saída: 1K é cerca de 1024x1024, 2K cerca de 2048x2048 e 4K cerca de 4096x4096. Qualquer resolução acima de 2K é renderizada em 2K e ampliada pelo modelo. Defina como `"custom"` para usar `width` e `height` em vez de uma área predefinida. | COMBO | Sim | `"1K"`<br>`"2K"`<br>`"4K"`<br>`"custom"` (padrão: `"2K"`) |
| `width` | Largura da saída em pixels. Usada apenas quando `resolution` é `"custom"`. | INT | Sim | 256-8192, incrementos de 16 (padrão: 2048) |
| `height` | Altura da saída em pixels. Usada apenas quando `resolution` é `"custom"`. | INT | Sim | 256-8192, incrementos de 16 (padrão: 2048) |
| `seed` | Semente usada para geração. Os resultados ainda variam entre execuções com a mesma semente. | INT | Sim | 0-2147483647 (padrão: 42) |
| `reference_detail` | Quanto detalhe das imagens de referência o modelo vê: `"standard"` permite até 1024x1024 pixels por imagem, `"high"` até 2048x2048 e preserva melhor textos pequenos e detalhes finos, mas demora mais. Este é um parâmetro avançado. | COMBO | Não | `"standard"`<br>`"high"` (padrão: `"standard"`) |
| `watermark` | Define se deve adicionar uma marca d'água gerada por IA ao resultado. Este é um parâmetro avançado. | BOOLEAN | Não | true<br>false (padrão: false) |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | As imagens de referência a serem editadas ou combinadas. Slot expansível: conecte de 1 a 5 imagens (`image_1` a `image_5`). Consulte-as no prompt como `@Image1` ... `@Image5`, numeradas na ordem de entrada; uma entrada em lote conta uma vez por imagem. | IMAGE | Sim | 1-5 imagens |

`prompt` não pode estar vazio, e uma referência no prompt como `@Image3` gera um erro quando apenas 1 ou 2 imagens estão conectadas. No máximo 5 imagens de referência podem ser usadas no total, contando cada imagem de um lote separadamente. Com a resolução `"custom"`, `width` e `height` devem ser ambos múltiplos de 16 e seu produto não deve exceder o limite de área de 4096 x 4096 pixels (cerca de 16,7 megapixels); qualquer proporção funciona, embora acima de aproximadamente 6:1 o modelo comece a repetir o assunto. A proporção `"auto"` só funciona dentro do limite de área de 2K, então em 4K escolha uma proporção explícita ou use `"custom"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem editada produzida a partir das imagens de referência e do prompt. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `46c112347b51a2983521f87bbeb047289515f4073c48ba5d909fd3bae4597633`

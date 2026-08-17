# Recraft Texto para Imagem

Gera imagens de forma síncrona com base no prompt e na resolução. Este nó se conecta à API Recraft para criar imagens a partir de descrições textuais com dimensões especificadas e parâmetros opcionais de estilo e controle.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt para a geração da imagem. (padrão: "") | STRING | Sim | - |
| `size` | O tamanho da imagem gerada. (padrão: "1024x1024") | COMBO | Sim | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" |
| `n` | O número de imagens a serem geradas. (padrão: 1) | INT | Sim | 1-6 |
| `seed` | Semente para determinar se o nó deve ser reexecutado; os resultados reais são não determinísticos independentemente da semente. (padrão: 0) | INT | Sim | 0-18446744073709551615 |
| `recraft_style` | Seleção opcional de estilo para geração de imagem. Quando não fornecida, o padrão é o estilo de imagem realista. | RECRAFT_STYLE | Não | Múltiplas opções disponíveis |
| `negative_prompt` | Uma descrição textual opcional de elementos indesejados em uma imagem. (padrão: "") | STRING | Não | - |
| `recraft_controls` | Controles adicionais opcionais sobre a geração por meio do nó Recraft Controls. | RECRAFT_CONTROLS | Não | Múltiplas opções disponíveis |

**Nota:** O parâmetro `seed` apenas controla quando o nó é reexecutado, mas não torna a geração de imagem determinística. As imagens de saída reais variarão mesmo com o mesmo valor de semente.

**Nota:** O parâmetro `prompt` deve ter entre 1 e 1000 caracteres de comprimento.

**Nota:** Se você usar um `style_id` da Infinite Style Library, certifique-se de que não seja um estilo de arte vetorial, pois isso retornará dados SVG em vez de uma imagem e causará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A(s) imagem(ns) gerada(s) como uma saída de tensor em lote. Quando várias imagens são geradas (n > 1), elas são concatenadas ao longo da dimensão do lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d75b7dd2d8cee70c3bc1d2c64fb07ce814a3672619e8647f4c4c2cdc2635945c`

# Recraft Texto para Imagem

Gera imagens de forma síncrona com base no prompt e na resolução. Este nó se conecta à API Recraft para criar imagens a partir de descrições textuais com dimensões especificadas e parâmetros opcionais de estilo e controle.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt para a geração da imagem. (padrão: "") | STRING | Sim | - |
| `size` | O tamanho da imagem gerada. (padrão: "1024x1024") | COMBO | Sim | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" |
| `n` | O número de imagens a serem geradas. (padrão: 1) | INT | Sim | 1-6 |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente. (padrão: 0) | INT | Sim | 0-18446744073709551615 |
| `recraft_style` | Seleção opcional de estilo para geração de imagem. Quando não fornecido, o padrão é o estilo "realistic_image". | RECRAFT_STYLE | Não | Múltiplas opções disponíveis |
| `negative_prompt` | Uma descrição textual opcional de elementos indesejados em uma imagem. (padrão: "") | STRING | Não | - |
| `recraft_controls` | Controles adicionais opcionais sobre a geração através do nó Recraft Controls. | RECRAFT_CONTROLS | Não | Múltiplas opções disponíveis |

**Observação:** O parâmetro `seed` controla apenas quando o nó é executado novamente, mas não torna a geração de imagens determinística. As imagens de saída reais variarão mesmo com o mesmo valor de semente.

**Observação:** O parâmetro `prompt` deve ter entre 1 e 1000 caracteres de comprimento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | A(s) imagem(ns) gerada(s) como uma saída de tensor em lote. Quando múltiplas imagens são geradas (n > 1), elas são concatenadas ao longo da dimensão do lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `28c510ccfad13ddb50700b465af14deaa3c7c1f8597fef048d89094fd24fcd7d`

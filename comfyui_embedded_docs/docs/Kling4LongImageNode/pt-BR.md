# Kling 4.0 Long Image

Gere uma imagem vertical com Kling 4.0: o design de uma página web completa ou uma página de detalhes de produto de e-commerce. Escolha a `skill` que corresponde ao layout desejado e o nó revelará as entradas desse layout.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `habilidade` | Layout a ser gerado. `"webpage"` projeta uma página completa em torno de uma imagem de estilo e de um sujeito opcionais; `"ecommerce"` monta uma página de detalhes de produto a partir de fotos do produto. | DYNAMIC_COMBO | Sim | `"webpage"`<br>`"ecommerce"` |

### Entradas do `webpage`

Estas entradas aparecem quando `skill` está definido como `"webpage"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `style_image` | Referência opcional para o estilo visual e o layout. Refira-se a ela como `@Image1`. | IMAGE | Não | Imagem única |
| `subject_image` | Sujeito opcional a ser preservado e em torno do qual a página será projetada. Refira-se a ele como `@Image2`. | IMAGE | Não | Imagem única |
| `prompt` | Descrição opcional da página. Refira-se à imagem de estilo como `@Image1` e à imagem do sujeito como `@Image2`, e especifique o idioma do texto da página, por exemplo: "Todo texto visível deve estar apenas em inglês." Padrão: string vazia. | STRING | Sim | Texto multilinha |
| `resolution` | Resolução da imagem de saída. Padrão: `"1K"`. | COMBO | Sim | `"1K"`<br>`"2K"` |
| `seed` | A seed controla se o nó deve ser reexecutado; os resultados não são determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

### Entradas do `ecommerce`

Estas entradas aparecem quando `skill` está definido como `"ecommerce"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `product_images` | Slots expansíveis para as fotos do produto (`image_1` ... `image_3`). Refira-se a eles no prompt como `@Image1`, `@Image2`, `@Image3`. | AUTOGROW | Sim | 1 a 3 imagens |
| `prompt` | Descrição opcional da página. Refira-se às imagens do produto como `@Image1`, `@Image2`, `@Image3`. Padrão: string vazia. | STRING | Sim | Texto multilinha |
| `length` | Comprimento da página gerada. Padrão: `"medium"`. | COMBO | Sim | `"short"`<br>`"medium"`<br>`"long"` |
| `resolution` | Resolução da imagem de saída. Padrão: `"1K"`. | COMBO | Sim | `"1K"`<br>`"2K"` |
| `seed` | A seed controla se o nó deve ser reexecutado; os resultados não são determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Restrições e comportamento:**

* No máximo 3 imagens de produto podem ser conectadas em `ecommerce`.
* Cada imagem deve ter pelo menos 300x300 pixels e uma proporção entre 2:5 e 5:2.
* Com `webpage`, um prompt que mencione `@Image1` ou `@Image2` gera um erro quando essa imagem não está conectada.
* O preço de uma chamada depende da skill, da resolução e, para `ecommerce`, do comprimento da página.

## Saídas

| Nome da Saída | Descrição | Tipo de dados |
|---------------|-------------|---------------|
| `image` | A imagem longa gerada, baixada do Kling assim que a tarefa for concluída. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4LongImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f1e687bcc8334229c60b318118120b85ddd580d1b62f343164f9803b98a1f987`

# Bria Product Holding

Este nó coloca um produto nas mãos de uma pessoa com a Bria. A identidade, a pose e o fundo da pessoa são mantidos enquanto a cena é renderizada novamente com cerca de 1 megapixel, então o resultado não fica alinhado pixel a pixel com a foto de entrada. Todas as imagens do produto descrevem um único produto a partir de ângulos ou estágios diferentes.

## Entradas

O seletor `moderation` revela uma opção adicional de moderação quando definido como `"true"`.

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `person_image` | A foto da pessoa que segura o produto. O canal alfa é descartado antes de a imagem ser enviada. | IMAGE | Sim | - |
| `product_images` | 1 a 3 imagens de um produto: o próprio produto, sua embalagem, outro ângulo ou um item complementar. Uma entrada em lote conta uma vez por imagem e áreas transparentes são tratadas como brancas. | AUTOGROW | Sim | 1 a 3 imagens |
| `instruction` | Direcionamento extra opcional adicionado à instrução integrada da Bria, como qual mão usar ou para que lado o rótulo está voltado. Padrão: `""` (string vazia). | STRING | Sim | - |
| `aspect_ratio` | `"auto"` mantém o enquadramento da foto da pessoa em cerca de 1 megapixel. Uma proporção fixa retorna de 0,6 a 1 megapixel, por exemplo 768x1024 para `"3:4"`. Padrão: `"auto"`. | COMBO | Sim | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"` |
| `seed` | Semente enviada à Bria com a solicitação. Padrão: 42. | INT | Sim | 1 a 2147483647 |
| `moderation` | Configurações de moderação. Quando definido como `"true"`, o sinalizador de moderação abaixo fica disponível. | DYNAMIC_COMBO | Sim | `"false"`<br>`"true"` |

### Entradas de moderação "true"

Este parâmetro aparece somente quando `moderation` está definido como `"true"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `visual_output_moderation` | Ativa a moderação de conteúdo na imagem gerada. Padrão: `False`. | BOOLEAN | Não | True / False |

**Restrições:**

* `product_images` aceita no máximo 3 imagens, contadas por imagem quando a entrada é em lote.
* Pixels transparentes nas imagens do produto são compostos sobre branco antes do upload.
* O canal alfa de `person_image` é descartado antes do upload.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A foto editada com o produto colocado nas mãos da pessoa. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaProductHolding/pt-BR.md)

---
**Source fingerprint (SHA-256):** `91a4a4dde0e9d7fe2480130da87edf1f8ed9d4ae0c86f8a8d030c36987dcdb8e`

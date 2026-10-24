# Bria Virtual Try-On

Este nó veste uma pessoa com roupas ou acessórios usando a Bria. A identidade, a pose e o fundo da pessoa são mantidos enquanto a cena é renderizada novamente com cerca de 1 megapixel, portanto o resultado não fica alinhado pixel a pixel com a foto de entrada. Cada imagem de peça de roupa substitui o item correspondente que a pessoa já veste.

## Entradas

O seletor `moderation` revela uma opção adicional de moderação quando definido como `"true"`.

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `person_image` | A foto da pessoa que experimenta as roupas. O canal alfa é descartado antes de a imagem ser enviada. | IMAGE | Sim | - |
| `garment_images` | 1 a 3 peças de roupa ou acessórios usados juntos, cada um substituindo o item correspondente que a pessoa veste. Uma entrada em lote conta uma vez por imagem e áreas transparentes são tratadas como branco. | AUTOGROW | Sim | 1 a 3 imagens |
| `instruction` | Direção extra opcional adicionada à instrução integrada da Bria, como qual peça de roupa colocar por cima. Padrão: `""` (string vazia). | STRING | Sim | - |
| `aspect_ratio` | `"auto"` mantém o enquadramento da foto da pessoa com cerca de 1 megapixel. Uma proporção fixa retorna de 0,6 a 1 megapixel, por exemplo 768x1024 para `"3:4"`. Padrão: `"auto"`. | COMBO | Sim | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"` |
| `seed` | Semente enviada à Bria com a solicitação. Padrão: 42. | INT | Sim | 1 a 2147483647 |
| `moderation` | Configurações de moderação. Quando definido como `"true"`, o sinalizador de moderação abaixo fica disponível. | DYNAMIC_COMBO | Sim | `"false"`<br>`"true"` |

### Entradas de moderação "true"

Este parâmetro aparece apenas quando `moderation` está definido como `"true"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `visual_output_moderation` | Ativa a moderação de conteúdo na imagem gerada. Padrão: `False`. | BOOLEAN | Não | True / False |

**Restrições:**

* `garment_images` aceita no máximo 3 imagens, contadas por imagem quando a entrada está em lote.
* Pixels transparentes nas imagens de peças de roupa são compostos sobre branco antes do envio.
* O canal alfa de `person_image` é descartado antes do envio.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `image` | A foto editada com a pessoa vestindo as peças de roupa fornecidas. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVirtualTryOn/pt-BR.md)

---
**Source fingerprint (SHA-256):** `32f89c8685d8624bdef2c17ba5ba916b030d1dc88718b83c79aadb9a5fa378de`

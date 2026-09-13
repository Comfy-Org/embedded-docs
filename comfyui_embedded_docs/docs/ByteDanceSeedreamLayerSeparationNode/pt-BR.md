# ByteDance Seedream 5.0 Pro Separação de Camadas

ByteDance Seedream 5.0 Pro Layer Separation decompõe uma imagem em uma imagem de fundo base mais até 16 camadas transparentes reposicionáveis, cada uma com ordem de empilhamento, caixa delimitadora, nome e descrição. Retorna o fundo, imagens por camada com máscaras, caixas de posicionamento e uma pilha de camadas pronta para edição.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A imagem a ser separada. Exatamente uma imagem, com pelo menos 512x512 pixels, proporção entre 1:16 e 16:1. Entradas maiores que cerca de 4MP são reduzidas antes do envio. | IMAGE | Sim | Imagem única |
| `prompt` | Como separar a imagem. Deixe vazio para detectar e separar automaticamente todos os elementos principais. Descreva elementos em linguagem natural para controlar a separação, ou direcione regiões exatas com tags `<bbox>left top right bottom</bbox>` (coordenadas de 0 a 1000 por mil). Padrão: string vazia. | STRING | Sim | Texto multilinha |
| `tamanho` | Nível de resolução de saída. "auto" segue o tamanho da imagem de entrada (limitado ao intervalo de 1K-2K). Padrão: "auto". | COMBO | Sim | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Semente a ser usada para geração. Padrão: 0. | INT | Sim | 0 a 2147483647 |
| `otimização do prompt` | Modo de otimização do prompt: "standard" oferece maior qualidade, "fast" menor tempo de geração. Padrão: "standard". | COMBO | Não | "standard"<br>"fast" |
| `marca d'água` | Se deve adicionar uma marca d'água "AI generated" às imagens. Padrão: false. | BOOLEAN | Não | false<br>true |
| `recortar camadas` | Geometria das saídas em lote de camadas/máscaras (`layer_stack` não é afetado e sempre tem recorte justo). Tela cheia: cada camada em uma tela do tamanho da base na posição de sua caixa delimitadora - recomponha diretamente com ImageCompositeMasked. Tamanho mínimo: cada camada recortada para sua caixa delimitadora (preenchida até a maior camada para processamento em lote) - tensores muito menores; reconstrua o posicionamento com Layers From Bounding Boxes usando a saída `bboxes`. Padrão: false (tela cheia). | BOOLEAN | Não | false (tela cheia)<br>true (tamanho mínimo) |

Nota: A entrada `image` deve ser uma única imagem; lotes não são suportados. A imagem deve ter pelo menos 512x512 pixels com proporção entre 1:16 e 16:1.

## Saídas

| Nome de Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `base_image` | A imagem base (imagem de fundo) sobre a qual as camadas são empilhadas. | IMAGE |
| `base_mask` | Transparência da imagem base (1 = transparente, convenção do LoadImage); atualmente sempre totalmente opaca. | MASK |
| `layers` | Camadas transparentes ordenadas de baixo para cima. Modo tela cheia: posicionadas em uma tela preta do tamanho da base na posição de sua caixa delimitadora. Modo tamanho mínimo: recortadas para sua caixa delimitadora, ancoradas no canto superior esquerdo, preenchidas até a maior camada. | IMAGE |
| `masks` | Transparência por camada, alinhada por índice com o lote de `layers` (1 = transparente, convenção do LoadImage). Para composição no estilo ImageCompositeMasked, adicione InvertMask primeiro. | MASK |
| `bboxes` | Uma caixa de posicionamento por camada, alinhada por índice com o lote de `layers` (conecte tanto `layers` quanto `bboxes`, além de `masks`, em Layers From Bounding Boxes para reconstruir o posicionamento por camada): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` é a região de conteúdo da camada dentro de seu próprio quadro; ela é posicionada na tela na posição da caixa mais esse deslocamento. | BOUNDING_BOX |
| `layer_stack` | Documento de camadas pronto para edição para Create Layered Image: a imagem base mais cada elemento como sua própria camada nomeada, com recorte justo, em sua posição real e ordem de empilhamento. Conecte diretamente, ou estenda com Add Layer. | LAYERS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`

# ByteDance Seedream 5.0 Layer Separation

O ByteDance Seedream 5.0 Layer Separation decompõe uma imagem em uma imagem de fundo base mais até 16 camadas transparentes reposicionáveis, cada uma com ordem de empilhamento, caixa delimitadora, nome e descrição. Ele retorna o fundo, imagens por camada com máscaras, caixas de posicionamento e uma pilha de camadas pronta para edição. O seletor `model` escolhe entre o Seedream 5.0 Pro e o Seedream 5.0 Flash, mais rápido.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo Seedream usado para a separação. "seedream 5.0 pro" (padrão) oferece a mais alta qualidade de separação e também expõe um controle `prompt_optimization`; "seedream 5.0 flash" é mais rápido e mais barato e não tem controle de otimização de prompt. | DYNAMIC_COMBO | Sim | "seedream 5.0 pro"<br>"seedream 5.0 flash" |

### Entradas do Seedream 5.0 Pro e 5.0 Flash

Estas entradas estão disponíveis com ambos os modelos.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem a ser separada. Exatamente uma imagem, com pelo menos 512x512 pixels, proporção entre 1:16 e 16:1. Entradas maiores que cerca de 4MP são reduzidas antes do envio. | IMAGE | Sim | Imagem única |
| `prompt` | Como separar a imagem. Deixe vazio para detectar automaticamente e separar todos os elementos principais. Descreva elementos em linguagem natural para controlar a separação, ou direcione regiões exatas com tags `<bbox>left top right bottom</bbox>` (coordenadas em permilagem, de 0 a 1000). Padrão: string vazia. | STRING | Sim | Texto multilinha |
| `size` | Nível de resolução da saída. "auto" segue o tamanho da imagem de entrada (limitado ao intervalo de 1K-2K). Padrão: "auto". | COMBO | Sim | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Semente a ser usada para a geração. Padrão: 42. | INT | Sim | 0 a 2147483647 |
| `watermark` | Se deve adicionar uma marca d'água "AI generated" às imagens. Padrão: false. | BOOLEAN | Sim | false<br>true |
| `crop_layers` | Geometria das saídas em lote layers/masks (layer_stack não é afetado e sempre fica justo). Canvas completo: cada camada em um canvas do tamanho da base, na posição de sua caixa delimitadora — recomponha diretamente com ImageCompositeMasked. Tamanho mínimo: cada camada recortada para sua caixa delimitadora (preenchida até a maior camada para batching) — tensores muito menores; reconstrua o posicionamento com Layers From Bounding Boxes usando a saída bboxes. Padrão: false (canvas completo). | BOOLEAN | Sim | false (tela cheia)<br>true (tamanho mínimo) |

### Entradas somente do Seedream 5.0 Pro

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt_optimization` | Modo de otimização de prompt: "standard" oferece maior qualidade; "fast", menor tempo de geração. Disponível apenas com o Seedream 5.0 Pro. Padrão: "standard". | COMBO | Sim | "standard"<br>"fast" |

**Observação:** A entrada `image` deve ser uma única imagem; lotes não são suportados. A imagem deve ter pelo menos 512x512 pixels, com proporção entre 1:16 e 16:1. O Seedream 5.0 Flash sempre usa a otimização de prompt padrão.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `base_image` | A imagem base (imagem de fundo base) sobre a qual as camadas são empilhadas. | IMAGE |
| `base_mask` | Transparência da imagem base (1 = transparente, convenção do LoadImage); atualmente sempre totalmente opaca. | MASK |
| `layers` | Camadas transparentes ordenadas de baixo para cima. Modo canvas completo: posicionadas em um canvas preto do tamanho da base, na posição de sua caixa delimitadora. Modo tamanho mínimo: recortadas para sua caixa delimitadora, ancoradas no canto superior esquerdo, preenchidas até a maior camada. | IMAGE |
| `masks` | Transparência por camada, alinhada por índice com o lote layers (1 = transparente, convenção do LoadImage). Para composição no estilo ImageCompositeMasked, adicione InvertMask primeiro. | MASK |
| `bboxes` | Uma caixa de posicionamento por camada, alinhada por índice com o lote layers (alimente ambas, mais masks, em Layers From Bounding Boxes para reconstruir o posicionamento por camada): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` é a região de conteúdo da camada dentro de seu próprio quadro; ela é colocada no canvas na posição da caixa mais esse deslocamento. | BOUNDING_BOX |
| `layer_stack` | Documento de camadas pronto para edição para Create Layered Image: a imagem base mais cada elemento como sua própria camada nomeada, recortada de forma justa, em sua posição real e ordem de empilhamento. Conecte diretamente ou estenda com Add Layer. | LAYERS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b106ca63d37aea68079f0032a1f7dfeefee9f759c71bb1605bbfe66c3d9dad62`

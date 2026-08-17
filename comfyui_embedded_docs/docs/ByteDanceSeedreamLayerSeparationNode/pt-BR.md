# ByteDance Seedream 5.0 Pro Separação de Camadas

ByteDance Seedream 5.0 Pro Layer Separation decompõe uma imagem em uma placa de fundo e até 16 camadas transparentes, cada uma com sua própria ordem de empilhamento, caixa delimitadora, nome e descrição. Ela retorna o fundo, imagens por camada com máscaras, caixas de posicionamento e uma pilha de camadas pronta para edição.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem a separar. Exatamente uma imagem, com pelo menos 512x512 pixels e proporção de aspecto entre 1:16 e 16:1. Entradas maiores que cerca de 4MP são reduzidas antes do upload. | IMAGE | Sim | Single image |
| `prompt` | Como separar a imagem. Deixe vazio para detectar automaticamente e separar todos os elementos principais. Descreva elementos em linguagem natural para controlar a separação, ou segmente regiões exatas com tags `<bbox>left top right bottom</bbox>` (coordenadas de 0 a 1000 por mil). Padrão: string vazia. | STRING | Sim | Multiline text |
| `size` | Nível de resolução de saída. "auto" segue o tamanho da imagem de entrada (limitado ao intervalo de 1K a 2K). Padrão: "auto". | COMBO | Sim | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Semente a usar para a geração. Padrão: 0. | INT | Sim | 0 to 2147483647 |
| `prompt_optimization` | Modo de otimização de prompt: "standard" oferece maior qualidade, "fast" tempo de geração menor. Padrão: "standard". | COMBO | Não | "standard"<br>"fast" |
| `watermark` | Se deve adicionar uma marca d'água "gerado por IA" às imagens. Padrão: false. | BOOLEAN | Não | false<br>true |
| `crop_layers` | Geometria das saídas em lote de camadas/máscaras (o layer_stack não é afetado e é sempre com corte preciso). Full canvas: cada camada em um canvas do tamanho da base na posição de sua caixa delimitadora — recomponha diretamente com ImageCompositeMasked. Minimal size: cada camada cortada para sua caixa delimitadora (preenchida até a maior camada para empacotamento) — tensores muito menores; reconstrua o posicionamento com Layers From Bounding Boxes usando a saída bboxes. Padrão: false (full canvas). | BOOLEAN | Não | false (full canvas)<br>true (minimal size) |

Nota: A imagem de entrada deve ser uma única imagem; lotes não são suportados. A imagem deve ter pelo menos 512x512 pixels com proporção de aspecto entre 1:16 e 16:1.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `base_image` | A imagem base (placa de fundo) sobre a qual as camadas são empilhadas. | IMAGE |
| `base_mask` | Transparência da imagem base (1 = transparente, convenção do LoadImage); atualmente sempre totalmente opaca. | MASK |
| `layers` | Camadas transparentes ordenadas de baixo para cima. No modo Full canvas: posicionadas em um canvas do tamanho da base na posição de sua caixa delimitadora. No modo Minimal size: cortadas para sua caixa delimitadora, ancoradas no canto superior esquerdo e preenchidas até a maior camada. | IMAGE |
| `masks` | Transparência por camada, alinhada por índice com o lote de camadas (1 = transparente, convenção do LoadImage). Para composição no estilo ImageCompositeMasked, adicione InvertMask primeiro. | MASK |
| `bboxes` | Uma caixa de posicionamento por camada, alinhada por índice com o lote de camadas (alimente ambos, mais máscaras, no Layers From Bounding Boxes para reconstruir o posicionamento por camada): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` é a região de conteúdo da camada dentro de seu próprio quadro; ela é posicionada no canvas na posição da caixa mais esse deslocamento. | BOUNDING_BOX |
| `layer_stack` | Documento de camadas pronto para edição para Create Layered Image: a placa base mais cada elemento como sua própria camada nomeada e cortada com precisão em sua posição e ordem de empilhamento reais. Conecte diretamente ou estenda com Add Layer. | LAYERS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`

# ByteDance Seedream 5.0 Pro Separação de Camadas

ByteDance Seedream 5.0 Pro Layer Separation decompõe uma imagem em uma placa de fundo e até 16 camadas transparentes, cada uma com sua própria ordem de empilhamento, caixa delimitadora, nome e descrição. Ele retorna o fundo, imagens por camada com máscaras, caixas de posicionamento e uma pilha de camadas pronta para edição.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `imagem` | A imagem a ser separada. Exatamente uma imagem, com pelo menos 512x512 pixels e proporção de aspecto entre 1:16 e 16:1. Entradas maiores que cerca de 4 MP são reduzidas antes do envio. | IMAGE | Sim | Imagem única |
| `prompt` | Como separar a imagem. Deixe vazio para detectar automaticamente e separar todos os elementos principais. Descreva os elementos em linguagem natural para controlar a separação, ou segmente regiões exatas com tags `<bbox>left top right bottom</bbox>` (coordenadas de 0 a 1000 por mil). Padrão: string vazia. | STRING | Sim | Texto multilinha |
| `tamanho` | Nível de resolução da saída. "auto" segue o tamanho da imagem de entrada (limitado ao intervalo de 1K a 2K). Padrão: "auto". | COMBO | Sim | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Semente a ser usada para a geração. Padrão: 0. | INT | Sim | 0 a 2147483647 |
| `otimização do prompt` | Modo de otimização do prompt: "standard" oferece maior qualidade, "fast" tempo de geração mais curto. Padrão: "standard". | COMBO | Não | "standard"<br>"fast" |
| `marca d'água` | Se deve adicionar uma marca d'água "AI generated" às imagens. Padrão: false. | BOOLEAN | Não | false<br>true |
| `recortar camadas` | Geometria das saídas em lote de camadas/máscaras (layer_stack não é afetada e é sempre ajustada). Canvas completo: cada camada em um canvas do tamanho da base, posicionada em sua caixa delimitadora — recomponha diretamente com ImageCompositeMasked. Tamanho mínimo: cada camada cortada para sua caixa delimitadora (com padding até a maior camada para compor o lote) — tensores muito menores; reconstrua o posicionamento com Layers From Bounding Boxes usando a saída bboxes. Padrão: false (canvas completo). | BOOLEAN | Não | false (canvas completo)<br>true (tamanho mínimo) |

Nota: a entrada `image` deve ser uma única imagem; lotes não são suportados. A imagem deve ter pelo menos 512x512 pixels e proporção de aspecto entre 1:16 e 16:1.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---------------|-------------|---------------|
| `imagem base` | A imagem base (placa de fundo) sobre a qual as camadas são empilhadas. | IMAGE |
| `máscara base` | Transparência da imagem base (1 = transparente, convenção do LoadImage); atualmente sempre totalmente opaca. | MASK |
| `camadas` | Camadas transparentes ordenadas de baixo para cima. Modo canvas completo: posicionadas em um canvas preto do tamanho da base, em sua posição da caixa delimitadora. Modo tamanho mínimo: cortadas para sua caixa delimitadora, ancoradas no canto superior esquerdo, com padding até a maior camada. | IMAGE |
| `máscaras` | Transparência por camada, alinhada por índice ao lote de camadas (1 = transparente, convenção do LoadImage). Para composição no estilo ImageCompositeMasked, adicione InvertMask antes. | MASK |
| `bboxes` | Uma caixa de posicionamento por camada, alinhada por índice ao lote de camadas (forneça ambas, além das máscaras, ao Layers From Bounding Boxes para reconstruir o posicionamento por camada): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` é a região de conteúdo da camada dentro do próprio quadro; ela é posicionada no canvas na posição da caixa mais esse deslocamento. | BOUNDING_BOX |
| `pilha de camadas` | Documento de camadas pronto para edição para o Create Layered Image: a placa de base mais cada elemento como uma camada nomeada e recortada com precisão, em sua posição real e ordem de empilhamento. Conecte diretamente ou estenda com Add Layer. | LAYERS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`

# LayersFromBoundingBoxes

Este nó converte um lote de imagens e suas caixas delimitadoras em uma pilha de camadas, criando uma camada por quadro e posicionando cada camada de acordo com sua caixa correspondente. Use-o quando um nó emitir camadas como um lote, pois um lote carrega apenas um único posicionamento para cada quadro e as posições individuais seriam perdidas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `image` | Lote de imagens; cada quadro torna-se uma camada. | IMAGE | Sim | — |
| `bboxes` | Caixas de posicionamento, alinhadas por índice com o lote de imagens. Aceita caixas delimitadoras (x, y, largura, altura), elementos normalizados (com um "bbox" — que precisam de canvas_width/canvas_height para serem resolvidos em pixels) ou uma string JSON de qualquer um desses. Quadros sem uma caixa correspondente são posicionados na origem. A largura/altura de uma caixa dimensiona a camada para ajustar-se a ela. metadata.name (ou desc) e metadata.z_index são usados quando presentes, e metadata.content_rect (relativo ao quadro) recorta o quadro para seu conteúdo real. | BOUNDING_BOX, ARRAY ou STRING | Sim | — |
| `mask` | Transparência por quadro, alinhada por índice com o lote de imagens (1 = transparente, convenção do LoadImage). | MASK | Não | — |
| `layers` | Pilha de camadas à qual anexar. Deixe desconectado para iniciar uma nova pilha. | LAYERS | Não | — |
| `crop_to_content` | Recorta cada quadro para metadata.content_rect quando presente e posiciona o conteúdo na posição da caixa mais o deslocamento do retângulo. Mantenha ativado para lotes cujos quadros são preenchidos — ele mantém apenas o conteúdo real em seu lugar verdadeiro. (padrão: true) | BOOLEAN | Não | true<br>false |
| `canvas_width` | Largura da tela do documento. 0 a deriva das camadas posicionadas. (padrão: 0) | INT | Não | 0 a MAX_RESOLUTION |
| `canvas_height` | Altura da tela do documento. 0 a deriva das camadas posicionadas. (padrão: 0) | INT | Não | 0 a MAX_RESOLUTION |

Notas:

- `bboxes` e `mask` devem estar alinhados por índice com `image`: a enésima caixa e o enésimo quadro de máscara correspondem ao enésimo quadro de imagem. Quadros sem uma caixa correspondente são posicionados na origem.
- Quando `bboxes` contém elementos normalizados (com um "bbox"), `canvas_width` e `canvas_height` devem ser fornecidos para que essas posições normalizadas possam ser resolvidas em pixels.
- `canvas_width` e `canvas_height` devem ser ambos maiores que 0 para definir a tela do documento explicitamente. Se algum deles for 0, a tela é derivada das camadas posicionadas ou herdada da pilha de camadas `layers` conectada.
- Quando `layers` está conectada, novas camadas são anexadas a ela e recebem valores de z-index acima do maior z-index já presente na pilha.
- Quando `crop_to_content` está ativado e um quadro possui metadata.content_rect, o quadro é recortado para esse retângulo e o redimensionamento de largura/altura da caixa não é aplicado; em vez disso, o deslocamento do retângulo é adicionado à posição da caixa.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `LAYERS` | A pilha de camadas, pronta para Create Layered Image. | LAYERS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LayersFromBoundingBoxes/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a70956bf0d7ea8bdbd16767ed8b19600b274a6eeb745728f95219578adc73712`

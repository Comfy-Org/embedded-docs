# Desenhar BBoxes

O nó DrawBBoxes visualiza resultados de detecção de objetos desenhando caixas delimitadoras, rótulos e pontuações de confiança em uma imagem. Se nenhuma imagem de entrada for fornecida, ele cria uma tela em branco grande o suficiente para conter todas as caixas desenhadas. Ele suporta processamento em lote, permitindo desenhar diferentes conjuntos de detecções para múltiplas imagens ou repetir as mesmas detecções em um lote.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A(s) imagem(ns) de entrada para desenhar as caixas delimitadoras. Se não for fornecida, uma tela em branco será gerada. | IMAGE | Não | - |
| `bboxes` | Uma lista de dicionários de caixas delimitadoras. Cada dicionário deve conter as chaves `x`, `y`, `width`, `height` e, opcionalmente, `label` e `score`. | BOUNDINGBOX | Sim | - |

**Restrições de Entrada:**
*   A entrada `bboxes` é obrigatória e deve ser fornecida.
*   O nó lida automaticamente com diferentes formatos de entrada para `bboxes`. Um único dicionário será aplicado a todas as imagens no lote. Uma lista simples de dicionários será tratada como o mesmo conjunto de detecções para cada imagem. Uma lista de listas permite especificar diferentes detecções para cada imagem no lote.
*   Se uma `image` não for fornecida, o nó criará uma imagem em branco com dimensões grandes o suficiente para acomodar todas as caixas delimitadoras fornecidas, com um tamanho mínimo padrão de 640x640.
*   O campo `label` é comparado com as classes do conjunto de dados COCO, então cada classe mantém uma cor consistente. Um rótulo que não é uma classe COCO também é desenhado e recebe uma das cores restantes na ordem de primeira aparição, e uma caixa sem `score` é desenhada apenas com o rótulo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `out_image` | A(s) imagem(ns) de saída com as caixas delimitadoras, rótulos e pontuações de confiança sobrepostos. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DrawBBoxes/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3a25677852fe1f0c137a011628ba0197034c3724281941f88a27e1ae1abfe48e`

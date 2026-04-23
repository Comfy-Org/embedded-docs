> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DrawBBoxes/pt-BR.md)

O nó DrawBBoxes visualiza resultados de detecção de objetos desenhando caixas delimitadoras, rótulos e pontuações de confiança em uma imagem. Se nenhuma imagem de entrada for fornecida, ele cria uma tela em branco grande o suficiente para conter todas as caixas desenhadas. Ele suporta processamento em lote, permitindo desenhar diferentes conjuntos de detecções para várias imagens ou repetir as mesmas detecções em um lote.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|---------------|-------------|-----------|-----------|
| `image` | IMAGE | Não | - | A(s) imagem(ns) de entrada para desenhar as caixas delimitadoras. Se não for fornecida, uma tela em branco será gerada. |
| `bboxes` | BOUNDINGBOX | Sim | - | Uma lista de dicionários de caixas delimitadoras. Cada dicionário deve conter chaves para `x`, `y`, `width`, `height` e, opcionalmente, `label` e `score`. |

**Restrições de Entrada:**
*   A entrada `bboxes` é obrigatória e deve ser fornecida.
*   O nó lida automaticamente com diferentes formatos de entrada para `bboxes`. Um único dicionário será aplicado a todas as imagens no lote. Uma lista simples de dicionários será tratada como o mesmo conjunto de detecções para cada imagem. Uma lista de listas permite especificar diferentes detecções para cada imagem no lote.
*   Se uma `image` não for fornecida, o nó criará uma imagem em branco com dimensões grandes o suficiente para acomodar todas as caixas delimitadoras fornecidas, com um tamanho mínimo padrão de 640x640.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `out_image` | IMAGE | A(s) imagem(ns) de saída com as caixas delimitadoras, rótulos e pontuações de confiança sobrepostos. |
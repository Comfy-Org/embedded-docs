> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/pt-BR.md)

O nó PrimitiveBoundingBox cria uma área retangular simples definida por sua posição e tamanho. Ele recebe coordenadas X e Y para o canto superior esquerdo, juntamente com valores de largura e altura, e gera uma estrutura de dados de caixa delimitadora que pode ser usada por outros nós em um fluxo de trabalho.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `x` | INT | Não | 0 a 8192 | A coordenada X para o canto superior esquerdo da caixa delimitadora (padrão: 0). |
| `y` | INT | Não | 0 a 8192 | A coordenada Y para o canto superior esquerdo da caixa delimitadora (padrão: 0). |
| `width` | INT | Não | 1 a 8192 | A largura da caixa delimitadora (padrão: 512). |
| `height` | INT | Não | 1 a 8192 | A altura da caixa delimitadora (padrão: 512). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `bounding_box` | BOUNDING_BOX | Uma estrutura de dados contendo as propriedades `x`, `y`, `width` e `height` do retângulo definido. |

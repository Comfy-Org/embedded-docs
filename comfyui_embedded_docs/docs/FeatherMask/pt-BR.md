> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FeatherMask/pt-BR.md)

O nó `FeatherMask` aplica um efeito de esmaecimento (feathering) nas bordas de uma máscara fornecida, suavizando suas bordas ao ajustar a opacidade com base em distâncias especificadas a partir de cada borda. Isso cria um efeito de borda mais suave e mesclado.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|---------------|-----------|
| `mask`    | MASK          | A máscara à qual o efeito de esmaecimento será aplicado. Ela determina a área da imagem que será afetada pelo esmaecimento. |
| `esquerda`    | INT           | Especifica a distância a partir da borda esquerda dentro da qual o efeito de esmaecimento será aplicado. |
| `topo`     | INT           | Especifica a distância a partir da borda superior dentro da qual o efeito de esmaecimento será aplicado. |
| `direita`   | INT           | Especifica a distância a partir da borda direita dentro da qual o efeito de esmaecimento será aplicado. |
| `inferior`  | INT           | Especifica a distância a partir da borda inferior dentro da qual o efeito de esmaecimento será aplicado. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|---------------|-----------|
| `mask`    | MASK          | A saída é uma versão modificada da máscara de entrada, com um efeito de esmaecimento aplicado às suas bordas. |
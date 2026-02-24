> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FeatherMask/pt-BR.md)

O nó `FeatherMask` aplica um efeito de esfumaçamento às bordas de uma máscara fornecida, realizando uma transição suave das bordas da máscara ao ajustar sua opacidade com base em distâncias específicas de cada borda. Isso cria um efeito de borda mais suave e mesclado.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|--------------|-------------|
| `mask`    | MASK         | A máscara à qual o efeito de esfumaçamento será aplicado. Ela determina a área da imagem que será afetada pelo esfumaçamento. |
| `left`    | INT          | Especifica a distância a partir da borda esquerda dentro da qual o efeito de esfumaçamento será aplicado. |
| `top`     | INT          | Especifica a distância a partir da borda superior dentro da qual o efeito de esfumaçamento será aplicado. |
| `right`   | INT          | Especifica a distância a partir da borda direita dentro da qual o efeito de esfumaçamento será aplicado. |
| `bottom`  | INT          | Especifica a distância a partir da borda inferior dentro da qual o efeito de esfumaçamento será aplicado. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|--------------|-------------|
| `mask`    | MASK         | A saída é uma versão modificada da máscara de entrada com um efeito de esfumaçamento aplicado às suas bordas. |

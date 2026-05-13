> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrowMask/pt-BR.md)

O nó `GrowMask` foi projetado para modificar o tamanho de uma máscara fornecida, expandindo-a ou contraindo-a, além de aplicar opcionalmente um efeito suavizado nos cantos. Essa funcionalidade é essencial para ajustar dinamicamente os limites da máscara em tarefas de processamento de imagens, permitindo um controle mais flexível e preciso sobre a área de interesse.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `mask`    | MASK        | A máscara de entrada a ser modificada. Este parâmetro é central para a operação do nó, servindo como base sobre a qual a máscara será expandida ou contraída. |
| `expand`  | INT         | Determina a magnitude e a direção da modificação da máscara. Valores positivos fazem a máscara expandir, enquanto valores negativos resultam em contração. Este parâmetro influencia diretamente o tamanho final da máscara. |
| `tapered_corners` | BOOLEAN    | Um sinalizador booleano que, quando definido como True, aplica um efeito suavizado nos cantos da máscara durante a modificação. Essa opção permite transições mais suaves e resultados visualmente agradáveis. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `mask`    | MASK        | A máscara modificada após aplicar a expansão/contração especificada e o efeito opcional de cantos suavizados. |
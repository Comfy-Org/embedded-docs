> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrowMask/pt-BR.md)

O nó `GrowMask` é projetado para modificar o tamanho de uma máscara fornecida, expandindo-a ou contraindo-a, enquanto aplica opcionalmente um efeito afilado aos cantos. Essa funcionalidade é crucial para ajustar dinamicamente os limites da máscara em tarefas de processamento de imagem, permitindo um controle mais flexível e preciso sobre a área de interesse.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `mask`    | MASK        | A máscara de entrada a ser modificada. Este parâmetro é central para a operação do nó, servindo como base sobre a qual a máscara é expandida ou contraída. |
| `expand`  | INT         | Determina a magnitude e a direção da modificação da máscara. Valores positivos fazem a máscara expandir, enquanto valores negativos levam à contração. Este parâmetro influencia diretamente o tamanho final da máscara. |
| `tapered_corners` | BOOLEAN    | Um sinalizador booleano que, quando definido como Verdadeiro, aplica um efeito afilado aos cantos da máscara durante a modificação. Esta opção permite transições mais suaves e resultados visualmente mais agradáveis. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `mask`    | MASK        | A máscara modificada após a aplicação da expansão/contração especificada e do efeito opcional de cantos afilados. |

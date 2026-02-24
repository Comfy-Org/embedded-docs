> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ThresholdMask/pt-BR.md)

O nó ThresholdMask converte uma máscara em uma máscara binária aplicando um valor de limiar. Ele compara cada pixel na máscara de entrada com o valor de limiar especificado e cria uma nova máscara onde os pixels acima do limiar se tornam 1 (branco) e os pixels abaixo ou iguais ao limiar se tornam 0 (preto).

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `mask` | MASK | Sim | - | A máscara de entrada a ser processada |
| `value` | FLOAT | Sim | 0.0 - 1.0 | O valor de limiar para binarização (padrão: 0.5) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `mask` | MASK | A máscara binária resultante após a aplicação do limiar |

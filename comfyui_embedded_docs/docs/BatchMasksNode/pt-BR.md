> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchMasksNode/pt-BR.md)

O nó Batch Masks combina várias entradas de máscaras individuais em um único lote. Ele recebe um número variável de entradas de máscara e as emite como um único tensor de máscara em lote, permitindo o processamento em lote de máscaras em nós subsequentes.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `mask_0` | MASK | Sim | - | A primeira entrada de máscara. |
| `mask_1` | MASK | Sim | - | A segunda entrada de máscara. |
| `mask_2` a `mask_49` | MASK | Não | - | Entradas de máscara adicionais opcionais. O nó pode aceitar um mínimo de 2 e um máximo de 50 máscaras no total. |

**Observação:** Este nó utiliza um modelo de entrada de crescimento automático. Você deve conectar pelo menos duas máscaras (`mask_0` e `mask_1`). É possível adicionar até 48 entradas de máscara opcionais adicionais (`mask_2` até `mask_49`) para um total de 50 máscaras. Todas as máscaras conectadas serão combinadas em um único lote.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | MASK | Uma única máscara em lote contendo todas as máscaras de entrada empilhadas juntas. |

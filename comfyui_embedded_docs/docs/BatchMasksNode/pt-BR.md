# Máscaras em Lote

O nó Batch Masks combina várias entradas de máscara individuais em um único lote. Ele recebe um número variável de entradas de máscara e as gera como um único tensor de máscara em lote, permitindo o processamento em lote de máscaras em nós subsequentes. Se as máscaras de entrada tiverem tamanhos diferentes, elas são redimensionadas automaticamente para corresponder às dimensões da primeira máscara.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `mask` | As entradas de máscara a serem combinadas em um lote. Pelo menos uma máscara é obrigatória. Você pode adicionar até 50 máscaras no total clicando no botão "+" no nó. Se as máscaras tiverem tamanhos diferentes, elas são redimensionadas automaticamente para corresponder às dimensões da primeira máscara. | MASK | Sim | 1 a 50 máscaras |

**Nota:** Este nó usa um modelo de entrada com crescimento automático. Você deve conectar pelo menos uma máscara. Você pode adicionar até mais 49 entradas de máscara, totalizando 50 máscaras. Todas as máscaras conectadas serão combinadas em um único lote. Se as máscaras tiverem alturas ou larguras diferentes, elas serão redimensionadas automaticamente para corresponder às dimensões da primeira máscara usando interpolação bilinear.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | Uma única máscara em lote contendo todas as máscaras de entrada empilhadas juntas. Se nenhuma máscara for fornecida, retorna None. | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchMasksNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7e9bc4be72c7fa8fceab2cf167c72b7e1ff858c0281d977f2ad3ab433d9d58d6`

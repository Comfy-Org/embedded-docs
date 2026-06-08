O nó **Agrupar Máscaras** combina múltiplas entradas de máscaras individuais em um único lote. Ele aceita um número variável de entradas de máscaras e as agrupa em um único tensor de máscara em lote, permitindo o processamento em lote de máscaras em nós subsequentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `mask_0` | A primeira entrada de máscara. | MASK | Sim | - |
| `mask_1` | A segunda entrada de máscara. | MASK | Sim | - |
| `mask_2` a `mask_49` | Entradas de máscara opcionais adicionais. O nó pode aceitar um mínimo de 2 e um máximo de 50 máscaras no total. | MASK | Não | - |

**Observação:** Este nó utiliza um modelo de entrada com crescimento automático. Você deve conectar pelo menos duas máscaras (`mask_0` e `mask_1`). É possível adicionar até 48 entradas de máscara opcionais adicionais (`mask_2` a `mask_49`), totalizando 50 máscaras. Todas as máscaras conectadas serão combinadas em um único lote.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | Uma única máscara em lote contendo todas as máscaras de entrada empilhadas. | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchMasksNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8eb7a2a2d8108b619387b049d92348b8e9fc6d5e94e78c856c8520b88cdf77f2`

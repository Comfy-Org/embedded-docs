# Condicionamento (Combinar)

Este nó combina duas entradas de condicionamento em uma única saída, mesclando efetivamente suas informações. As duas condições são combinadas usando concatenação de listas.

## Entradas

| Nome do Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `condicionamento_1` | A primeira entrada de condicionamento a ser combinada. Tem importância igual à `condicionamento_2` no processo de combinação. | `CONDITIONING` |
| `condicionamento_2` | A segunda entrada de condicionamento a ser combinada. Tem importância igual à `condicionamento_1` no processo de combinação. | `CONDITIONING` |

## Saídas

| Nome do Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `conditioning` | O resultado da combinação de `condicionamento_1` e `condicionamento_2`, encapsulando as informações mescladas. | `CONDITIONING` |

## Cenários de Uso

Compare os dois grupos abaixo: o lado esquerdo usa o nó ConditioningCombine, enquanto o lado direito mostra a saída normal.

![Comparar](./asset/compare.jpg)

Neste exemplo, as duas condições usadas em `Conditioning Combine` têm importância equivalente. Portanto, você pode usar diferentes codificações de texto para estilo de imagem, características do assunto, etc., permitindo que os atributos do prompt sejam gerados de forma mais completa. O segundo prompt usa o prompt completo combinado, mas a compreensão semântica pode codificar condições completamente diferentes.

Usando este nó, você pode alcançar:

- **Mesclagem básica de texto:** Conecte as saídas de dois nós `CLIP Text Encode` às duas portas de entrada do `Conditioning Combine`
- **Combinação complexa de prompts:** Combine prompts positivos e negativos, ou codifique separadamente descrições principais e descrições de estilo antes de mesclar
- **Combinação em cadeia condicional:** Vários nós `Conditioning Combine` podem ser usados em série para alcançar a combinação gradual de múltiplas condições

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningCombine/pt-BR.md)

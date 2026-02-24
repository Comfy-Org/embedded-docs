> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningCombine/pt-BR.md)

Este nó combina duas entradas de condicionamento em uma única saída, efetivamente mesclando suas informações. As duas condições são combinadas usando concatenação de listas.

## Entradas

| Nome do Parâmetro    | Tipo de Dados      | Descrição |
|----------------------|--------------------|-------------|
| `conditioning_1`     | `CONDITIONING`     | A primeira entrada de condicionamento a ser combinada. Tem importância igual a `conditioning_2` no processo de combinação. |
| `conditioning_2`     | `CONDITIONING`     | A segunda entrada de condicionamento a ser combinada. Tem importância igual a `conditioning_1` no processo de combinação. |

## Saídas

| Nome do Parâmetro    | Tipo de Dados      | Descrição |
|----------------------|--------------------|-------------|
| `conditioning`       | `CONDITIONING`     | O resultado da combinação de `conditioning_1` e `conditioning_2`, encapsulando as informações mescladas. |

## Cenários de Uso

Compare os dois grupos abaixo: o lado esquerdo usa o nó ConditioningCombine, enquanto o lado direito mostra a saída normal.

![Comparação](./asset/compare.jpg)

Neste exemplo, as duas condições usadas no `Conditioning Combine` têm importância equivalente. Portanto, você pode usar diferentes codificações de texto para estilo de imagem, características do assunto, etc., permitindo que as características do prompt sejam geradas de forma mais completa. O segundo prompt usa o prompt completo combinado, mas o entendimento semântico pode codificar condições completamente diferentes.

Usando este nó, você pode alcançar:

- **Mesclagem básica de texto:** Conecte as saídas de dois nós `CLIP Text Encode` às duas portas de entrada do `Conditioning Combine`.
- **Combinação complexa de prompts:** Combine prompts positivos e negativos, ou codifique separadamente descrições principais e descrições de estilo antes de mesclá-las.
- **Combinação em cadeia de condições:** Múltiplos nós `Conditioning Combine` podem ser usados em série para alcançar uma combinação gradual de várias condições.

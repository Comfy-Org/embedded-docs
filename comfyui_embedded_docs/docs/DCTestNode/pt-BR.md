# DCTestNode

DCTestNode é um nó de lógica que retorna diferentes tipos de dados com base na seleção do usuário em uma caixa de combinação dinâmica. Ele funciona como um roteador condicional, em que a opção escolhida determina qual campo de entrada fica ativo e que tipo de valor o nó produzirá. O nó é marcado como um nó de saída no ComfyUI.

## Entradas

O nó usa um seletor dinâmico de combinação: o parâmetro `combo` está sempre visível, e os outros campos de entrada aparecem somente quando a opção correspondente é selecionada.

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `combo` | A seleção principal que determina qual campo de entrada fica ativo e o que o nó produzirá. | DYNAMIC_COMBO | Sim | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |

### Entradas de option1

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `string` | Um campo de entrada de texto. Este campo só fica ativo e obrigatório quando `combo` está definido como `"option1"`. | STRING | Sim | - |

### Entradas de option2

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `integer` | Um campo de entrada de número inteiro. Este campo só fica ativo e obrigatório quando `combo` está definido como `"option2"`. | INT | Sim | - |

### Entradas de option3

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image` | Um campo de entrada de imagem. Este campo só fica ativo e obrigatório quando `combo` está definido como `"option3"`. | IMAGE | Sim | - |

### Entradas de option4

Quando `combo` está definido como `"option4"`, o nó mostra um segundo seletor dinâmico de combinação (`subcombo`) que controla um conjunto aninhado de campos de entrada.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `subcombo` | Uma seleção dinâmica de combinação secundária que aparece quando `combo` está definido como `"option4"`. Ela determina quais campos de entrada aninhados ficam ativos. | DYNAMIC_COMBO | Sim | `"opt1"`<br>`"opt2"` |
| `float_x` | Uma entrada de número decimal. Este campo só fica ativo e obrigatório quando `combo` está definido como `"option4"` e `subcombo` está definido como `"opt1"`. | FLOAT | Sim | - |
| `float_y` | Uma entrada de número decimal. Este campo só fica ativo e obrigatório quando `combo` está definido como `"option4"` e `subcombo` está definido como `"opt1"`. | FLOAT | Sim | - |
| `mask1` | Um campo de entrada de máscara. Este campo só fica ativo quando `combo` está definido como `"option4"` e `subcombo` está definido como `"opt2"`. Ele é opcional. | MASK | Não | - |

**Restrições dos parâmetros:**

* O parâmetro `combo` controla a visibilidade e a obrigatoriedade de todos os outros campos de entrada. Somente as entradas associadas à opção selecionada de `combo` serão exibidas e serão obrigatórias (exceto `mask1`, que é opcional).
* Quando `combo` está definido como `"option4"`, o parâmetro `subcombo` torna-se obrigatório e controla um segundo conjunto de entradas aninhadas (`float_x`/`float_y` ou `mask1`).
* Se `combo` receber um valor que não seja uma das quatro opções listadas, o nó lança um erro.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `output` | A saída depende da opção `combo` selecionada. Pode ser um STRING (`"option1"`), um INT (`"option2"`), um IMAGE (`"option3"`) ou uma representação em string do valor de `subcombo` (`"option4"`). | ANYTYPE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9dd616a427a56eddb78b48d6eea6f71419b7097d417afae5557132b333641e69`

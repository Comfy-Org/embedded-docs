# DCTestNode

O nó DCTestNode é um nó lógico que retorna diferentes tipos de dados com base na seleção do usuário em uma caixa de combinação dinâmica. Ele atua como um roteador condicional, onde a opção escolhida determina qual campo de entrada está ativo e que tipo de valor o nó irá emitir.

## Entradas

O seletor `combo` está sempre visível. Os campos de entrada exibidos abaixo dele dependem da opção selecionada.

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `combo` | A seleção principal que determina qual campo de entrada está ativo e o que o nó irá emitir. | DYNAMIC_COMBO | Sim | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |

### option1 Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `string` | Um campo de entrada de texto. Este campo só fica ativo e é obrigatório quando `combo` está definido como `"option1"`. | STRING | Sim | - |

### option2 Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `integer` | Um campo de entrada de número inteiro. Este campo só fica ativo e é obrigatório quando `combo` está definido como `"option2"`. | INT | Sim | - |

### option3 Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image` | Um campo de entrada de imagem. Este campo só fica ativo e é obrigatório quando `combo` está definido como `"option3"`. | IMAGE | Sim | - |

### option4 Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `subcombo` | Uma seleção secundária que aparece quando `combo` está definido como `"option4"`. Ela determina quais campos de entrada aninhados estão ativos. | DYNAMIC_COMBO | Sim | `"opt1"`<br>`"opt2"` |

#### opt1 Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `float_x` | Um campo de entrada de número decimal. Este campo só fica ativo e é obrigatório quando `combo` está definido como `"option4"` e `subcombo` está definido como `"opt1"`. | FLOAT | Sim | - |
| `float_y` | Um campo de entrada de número decimal. Este campo só fica ativo e é obrigatório quando `combo` está definido como `"option4"` e `subcombo` está definido como `"opt1"`. | FLOAT | Sim | - |

#### opt2 Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `mask1` | Um campo de entrada de máscara. Este campo só fica ativo quando `combo` está definido como `"option4"` e `subcombo` está definido como `"opt2"`. Ele é opcional. | MASK | Não | - |

**Restrições dos parâmetros:**

* O parâmetro `combo` controla a visibilidade e a obrigatoriedade de todos os outros campos de entrada. Somente os campos associados à opção `combo` selecionada são exibidos e obrigatórios (exceto `mask1`, que é opcional).
* Quando `combo` está definido como `"option4"`, o parâmetro `subcombo` se torna ativo e obrigatório e controla um segundo conjunto de campos aninhados: `"opt1"` exibe `float_x` e `float_y`; `"opt2"` exibe `mask1`.
* Se `combo` for definido com um valor inesperado, o nó lança um ValueError.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | A saída depende da opção `combo` selecionada. Pode ser uma STRING (`"option1"`), um INT (`"option2"`), uma IMAGE (`"option3"`) ou uma representação em string do dicionário `subcombo` (`"option4"`). | ANYTYPE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9dd616a427a56eddb78b48d6eea6f71419b7097d417afae5557132b333641e69`

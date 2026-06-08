Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/en.md)

O DCTestNode é um nó lógico que retorna diferentes tipos de dados com base na seleção do usuário em uma caixa de combinação dinâmica. Ele atua como um roteador condicional, onde a opção escolhida determina qual campo de entrada está ativo e qual tipo de valor o nó irá gerar.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `combo` | A seleção principal que determina qual campo de entrada está ativo e o que o nó irá gerar. | COMBO | Sim | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |
| `string` | Um campo de entrada de texto. Este campo só fica ativo e obrigatório quando `combo` está definido como `"option1"`. | STRING | Não | - |
| `integer` | Um campo de entrada de número inteiro. Este campo só fica ativo e obrigatório quando `combo` está definido como `"option2"`. | INT | Não | - |
| `image` | Um campo de entrada de imagem. Este campo só fica ativo e obrigatório quando `combo` está definido como `"option3"`. | IMAGE | Não | - |
| `subcombo` | Uma seleção secundária que aparece quando `combo` está definido como `"option4"`. Ela determina quais campos de entrada aninhados estão ativos. | COMBO | Não | `"opt1"`<br>`"opt2"` |
| `float_x` | Uma entrada de número decimal. Este campo só fica ativo e obrigatório quando `combo` está definido como `"option4"` e `subcombo` está definido como `"opt1"`. | FLOAT | Não | - |
| `float_y` | Uma entrada de número decimal. Este campo só fica ativo e obrigatório quando `combo` está definido como `"option4"` e `subcombo` está definido como `"opt1"`. | FLOAT | Não | - |
| `mask1` | Um campo de entrada de máscara. Este campo só fica ativo quando `combo` está definido como `"option4"` e `subcombo` está definido como `"opt2"`. É opcional. | MASK | Não | - |

**Restrições dos Parâmetros:**

* O parâmetro `combo` controla a visibilidade e a obrigatoriedade de todos os outros campos de entrada. Apenas as entradas associadas à opção `combo` selecionada serão exibidas e serão obrigatórias (exceto `mask1`, que é opcional).
* Quando `combo` está definido como `"option4"`, o parâmetro `subcombo` se torna obrigatório e controla um segundo conjunto de entradas aninhadas (`float_x`/`float_y` ou `mask1`).

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A saída depende da opção `combo` selecionada. Pode ser uma STRING (`"option1"`), um INT (`"option2"`), uma IMAGE (`"option3"`) ou uma representação em string do dicionário `subcombo` (`"option4"`). | ANYTYPE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `98c4ca2100a27594df360935cc1507960480fe75a76ca0df2af75925d399be00`

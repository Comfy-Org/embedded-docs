> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/pt-BR.md)

O DCTestNode é um nó lógico que retorna diferentes tipos de dados com base na seleção do usuário em uma caixa de combinação dinâmica. Ele atua como um roteador condicional, onde a opção escolhida determina qual campo de entrada está ativo e que tipo de valor o nó irá produzir.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `combo` | COMBO | Sim | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` | A seleção principal que determina qual campo de entrada está ativo e o que o nó irá produzir. |
| `string` | STRING | Não | - | Um campo de entrada de texto. Este campo só está ativo e é obrigatório quando `combo` está definido como `"option1"`. |
| `integer` | INT | Não | - | Um campo de entrada para números inteiros. Este campo só está ativo e é obrigatório quando `combo` está definido como `"option2"`. |
| `image` | IMAGE | Não | - | Um campo de entrada de imagem. Este campo só está ativo e é obrigatório quando `combo` está definido como `"option3"`. |
| `subcombo` | COMBO | Não | `"opt1"`<br>`"opt2"` | Uma seleção secundária que aparece quando `combo` está definido como `"option4"`. Ela determina quais campos de entrada aninhados estão ativos. |
| `float_x` | FLOAT | Não | - | Uma entrada para número decimal. Este campo só está ativo e é obrigatório quando `combo` está definido como `"option4"` e `subcombo` está definido como `"opt1"`. |
| `float_y` | FLOAT | Não | - | Uma entrada para número decimal. Este campo só está ativo e é obrigatório quando `combo` está definido como `"option4"` e `subcombo` está definido como `"opt1"`. |
| `mask1` | MASK | Não | - | Um campo de entrada de máscara. Este campo só está ativo quando `combo` está definido como `"option4"` e `subcombo` está definido como `"opt2"`. É opcional. |

**Restrições dos Parâmetros:**

* O parâmetro `combo` controla a visibilidade e a obrigatoriedade de todos os outros campos de entrada. Somente as entradas associadas à opção `combo` selecionada serão mostradas e serão obrigatórias (exceto `mask1`, que é opcional).
* Quando `combo` está definido como `"option4"`, o parâmetro `subcombo` torna-se obrigatório e controla um segundo conjunto de entradas aninhadas (`float_x`/`float_y` ou `mask1`).

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | ANYTYPE | A saída depende da opção `combo` selecionada. Pode ser uma STRING (`"option1"`), um INT (`"option2"`), uma IMAGE (`"option3"`), ou uma representação em string do dicionário `subcombo` (`"option4"`). |

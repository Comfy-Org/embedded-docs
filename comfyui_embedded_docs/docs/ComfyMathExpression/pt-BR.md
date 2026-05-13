> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/pt-BR.md)

O nó ComfyMathExpression avalia uma fórmula matemática usando um conjunto de valores de entrada. Você pode escrever uma expressão usando nomes de variáveis (como `a`, `b`, `c`), e o nó calculará o resultado. Ele suporta a adição dinâmica de quantos valores de entrada forem necessários para seu cálculo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `expression` | STRING | Sim | N/A | A fórmula matemática a ser avaliada. Você pode usar nomes de variáveis que correspondam aos valores de entrada (padrão: "a + b"). |
| `values` | FLOAT, INT, BOOLEAN | Não | N/A | Um conjunto de entradas numéricas ou booleanas que podem ser adicionadas dinamicamente. Cada entrada recebe uma letra do alfabeto (a, b, c, ...) para ser usada como variável na expressão. |

**Restrições dos Parâmetros:**
*   O parâmetro `expression` não pode estar vazio ou conter apenas espaços em branco.
*   A expressão deve resultar em um valor numérico finito (INT ou FLOAT). Valores booleanos ou outros resultados não numéricos causarão um erro.
*   Os valores de entrada para o parâmetro `values` podem ser números (INT ou FLOAT) ou valores booleanos (TRUE/FALSE).

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `FLOAT` | FLOAT | O resultado da expressão matemática como um número de ponto flutuante. |
| `INT` | INT | O resultado da expressão matemática como um número inteiro. |
| `BOOL` | BOOLEAN | O resultado da expressão matemática como um valor booleano. |

---
**Source fingerprint (SHA-256):** `962f82684d9dc58a67a57e6738d6d2ed457d7f30288cedb21fd46b5c655c1708`

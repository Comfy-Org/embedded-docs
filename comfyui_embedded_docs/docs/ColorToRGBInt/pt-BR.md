# Cor para RGB Int

O nó **ColorToRGBInt** converte uma cor fornecida em formato hexadecimal (como `#FF5733`) em um único valor inteiro RGB. Ele extrai os componentes vermelho, verde e azul da string de cor, combina-os em um inteiro e também retorna a representação hexadecimal original e o valor alpha (opacidade).

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `cor` | Um valor de cor no formato hexadecimal `#RRGGBB` ou `#RRGGBBAA`. Deve ter 7 ou 9 caracteres e começar com `#`. | COLOR | Sim | `#RRGGBB`<br>`#RRGGBBAA` |

**Observação:** A string de entrada `color` deve seguir o formato `#RRGGBB` ou `#RRGGBBAA`. Se não tiver 7 ou 9 caracteres, não começar com `#` ou contiver caracteres hexadecimais inválidos, o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `rgb_int` | O valor inteiro RGB calculado, derivado da fórmula: `(Red * 65536) + (Green * 256) + Blue`. | INT |
| `hex` | A string hexadecimal de cor no formato `#RRGGBB`. Se a entrada incluiu um canal alpha, ele é removido desta saída. | COLOR |
| `alpha` | O valor alpha (opacidade) entre 0.0 e 1.0. É igual a 1.0 quando a entrada é `#RRGGBB`, ou o valor do canal alpha dividido por 255 quando a entrada é `#RRGGBBAA`. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4e64616d168beee73bca4364d47e2a089418b5046a76bfcfa061dfab9a5e49ed`

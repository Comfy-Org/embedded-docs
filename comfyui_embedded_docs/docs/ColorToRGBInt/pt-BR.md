# Cor para RGB Int

O nó **ColorToRGBInt** converte uma cor especificada em formato hexadecimal (como `#FF5733`) em um único valor inteiro RGB. Ele extrai os componentes vermelho, verde e azul da string de cor e os combina em um inteiro, além de retornar a representação hexadecimal. Cores com canal alfa (`#RRGGBBAA`) também são suportadas, e o valor alfa é retornado separadamente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `color` | Um valor de cor no formato hexadecimal `#RRGGBB` ou `#RRGGBBAA`. Deve ter exatamente 7 ou 9 caracteres e começar com `#`. | COLOR | Sim | `#RRGGBB`<br>`#RRGGBBAA` |

**Nota:** A string de entrada `color` deve seguir exatamente o formato `#RRGGBB` ou `#RRGGBBAA`. Se a string não tiver 7 ou 9 caracteres, não começar com `#` ou contiver caracteres que não sejam dígitos hexadecimais válidos, o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `rgb_int` | O valor inteiro RGB calculado, derivado da fórmula: `(Red * 65536) + (Green * 256) + Blue`. | INT |
| `hex` | A string de cor hexadecimal no formato `#RRGGBB`. Se a entrada incluir um canal alfa, ele é removido desta saída. | COLOR |
| `alpha` | O valor alfa (opacidade) como um número de 0.0 a 1.0. Para cores de entrada com canal alfa (`#RRGGBBAA`), é o valor alfa de dois dígitos dividido por 255. Para cores sem canal alfa, é 1.0. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4e64616d168beee73bca4364d47e2a089418b5046a76bfcfa061dfab9a5e49ed`

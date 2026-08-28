# Conversão de Número

O nó Number Convert transforma vários tipos de dados de entrada em valores numéricos. Ele aceita uma única entrada do tipo inteiro, float, string ou booleano e produz duas saídas: um número de ponto flutuante e um inteiro. Isso é útil para converter texto ou valores lógicos em um formato que possa ser usado por outros nós matemáticos ou de processamento no seu fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `valor` | O valor a ser convertido em saídas numéricas. Aceita um inteiro, um número de ponto flutuante, uma string de texto ou um booleano true/false. | INT, FLOAT, STRING, BOOLEAN | Sim | N/A |

**Nota:** Quando a entrada é uma string, ela não deve estar vazia e deve conter uma representação válida de um número (ex.: `"123"`, `"3.14"`). O nó gerará um erro para strings vazias, texto que não possa ser interpretado como número ou valores que não sejam finitos (como `"inf"` ou `"nan"`). Para entradas booleanas, `true` é convertido para 1.0 (FLOAT) e 1 (INT), enquanto `false` é convertido para 0.0 (FLOAT) e 0 (INT). Para entradas float e para strings que contenham um número decimal, a saída inteira é obtida truncando-se a parte decimal.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `FLOAT` | O valor de entrada convertido para um número de ponto flutuante. | FLOAT |
| `INT` | O valor de entrada convertido para um inteiro. Para entradas float, isso realiza um truncamento. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d6a774bf7c3ad9482b2275adc6ccc9e47c82b1f35f11c5a241b00efd29526f94`

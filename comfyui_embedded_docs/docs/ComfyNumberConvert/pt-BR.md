# Conversão de Número

O nó Number Convert transforma vários tipos de dados de entrada em valores numéricos. Ele aceita uma única entrada dos tipos inteiro, ponto flutuante, string ou booleano e produz duas saídas: um número de ponto flutuante e um número inteiro. Isso é útil para converter texto ou valores lógicos em um formato que possa ser usado por outros nós matemáticos ou de processamento no seu fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `value` | O valor a ser convertido em saídas numéricas. Aceita um número inteiro, um número de ponto flutuante, uma string de texto ou um booleano true/false. | INT, FLOAT, STRING, BOOLEAN | Sim | N/A |

**Observação:** Quando a entrada é uma string, ela não pode estar vazia e deve conter uma representação válida de um número (por exemplo, `"123"`, `"3.14"`). O nó gerará um erro para strings vazias, texto que não puder ser interpretado como número ou valores que não forem finitos (como `"inf"` ou `"nan"`). Para entradas booleanas, `true` é convertido para 1.0 (FLOAT) e 1 (INT), enquanto `false` é convertido para 0.0 (FLOAT) e 0 (INT). Para entradas de ponto flutuante e para strings que contêm um número decimal, a saída INT é obtida truncando a parte decimal.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `FLOAT` | O valor de entrada convertido em um número de ponto flutuante. | FLOAT |
| `INT` | O valor de entrada convertido em um número inteiro. Para entradas de ponto flutuante e strings decimais, isso realiza um truncamento. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d6a774bf7c3ad9482b2275adc6ccc9e47c82b1f35f11c5a241b00efd29526f94`

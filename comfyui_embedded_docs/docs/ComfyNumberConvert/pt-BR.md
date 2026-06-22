# Conversão de Número

O nó Number Convert transforma vários tipos de dados de entrada em valores numéricos. Ele aceita uma única entrada dos tipos inteiro, ponto flutuante, string ou booleano e produz duas saídas: um número de ponto flutuante e um número inteiro. Isso é útil para converter valores de texto ou lógicos em um formato que possa ser utilizado por outros nós matemáticos ou de processamento no seu fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `valor` | O valor a ser convertido em saídas numéricas. Aceita um número inteiro, um número de ponto flutuante, uma string de texto ou um valor booleano verdadeiro/falso. | INT, FLOAT, STRING, BOOLEAN | Sim | N/A |

**Observação:** Quando a entrada é uma string, ela não pode estar vazia e deve conter uma representação válida de um número (por exemplo, `"123"`, `"3.14"`). O nó gerará um erro para strings vazias, texto que não possa ser interpretado como número ou valores que não sejam finitos (como `"inf"` ou `"nan"`). Para entradas booleanas, `true` é convertido para 1.0 (FLOAT) e 1 (INT), enquanto `false` é convertido para 0.0 (FLOAT) e 0 (INT). Para entradas do tipo float, a saída inteira é obtida truncando a parte decimal.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `FLOAT` | O valor de entrada convertido para um número de ponto flutuante. | FLOAT |
| `INT` | O valor de entrada convertido para um número inteiro. Para entradas do tipo float, isso realiza um truncamento. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/pt-BR.md)

---
**Source fingerprint (SHA-256):** `961fbea05b22c68f768f9ecaae2ee455b1913afe4a65d8c0e6b6497b1e24ce72`

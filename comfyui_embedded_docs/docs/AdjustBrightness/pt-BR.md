# Ajustar Brilho

O nó Ajustar Brilho modifica o brilho de uma imagem de entrada. Ele funciona multiplicando o valor de cada pixel por um fator especificado e, em seguida, limitando os valores resultantes para permanecerem dentro de um intervalo válido. Um fator de 1,0 mantém a imagem inalterada, valores abaixo de 1,0 a escurecem e valores acima de 1,0 a clareiam.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image` | A imagem de entrada a ser ajustada. | IMAGE | Sim | - |
| `fator` | Fator de brilho. 1,0 = sem alteração, <1,0 = mais escuro, >1,0 = mais claro. (padrão: 1,0) | FLOAT | Não | 0,0 - 2,0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem de saída com o brilho ajustado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c8f2fbb5fa149812a2ecd1ff9fce7bd6d29bf4c48b929e9ebc0a95c9e46ec65e`

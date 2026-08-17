# LatentCut

O nó LatentCut extrai uma seção específica de amostras latentes ao longo de uma dimensão escolhida. Ele permite cortar uma parte da representação latente especificando a dimensão (x, y ou t), a posição inicial e a quantidade a extrair. O nó lida com indexação positiva e negativa e ajusta automaticamente a quantidade de extração para permanecer dentro dos limites disponíveis.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `samples` | As amostras latentes de entrada das quais extrair | LATENT | Sim | - |
| `dim` | A dimensão ao longo da qual cortar as amostras latentes | COMBO | Sim | "x"<br>"y"<br>"t" |
| `index` | A posição inicial para o corte (padrão: 0). Valores positivos contam a partir do início, valores negativos contam a partir do final. O nó ajusta automaticamente o índice para permanecer dentro do intervalo válido das amostras latentes | INT | Sim | -16384 a 16384 |
| `amount` | O número de elementos a extrair ao longo da dimensão especificada (padrão: 1). O nó reduz automaticamente esse valor se exceder os dados disponíveis além do índice inicial | INT | Sim | 1 a 16384 |

Nota: `x` corta ao longo da última dimensão do tensor latente, `y` ao longo da penúltima dimensão e `t` ao longo da antepenúltima dimensão. Quando `index` é positivo, ele é limitado à última posição válida da dimensão escolhida; quando negativo, é limitado para não apontar antes do início dos dados. `amount` é reduzido sempre que o corte solicitado se estender além dos dados disponíveis.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | A parte extraída das amostras latentes | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7682de2644a4b85dba0571406f9f9802eca7caab09dc2ccf1ac91dc13b41bcdf`

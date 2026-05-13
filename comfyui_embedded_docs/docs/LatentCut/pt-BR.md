> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/pt-BR.md)

O nó LatentCut extrai uma seção específica de amostras latentes ao longo de uma dimensão escolhida. Ele permite recortar uma parte da representação latente especificando a dimensão (x, y ou t), a posição inicial e a quantidade a ser extraída. O nó lida com indexação positiva e negativa e ajusta automaticamente a quantidade de extração para permanecer dentro dos limites disponíveis.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `amostras` | LATENT | Sim | - | As amostras latentes de entrada das quais extrair |
| `dimensão` | COMBO | Sim | "x"<br>"y"<br>"t" | A dimensão ao longo da qual cortar as amostras latentes |
| `índice` | INT | Sim | -16384 a 16384 | A posição inicial para o corte (padrão: 0). Valores positivos contam a partir do início, valores negativos contam a partir do final. O nó ajusta automaticamente o índice para permanecer dentro do intervalo válido das amostras latentes |
| `quantidade` | INT | Sim | 1 a 16384 | O número de elementos a extrair ao longo da dimensão especificada (padrão: 1). O nó reduz automaticamente esse valor se exceder os dados disponíveis além do índice inicial |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | LATENT | A porção extraída das amostras latentes |

---
**Source fingerprint (SHA-256):** `54f2b0cead9dce2c2cbd241d4e8c50ce85a67d3e1a40e7002056b83acbf0cf2d`

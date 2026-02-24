> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/pt-BR.md)

O nó LatentCut extrai uma seção específica de amostras latentes ao longo de uma dimensão escolhida. Ele permite que você recorte uma porção da representação latente especificando a dimensão (x, y ou t), a posição inicial e a quantidade a ser extraída. O nó lida com indexação positiva e negativa e ajusta automaticamente a quantidade de extração para permanecer dentro dos limites disponíveis.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Sim | - | As amostras latentes de entrada das quais extrair |
| `dim` | COMBO | Sim | "x"<br>"y"<br>"t" | A dimensão ao longo da qual cortar as amostras latentes |
| `index` | INT | Não | -16384 a 16384 | A posição inicial para o corte (padrão: 0). Valores positivos contam a partir do início, valores negativos contam a partir do final |
| `amount` | INT | Não | 1 a 16384 | O número de elementos a extrair ao longo da dimensão especificada (padrão: 1) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | LATENT | A porção extraída das amostras latentes |

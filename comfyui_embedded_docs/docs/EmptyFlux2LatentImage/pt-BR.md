> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/pt-BR.md)

O nó EmptyFlux2LatentImage cria uma representação latente em branco e vazia. Ele gera um tensor preenchido com zeros, que serve como ponto de partida para o processo de remoção de ruído do modelo Flux. As dimensões do latente são determinadas pela largura e altura de entrada, reduzidas por um fator de 16.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Sim | 16 a 8192 | A largura da imagem final a ser gerada. A largura latente será este valor dividido por 16. O valor padrão é 1024. |
| `height` | INT | Sim | 16 a 8192 | A altura da imagem final a ser gerada. A altura latente será este valor dividido por 16. O valor padrão é 1024. |
| `batch_size` | INT | Não | 1 a 4096 | O número de amostras latentes a serem geradas em um único lote. O valor padrão é 1. |

**Observação:** As entradas `width` e `height` devem ser divisíveis por 16, pois o nó as divide internamente por este fator para criar as dimensões latentes.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `samples` | LATENT | Um tensor latente preenchido com zeros. A forma é `[batch_size, 128, height // 16, width // 16]`. |

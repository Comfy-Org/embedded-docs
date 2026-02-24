> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetImageSize/pt-BR.md)

O nó GetImageSize extrai as dimensões e informações de lote de uma imagem de entrada. Ele retorna a largura, altura e o tamanho do lote da imagem, além de exibir essas informações como texto de progresso na interface do nó. Os dados originais da imagem passam inalterados.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada da qual extrair as informações de tamanho |
| `unique_id` | UNIQUE_ID | Não | - | Identificador interno usado para exibir informações de progresso |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `width` | INT | A largura da imagem de entrada em pixels |
| `height` | INT | A altura da imagem de entrada em pixels |
| `batch_size` | INT | O número de imagens no lote |

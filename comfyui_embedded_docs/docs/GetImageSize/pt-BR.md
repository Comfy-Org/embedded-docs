> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetImageSize/pt-BR.md)

O nó GetImageSize extrai as dimensões e informações de lote de uma imagem de entrada. Ele retorna a largura, altura e tamanho do lote da imagem, exibindo também essas informações como texto de progresso na interface do nó. Os dados originais da imagem passam sem alterações.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | - | A imagem de entrada da qual extrair informações de tamanho |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `width` | INT | A largura da imagem de entrada em pixels |
| `height` | INT | A altura da imagem de entrada em pixels |
| `batch_size` | INT | O número de imagens no lote |

---
**Source fingerprint (SHA-256):** `5cd19ae762d2403c6c5d0740cd5f8c17913daea737fddcff8f0d9da2210e82ab`

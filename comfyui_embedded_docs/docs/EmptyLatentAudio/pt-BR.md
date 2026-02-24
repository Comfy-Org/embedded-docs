> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/pt-BR.md)

O nó EmptyLatentAudio cria tensores latentes vazios para processamento de áudio. Ele gera uma representação latente de áudio em branco com duração e tamanho de lote especificados, que pode ser usada como entrada para fluxos de trabalho de geração ou processamento de áudio. O nó calcula as dimensões latentes apropriadas com base na duração do áudio e na taxa de amostragem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `seconds` | FLOAT | Sim | 1.0 - 1000.0 | A duração do áudio em segundos (padrão: 47.6) |
| `batch_size` | INT | Sim | 1 - 4096 | O número de imagens latentes no lote (padrão: 1) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Retorna um tensor latente vazio para processamento de áudio com a duração e o tamanho de lote especificados |

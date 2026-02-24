> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/pt-BR.md)

O nó EmptyCosmosLatentVideo cria um tensor de vídeo latente vazio com dimensões especificadas. Ele gera uma representação latente preenchida com zeros que pode ser usada como ponto de partida para fluxos de trabalho de geração de vídeo, com parâmetros configuráveis de largura, altura, duração e tamanho do lote.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Sim | 16 a MAX_RESOLUTION | A largura do vídeo latente em pixels (padrão: 1280, deve ser divisível por 16) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION | A altura do vídeo latente em pixels (padrão: 704, deve ser divisível por 16) |
| `length` | INT | Sim | 1 a MAX_RESOLUTION | O número de quadros no vídeo latente (padrão: 121) |
| `batch_size` | INT | Não | 1 a 4096 | O número de vídeos latentes a serem gerados em um lote (padrão: 1) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `samples` | LATENT | O tensor de vídeo latente vazio gerado, com valores zero |

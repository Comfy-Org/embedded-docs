> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/pt-BR.md)

O nó EmptyLTXVLatentVideo cria um tensor latente vazio para processamento de vídeo. Ele gera um ponto de partida em branco com dimensões especificadas que pode ser usado como entrada para fluxos de trabalho de geração de vídeo. O nó produz uma representação latente preenchida com zeros com a largura, altura, comprimento e tamanho do lote configurados.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `width` | INT | Sim | 64 a MAX_RESOLUTION | A largura do tensor de vídeo latente (padrão: 768, passo: 32) |
| `height` | INT | Sim | 64 a MAX_RESOLUTION | A altura do tensor de vídeo latente (padrão: 512, passo: 32) |
| `length` | INT | Sim | 1 a MAX_RESOLUTION | O número de quadros no vídeo latente (padrão: 97, passo: 8) |
| `batch_size` | INT | Não | 1 a 4096 | O número de vídeos latentes a serem gerados em um lote (padrão: 1) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `samples` | LATENT | O tensor latente vazio gerado com valores zero nas dimensões especificadas |

---
**Source fingerprint (SHA-256):** `c3ee9374210e100a074b238ce7ac8b5d2d2d415efd3318c9a6a7c8f7e20bda84`

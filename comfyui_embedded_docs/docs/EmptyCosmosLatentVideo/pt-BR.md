# EmptyCosmosLatentVideo

O nó `EmptyCosmosLatentVideo` cria um tensor de vídeo latente vazio com dimensões especificadas. Ele gera uma representação latente preenchida com zeros que pode ser usada como ponto de partida para fluxos de trabalho de geração de vídeo, com parâmetros configuráveis de largura, altura, comprimento e tamanho do lote. As dimensões espaciais do latente são reduzidas por um fator de 8.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `width` | A largura do vídeo latente em pixels (padrão: 1280, deve ser divisível por 16) | INT | Sim | 16 to MAX_RESOLUTION |
| `height` | A altura do vídeo latente em pixels (padrão: 704, deve ser divisível por 16) | INT | Sim | 16 to MAX_RESOLUTION |
| `length` | O número de quadros no vídeo latente (padrão: 121, deve ser divisível por 8) | INT | Sim | 1 to MAX_RESOLUTION |
| `batch_size` | O número de vídeos latentes a serem gerados em um lote (padrão: 1) | INT | Sim | 1 to 4096 |

O tensor latente utiliza 16 canais. As dimensões espaciais são divididas por 8 em comparação às dimensões em pixels (altura // 8, largura // 8), e a contagem de quadros é comprimida para ((comprimento - 1) // 8) + 1 quadros latentes.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `samples` | O tensor de vídeo latente vazio gerado, com valores zero. Formato: (batch_size, 16, ((length - 1) // 8) + 1, height // 8, width // 8) | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`

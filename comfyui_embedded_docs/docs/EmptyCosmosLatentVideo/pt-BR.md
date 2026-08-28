# EmptyCosmosLatentVideo

EmptyCosmosLatentVideo cria um tensor de vídeo latente vazio com as dimensões especificadas. Ele gera uma representação latente preenchida com zeros que pode ser usada como ponto de partida para fluxos de trabalho de geração de vídeo, com parâmetros configuráveis de largura, altura, comprimento e tamanho do lote.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `largura` | A largura do vídeo latente em pixels (padrão: 1280, incrementos de 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | A altura do vídeo latente em pixels (padrão: 704, incrementos de 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | O número de quadros no vídeo latente (padrão: 121, incrementos de 8) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de vídeos latentes a serem gerados em um lote (padrão: 1) | INT | Não | 1 a 4096 |

Nota: O tensor latente é reduzido espacialmente por um fator de 8 tanto na altura quanto na largura e contém 16 canais. O número de quadros temporais latentes é calculado como `((length - 1) // 8) + 1`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `samples` | O tensor de vídeo latente vazio gerado, com valores zero | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`

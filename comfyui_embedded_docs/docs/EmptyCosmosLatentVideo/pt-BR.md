O nó EmptyCosmosLatentVideo cria um tensor de vídeo latente vazio com dimensões especificadas. Ele gera uma representação latente preenchida com zeros que pode ser usada como ponto de partida para fluxos de trabalho de geração de vídeo, com parâmetros configuráveis de largura, altura, comprimento e tamanho do lote.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `largura` | A largura do vídeo latente em pixels (padrão: 1280, deve ser divisível por 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | A altura do vídeo latente em pixels (padrão: 704, deve ser divisível por 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | O número de quadros no vídeo latente (padrão: 121, deve ser divisível por 8) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de vídeos latentes a serem gerados em um lote (padrão: 1) | INT | Não | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | O tensor de vídeo latente vazio gerado, com valores zero | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f473820af3faf7cb6992ff1959089801e333df395b4007abeb9b504962bfc73b`

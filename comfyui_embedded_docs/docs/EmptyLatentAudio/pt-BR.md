# Empty Latent Audio

O nó EmptyLatentAudio cria um tensor latente vazio para processamento de áudio. Ele gera uma representação latente de áudio em branco com uma duração e tamanho de lote especificados, que pode ser usada como ponto de partida para fluxos de trabalho de geração ou processamento de áudio. O nó calcula automaticamente as dimensões latentes apropriadas com base na duração do áudio e na taxa de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `seconds` | A duração do áudio em segundos (padrão: 47.6) | FLOAT | Sim | 1.0 - 1000.0 (passo 0.1) |
| `batch_size` | O número de imagens latentes no lote (padrão: 1) | INT | Sim | 1 - 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | Retorna um tensor latente vazio para processamento de áudio com a duração e o tamanho do lote especificados. O tensor tem o formato [batch_size, 64, length], em que length é calculado a partir da duração do áudio e da taxa de amostragem. A saída também inclui metadados que indicam que o tipo é "audio" e um fator de redução temporal de 2048. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6ca63d26febe2d87ff751a57044eb81b553b19756f4b3f9478ecb5a733ec0041`

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/pt-BR.md)

O nó EmptyLatentAudio cria um tensor latente vazio para processamento de áudio. Ele gera uma representação latente de áudio em branco com duração e tamanho de lote especificados, que pode ser usada como ponto de partida para fluxos de trabalho de geração ou processamento de áudio. O nó calcula automaticamente as dimensões latentes apropriadas com base na duração do áudio e na taxa de amostragem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `segundos` | FLOAT | Sim | 1.0 - 1000.0 | A duração do áudio em segundos (padrão: 47.6) |
| `tamanho_do_lote` | INT | Sim | 1 - 4096 | O número de imagens latentes no lote (padrão: 1) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `LATENT` | LATENT | Retorna um tensor latente vazio para processamento de áudio com a duração e o tamanho do lote especificados. O tensor tem a forma [batch_size, 64, length], onde length é calculado a partir da duração do áudio e da taxa de amostragem. |

---
**Source fingerprint (SHA-256):** `004f730131b179fe5ac072afe81b2e01a3937fceca5a260b4ae66f92774e96d9`

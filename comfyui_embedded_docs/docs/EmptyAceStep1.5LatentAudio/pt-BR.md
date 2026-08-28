# EmptyAceStep1.5LatentAudio

O nó Empty Ace Step 1.5 Latent Audio cria um tensor latente vazio projetado para processamento de áudio. Ele gera um latente de áudio silencioso com uma duração e tamanho de lote especificados, que pode ser usado como ponto de partida para fluxos de trabalho de geração de áudio no ComfyUI. O nó calcula o comprimento do latente com base nos segundos de entrada e em uma taxa de amostragem fixa.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `seconds` | A duração do áudio a ser gerado, em segundos (padrão: 120.0). | FLOAT | Sim | 1.0 - 1000.0 |
| `batch_size` | O número de imagens latentes no lote (padrão: 1). | INT | Sim | 1 - 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | Um tensor latente vazio representando áudio silencioso, com um identificador de tipo "audio". A saída também inclui um valor `downscale_ratio_temporal` de 1764, que é usado para a redução da escala temporal no processamento de áudio. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bb7120c91ce5d779147cb8553d6f96fa160d87468d4d87550fb6dd4ec89b1557`

# EmptyAceStep1.5LatentAudio

O nó Empty Ace Step 1.5 Latent Audio cria um tensor latente de áudio vazio (silencioso) para fluxos de trabalho de geração de áudio. Ele constrói um latente com 64 canais cujo comprimento temporal é calculado a partir da duração solicitada e o identifica como dados de áudio para uso por nós de áudio subsequentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `seconds` | A duração do áudio a gerar, em segundos (padrão: 120.0). O comprimento do latente é calculado como `seconds * 48000 / 1920`, arredondado para o número inteiro mais próximo. | FLOAT | Sim | 1.0 - 1000.0 (passo: 0.01) |
| `batch_size` | O número de imagens latentes no lote (padrão: 1). | INT | Sim | 1 - 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | Um tensor latente vazio representando áudio silencioso. O tensor tem formato [batch_size, 64, length], onde length é derivado de `seconds`. A saída também inclui um identificador de tipo "audio" e um valor `downscale_ratio_temporal` de 1764, que é usado para redução de escala temporal no processamento de áudio. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bb7120c91ce5d779147cb8553d6f96fa160d87468d4d87550fb6dd4ec89b1557`

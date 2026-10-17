# Get Audio Latent Size

Lê um latent de áudio e retorna seu comprimento, a contagem de canais de áudio e o tamanho do lote, para que esses valores possam ser reutilizados sem decodificar o áudio. Use-o para dimensionar máscaras de ruído ou igualar os comprimentos de áudio e vídeo antes da amostragem. Os valores medidos também são impressos no próprio nó.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `latent` | O latent de áudio ou de áudio/vídeo a ser inspecionado. Quando o latent contém vários fluxos, o fluxo de áudio é medido. | LATENT | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `length` | O comprimento do latent de áudio, em células do latent, e não em amostras de áudio. | INT |
| `audio_channels` | O número de canais de áudio. Latents sem uma dimensão de canal de áudio reportam um canal. | INT |
| `batch_size` | O número de latents no lote. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetAudioLatentSize/pt-BR.md)

---
**Source fingerprint (SHA-256):** `82bac0636a070d14a8845c3f4a5e73359c1d943ce223be3b93212ef25d44b1a8`

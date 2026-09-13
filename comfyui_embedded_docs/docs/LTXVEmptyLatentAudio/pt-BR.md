# LTXV Áudio Latente Vazio

O nó LTXV Empty Latent Audio cria um lote de tensores latentes de áudio vazios (preenchidos com zeros). Ele lê a configuração de um modelo Audio VAE conectado para determinar as dimensões latentes corretas, como o número de canais e bins de frequência, e calcula quantos latentes de áudio são necessários a partir da contagem de frames e da taxa de frames. O latente vazio resultante pode ser usado como ponto de partida para fluxos de trabalho de geração ou manipulação de áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `frames_number` | Número de frames. O valor padrão é 97. | INT | Sim | 1 a 1000 |
| `frame_rate` | Número de frames por segundo. O valor padrão é 25.0. Esta entrada aceita valores FLOAT ou INT. | FLOAT | Sim | 1.0 a 1000.0 |
| `batch_size` | O número de amostras de áudio latentes no lote. O valor padrão é 1. | INT | Sim | 1 a 4096 |
| `audio_vae` | O modelo Audio VAE do qual obter a configuração. Exibido como "Audio VAE". | VAE | Sim | N/A |

**Nota:** A entrada `audio_vae` é obrigatória. O nó gera um erro se ela não for fornecida.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `Latent` | Um tensor latente de áudio vazio com o shape (batch_size, z_channels, num_audio_latents, audio_freq), em que a contagem de canais e os bins de frequência vêm do Audio VAE e o número de latentes de áudio é derivado de `frames_number` e `frame_rate`. A saída também inclui um campo `type` definido como "audio". | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`

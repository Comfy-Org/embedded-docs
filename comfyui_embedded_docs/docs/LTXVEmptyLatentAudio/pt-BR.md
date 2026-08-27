# LTXV Áudio Latente Vazio

O nó LTXV Empty Latent Audio cria um lote de tensores de áudio latente vazios (preenchidos com zeros). Ele usa a configuração de um modelo Audio VAE fornecido para determinar as dimensões corretas para o espaço latente, como o número de canais e bins de frequência, e calcula o número de latentes de áudio a partir da contagem de quadros e da taxa de quadros. Esse latente vazio serve como ponto de partida para fluxos de trabalho de geração ou manipulação de áudio no ComfyUI.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `frames_number` | Número de quadros. O valor padrão é 97. | INT | Sim | 1 a 1000 |
| `frame_rate` | Número de quadros por segundo. O valor padrão é 25.0. Aceita valores FLOAT ou INT. | FLOAT | Sim | 1.0 a 1000.0 |
| `batch_size` | O número de amostras de áudio latente no lote. O valor padrão é 1. | INT | Sim | 1 a 4096 |
| `audio_vae` | O modelo Audio VAE do qual obter a configuração. Este parâmetro é obrigatório. | VAE | Sim | N/A |

**Nota:** A entrada `audio_vae` é obrigatória. O nó gerará um erro se ela não for fornecida.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `Latent` | Um tensor de áudio latente vazio com a estrutura (batch_size, z_channels, num_audio_latents, audio_freq) configurado para corresponder ao Audio VAE de entrada. A saída também inclui um campo `type` definido como "audio". | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`

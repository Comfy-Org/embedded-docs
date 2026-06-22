# LTXV Áudio Latente Vazio

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/en.md)

O nó LTXV Empty Latent Audio cria um lote de tensores latentes de áudio vazios (preenchidos com zeros). Ele utiliza a configuração de um modelo Audio VAE fornecido para determinar as dimensões corretas do espaço latente, como o número de canais e bins de frequência. Esse latente vazio serve como ponto de partida para fluxos de trabalho de geração ou manipulação de áudio no ComfyUI.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `frames_number` | Número de quadros. O valor padrão é 97. | INT | Sim | 1 a 1000 |
| `frame_rate` | Número de quadros por segundo. O valor padrão é 25. | INT | Sim | 1 a 1000 |
| `batch_size` | O número de amostras latentes de áudio no lote. O valor padrão é 1. | INT | Sim | 1 a 4096 |
| `audio_vae` | O modelo Audio VAE para obter a configuração. Este parâmetro é obrigatório. | VAE | Sim | N/A |

**Nota:** A entrada `audio_vae` é obrigatória. O nó gerará um erro se ela não for fornecida.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `Latent` | Um tensor latente de áudio vazio com a estrutura (batch_size, z_channels, num_audio_latents, audio_freq) configurado para corresponder ao Audio VAE de entrada. A saída também inclui um campo `type` definido como "audio". | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1a8bfea98f14de014069016652b39542cfd9290cae2d870ab4e381e46aa1e08f`

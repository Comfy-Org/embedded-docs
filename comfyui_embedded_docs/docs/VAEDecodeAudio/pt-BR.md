# VAE Decodificar Áudio

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `samples` | As amostras de áudio codificadas no espaço latente que serão decodificadas de volta para a forma de onda de áudio | LATENT | Sim | - |
| `vae` | O modelo Autoencoder Variacional usado para decodificar as amostras latentes em áudio | VAE | Sim | - |

Nota: Se `samples` contiver dados latentes aninhados, apenas o último elemento é usado para a decodificação.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `AUDIO` | A forma de onda de áudio decodificada com volume normalizado e taxa de amostragem (padrão: 44100 Hz, ou a taxa de amostragem de `samples` de entrada, se houver) | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`

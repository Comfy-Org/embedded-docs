# VAE Codificar Áudio

O nó VAE Encode Audio converte dados de áudio em uma representação latente usando um Autoencoder Variacional (VAE). Ele processa o áudio de entrada através do VAE para produzir amostras latentes comprimidas que podem ser usadas para tarefas adicionais de geração ou manipulação de áudio. Se a taxa de amostragem do áudio for diferente da taxa de amostragem esperada pelo VAE, o áudio é reamostrado automaticamente antes da codificação.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `audio` | Os dados de áudio a serem codificados, contendo informações de forma de onda e taxa de amostragem | AUDIO | Sim | - |
| `vae` | O modelo de Autoencoder Variacional usado para codificar o áudio no espaço latente | VAE | Sim | - |

**Observação:** A entrada de áudio é reamostrada automaticamente para corresponder à taxa de amostragem esperada pelo VAE (padrão: 44100 Hz) se a taxa de amostragem original for diferente desse valor. Se o áudio de entrada for None (por exemplo, quando o vídeo de origem não tiver faixa de áudio), o nó gerará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | A representação codificada do áudio no espaço latente, contendo amostras comprimidas | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `224563af40a377a37209b26ec8becf035560da273b18293634f684e18c5e63ed`

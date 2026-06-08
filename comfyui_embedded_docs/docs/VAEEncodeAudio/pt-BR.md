O nó VAEEncodeAudio converte dados de áudio em uma representação latente usando um Autoencoder Variacional (VAE). Ele recebe uma entrada de áudio e a processa através do VAE para gerar amostras latentes comprimidas que podem ser usadas para tarefas posteriores de geração ou manipulação de áudio. O nó reamostra automaticamente o áudio para corresponder à taxa de amostragem esperada pelo VAE, se necessário, antes da codificação.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `áudio` | Os dados de áudio a serem codificados, contendo informações de forma de onda e taxa de amostragem | AUDIO | Sim | - |
| `vae` | O modelo de Autoencoder Variacional usado para codificar o áudio no espaço latente | VAE | Sim | - |

**Observação:** A entrada de áudio é reamostrada automaticamente para corresponder à taxa de amostragem esperada pelo VAE (padrão: 44100 Hz) se a taxa de amostragem original for diferente deste valor.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `LATENT` | A representação de áudio codificada no espaço latente, contendo amostras comprimidas | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `db509ab571154c4cedbfc6cae6591bd2b67b2c6e2261766565cdb0205b2c2ecc`

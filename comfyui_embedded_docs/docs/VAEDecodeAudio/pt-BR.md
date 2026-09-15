# VAE Decodificar Áudio

Este nó converte uma representação latente de áudio de volta em uma forma de onda de áudio reproduzível usando um Autoencoder Variacional (VAE). Ele recebe as amostras codificadas, decodifica-as através da VAE selecionada e, em seguida, normaliza a forma de onda resultante para que o nível de volume geral permaneça consistente. O áudio de saída usa a taxa de amostragem de áudio da VAE (44100 Hz por padrão), ou a taxa de amostragem armazenada nas amostras de entrada quando houver uma.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `amostras` | As amostras de áudio codificadas no espaço latente que serão decodificadas de volta para uma forma de onda de áudio. Se as amostras tiverem sua própria taxa de amostragem, esse valor será usado para a saída. | LATENT | Sim | - |
| `vae` | O modelo Autoencoder Variacional usado para decodificar as amostras latentes em áudio. Sua taxa de amostragem de saída de áudio (padrão 44100 Hz) determina a taxa de amostragem da forma de onda resultante quando as amostras de entrada não especificam uma. | VAE | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `AUDIO` | A forma de onda de áudio decodificada com volume normalizado, retornada juntamente com sua taxa de amostragem (a taxa de amostragem das amostras de entrada `samples` se presente; caso contrário, a taxa de amostragem de áudio da VAE, padrão 44100 Hz). | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`

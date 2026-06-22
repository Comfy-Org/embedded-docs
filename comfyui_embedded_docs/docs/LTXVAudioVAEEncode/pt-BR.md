# LTXV Codificar Áudio VAE

O nó LTXV Audio VAE Encode recebe uma entrada de áudio e a comprime em uma representação latente menor, utilizando um modelo Audio VAE específico. Esse processo é essencial para gerar ou manipular áudio dentro de um fluxo de trabalho de espaço latente, pois converte dados brutos de áudio em um formato que outros nós no pipeline possam entender e processar.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `áudio` | O áudio a ser codificado. | AUDIO | Sim | - |
| `audio_vae` | O modelo Audio VAE a ser usado para codificação. | VAE | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `Audio Latent` | A representação latente comprimida do áudio de entrada. A saída inclui as amostras latentes, a taxa de amostragem do modelo VAE e um identificador de tipo. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fc10d8bbdca5150b7c87adb52960b8690397c3d003c89f9ec6a8410c541a347f`

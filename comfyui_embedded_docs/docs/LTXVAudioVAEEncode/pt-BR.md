> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/pt-BR.md)

O nó LTXV Audio VAE Encode recebe uma entrada de áudio e a comprime em uma representação latente menor, utilizando um modelo Audio VAE específico. Esse processo é essencial para gerar ou manipular áudio dentro de um fluxo de trabalho de espaço latente, pois converte dados brutos de áudio em um formato que outros nós no pipeline possam entender e processar.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `áudio` | AUDIO | Sim | - | O áudio a ser codificado. |
| `audio_vae` | VAE | Sim | - | O modelo Audio VAE a ser usado para codificação. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `Audio Latent` | LATENT | A representação latente comprimida do áudio de entrada. A saída inclui as amostras latentes, a taxa de amostragem do modelo VAE e um identificador de tipo. |

---
**Source fingerprint (SHA-256):** `fc10d8bbdca5150b7c87adb52960b8690397c3d003c89f9ec6a8410c541a347f`

# LTXV Codificar Áudio VAE

O nó LTXV Audio VAE Encode recebe uma entrada de áudio e a compacta em uma representação latente menor, usando um modelo Audio VAE especificado. Esse processo é essencial para gerar ou manipular áudio em um fluxo de trabalho de espaço latente, pois converte os dados de áudio brutos em um formato que outros nós no pipeline podem entender e processar.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `audio` | O áudio a ser codificado. | AUDIO | Sim | - |
| `audio_vae` | O modelo Audio VAE a ser usado para codificação. | VAE | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `Audio Latent` | A representação latente compactada do áudio de entrada. A saída inclui as amostras latentes, a taxa de amostragem do modelo VAE e um identificador de tipo. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `68f70e0f8048cd9ba723f52eefc93cc33564eb3e68c0cb9b677964dc99aecb97`

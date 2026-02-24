> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/pt-BR.md)

O nó **LTXV Audio VAE Encode** recebe uma entrada de áudio e a comprime em uma representação latente menor usando um modelo de Audio VAE especificado. Este processo é essencial para gerar ou manipular áudio em um fluxo de trabalho de espaço latente, pois converte os dados brutos de áudio em um formato que outros nós no *pipeline* podem entender e processar.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sim | - | O áudio a ser codificado. |
| `audio_vae` | VAE | Sim | - | O modelo de Audio VAE a ser usado para a codificação. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `Audio Latent` | LATENT | A representação latente comprimida do áudio de entrada. A saída inclui as amostras latentes, a taxa de amostragem do modelo VAE e um identificador de tipo. |

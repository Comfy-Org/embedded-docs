> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/pt-BR.md)

O nó VAEEncodeAudio converte dados de áudio em uma representação latente usando um Autoencoder Variacional (VAE). Ele recebe uma entrada de áudio e a processa através do VAE para gerar amostras latentes comprimidas que podem ser usadas para tarefas posteriores de geração ou manipulação de áudio. O nó reamostra automaticamente o áudio para 44100 Hz, se necessário, antes da codificação.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sim | - | Os dados de áudio a serem codificados, contendo informações de forma de onda e taxa de amostragem |
| `vae` | VAE | Sim | - | O modelo de Autoencoder Variacional usado para codificar o áudio no espaço latente |

**Observação:** A entrada de áudio é automaticamente reamostrada para 44100 Hz se a taxa de amostragem original for diferente deste valor.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `LATENT` | LATENT | A representação codificada do áudio no espaço latente, contendo amostras comprimidas |

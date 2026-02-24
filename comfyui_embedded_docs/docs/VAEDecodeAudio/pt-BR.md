> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/pt-BR.md)

O nó VAEDecodeAudio converte representações latentes de volta em formas de onda de áudio usando um Autoencoder Variacional. Ele recebe amostras de áudio codificadas e as processa através do VAE para reconstruir o áudio original, aplicando normalização para garantir níveis de saída consistentes. O áudio resultante é retornado com uma taxa de amostragem padrão de 44100 Hz.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Sim | - | As amostras de áudio codificadas no espaço latente que serão decodificadas de volta para a forma de onda de áudio |
| `vae` | VAE | Sim | - | O modelo de Autoencoder Variacional usado para decodificar as amostras latentes em áudio |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | A forma de onda de áudio decodificada com volume normalizado e taxa de amostragem de 44100 Hz |

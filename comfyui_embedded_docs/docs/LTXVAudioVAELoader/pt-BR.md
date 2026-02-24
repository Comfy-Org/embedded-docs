> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/pt-BR.md)

O nó LTXV Audio VAE Loader carrega um modelo pré-treinado de Autoencoder Variacional (VAE) para áudio a partir de um arquivo de checkpoint. Ele lê o checkpoint especificado, carrega seus pesos e metadados, e prepara o modelo para uso em fluxos de trabalho de geração ou processamento de áudio dentro do ComfyUI.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `ckpt_name` | STRING | Sim | Todos os arquivos na pasta `checkpoints`.<br>*Exemplo: `"audio_vae.safetensors"`* | Checkpoint do VAE de áudio a ser carregado. Esta é uma lista suspensa preenchida com todos os arquivos encontrados no seu diretório `checkpoints` do ComfyUI. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `Audio VAE` | VAE | O modelo de Autoencoder Variacional para áudio carregado, pronto para ser conectado a outros nós de processamento de áudio. |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/en.md)

O nó Carregador de VAE de Áudio LTXV carrega um modelo de Autoencoder Variacional (VAE) de áudio pré-treinado a partir de um arquivo de checkpoint. Ele lê o checkpoint especificado, carrega seus pesos e metadados, e prepara o modelo para uso em fluxos de trabalho de geração ou processamento de áudio no ComfyUI.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `ckpt_name` | STRING | Sim | Todos os arquivos na pasta `checkpoints`.<br>*Exemplo: `"audio_vae.safetensors"`* | Checkpoint do VAE de áudio a ser carregado. Esta é uma lista suspensa preenchida com todos os arquivos encontrados no diretório `checkpoints` do seu ComfyUI. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `VAE de Áudio` | VAE | O modelo de Autoencoder Variacional de áudio carregado, pronto para ser conectado a outros nós de processamento de áudio. |

---
**Source fingerprint (SHA-256):** `44e79f694eed796a83f3ac25c56946baaa12b016568bd8824eb179bf79e50588`

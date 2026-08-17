# LTXV Carregar Áudio VAE

O nó LTXV Audio VAE Loader carrega um modelo de Autoencoder Variacional de Áudio (VAE) pré-treinado a partir de um arquivo de checkpoint. Ele lê o checkpoint especificado, carrega seus pesos e metadados e prepara o modelo para uso em fluxos de trabalho de geração ou processamento de áudio no ComfyUI.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `ckpt_name` | Checkpoint de VAE de áudio a carregar. Esta é uma lista suspensa preenchida com todos os arquivos encontrados no diretório `checkpoints` do seu ComfyUI. | COMBO | Sim | Todos os arquivos na pasta `checkpoints` (preenchidos dinamicamente).<br>*Exemplo: `"audio_vae.safetensors"`* |

Nota: O nó gera um erro se o arquivo de checkpoint selecionado não for encontrado ou não contiver um VAE de áudio válido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| Audio VAE | O modelo de Autoencoder Variacional de Áudio carregado, pronto para ser conectado a outros nós de processamento de áudio. | VAE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`

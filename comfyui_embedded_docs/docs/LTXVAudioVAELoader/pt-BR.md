# LTXV Carregar Áudio VAE

O nó **Carregador de VAE de Áudio LTXV** carrega um modelo de Autoencoder Variacional de Áudio (VAE) pré-treinado a partir de um arquivo checkpoint. Ele lê o checkpoint especificado, carrega seus pesos e metadados e prepara o modelo para uso em fluxos de trabalho de geração ou processamento de áudio no ComfyUI.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|--------------|-------|
| `nome_ckpt` | Checkpoint de VAE de áudio a ser carregado. Esta é uma lista suspensa preenchida com todos os arquivos encontrados no diretório `checkpoints` do seu ComfyUI. | COMBO | Sim | Todos os arquivos na pasta `checkpoints`. A lista é gerada em tempo de execução. |

O arquivo selecionado deve ser um checkpoint VAE de áudio LTXV válido. O nó mantém apenas os pesos do VAE de áudio e do vocoder do arquivo, e gera um erro se o modelo carregado não for um VAE válido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| Audio VAE | O modelo de Autoencoder Variacional de Áudio carregado, pronto para ser conectado a outros nós de processamento de áudio. | VAE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`

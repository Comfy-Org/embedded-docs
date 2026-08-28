# Salvar Checkpoint Somente Imagem

O nó ImageOnlyCheckpointSave salva um arquivo de checkpoint contendo um modelo, um codificador de visão CLIP e uma VAE. Ele cria um arquivo safetensors com o prefixo de nome de arquivo especificado e o armazena no diretório de saída. Este nó é especificamente projetado para salvar componentes de modelo relacionados a imagens juntos em um único arquivo de checkpoint.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo a ser salvo no checkpoint | MODEL | Sim | - |
| `clip_vision` | O codificador de visão CLIP a ser salvo no checkpoint | CLIP_VISION | Sim | - |
| `vae` | A VAE (Autoencoder Variacional) a ser salva no checkpoint | VAE | Sim | - |
| `prefixo_do_arquivo` | O prefixo para o nome do arquivo de saída (padrão: "checkpoints/ComfyUI") | STRING | Sim | - |
| `prompt` | Parâmetro oculto para dados de prompt do fluxo de trabalho | PROMPT | Não | - |
| `extra_pnginfo` | Metadados adicionais de PNG | EXTRA_PNGINFO | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| - | Este nó não retorna nenhuma saída | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`

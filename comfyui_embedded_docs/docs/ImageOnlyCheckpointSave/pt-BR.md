# Salvar Checkpoint Somente Imagem

Este nó salva um arquivo checkpoint que agrupa um modelo junto com seu codificador de visão CLIP e VAE. O arquivo é gravado no formato safetensors no diretório de saída, usando o prefixo de nome de arquivo fornecido, para que os componentes relacionados a imagem de um modelo possam ser armazenados como um único checkpoint.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo a ser salvo no checkpoint | MODEL | Sim | - |
| `clip_vision` | O codificador de visão CLIP a ser salvo no checkpoint | CLIP_VISION | Sim | - |
| `vae` | O VAE (Variational Autoencoder) a ser salvo no checkpoint | VAE | Sim | - |
| `filename_prefix` | O prefixo para o nome do arquivo de saída (padrão: "checkpoints/ComfyUI") | STRING | Sim | - |
| `prompt` | Parâmetro oculto que recebe os dados do prompt do fluxo de trabalho | PROMPT | Não | - |
| `extra_pnginfo` | Parâmetro oculto que recebe metadados PNG adicionais | EXTRA_PNGINFO | Não | - |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| - | Este nó não retorna nenhuma saída | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`

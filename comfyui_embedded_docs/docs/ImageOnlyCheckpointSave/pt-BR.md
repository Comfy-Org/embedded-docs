> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/pt-BR.md)

O nó ImageOnlyCheckpointSave salva um arquivo de checkpoint contendo um modelo, codificador de visão CLIP e VAE. Ele cria um arquivo safetensors com o prefixo de nome de arquivo especificado e o armazena no diretório de saída. Este nó foi projetado especificamente para salvar componentes de modelo relacionados a imagens juntos em um único arquivo de checkpoint.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | MODEL | Sim | - | O modelo a ser salvo no checkpoint |
| `clip_vision` | CLIP_VISION | Sim | - | O codificador de visão CLIP a ser salvo no checkpoint |
| `vae` | VAE | Sim | - | O VAE (Autoencoder Variacional) a ser salvo no checkpoint |
| `filename_prefix` | STRING | Sim | - | O prefixo para o nome do arquivo de saída (padrão: "checkpoints/ComfyUI") |
| `prompt` | PROMPT | Não | - | Parâmetro oculto para dados de prompt do fluxo de trabalho |
| `extra_pnginfo` | EXTRA_PNGINFO | Não | - | Parâmetro oculto para metadados PNG adicionais |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| - | - | Este nó não retorna nenhuma saída |

---
**Source fingerprint (SHA-256):** `d2a26933f0e2fcccf3c57f50038fb40ef5b23d00ccdd2e1d215b3cb78203b9fd`

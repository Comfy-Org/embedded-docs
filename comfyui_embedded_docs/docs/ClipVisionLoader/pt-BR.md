# Carregar CLIP Vision

Este nó detecta automaticamente os modelos localizados na pasta `ComfyUI/models/clip_vision`, bem como quaisquer caminhos de modelos adicionais configurados no arquivo `extra_model_paths.yaml`. Se você adicionar modelos após iniciar o ComfyUI, **atualize a interface do ComfyUI** para garantir que os arquivos de modelo mais recentes sejam listados.

## Entradas

| Campo | Descrição | Tipo de Dado |
| --- | --- | --- |
| `nome_do_clip` | Lista todos os arquivos de modelo suportados na pasta `ComfyUI/models/clip_vision`. | COMBO[STRING] |

## Saídas

| Campo | Descrição | Tipo de Dado |
| --- | --- | --- |
| `clip_vision` | Modelo CLIP Vision carregado, pronto para codificar imagens ou outras tarefas relacionadas à visão computacional. | CLIP_VISION |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionLoader/pt-BR.md)

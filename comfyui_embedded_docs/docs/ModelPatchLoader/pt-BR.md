# ModelPatchLoader

O nó ModelPatchLoader carrega patches de modelo especializados da pasta `model_patches`. Ele detecta automaticamente o tipo de arquivo de patch e carrega a arquitetura de modelo apropriada, em seguida o envolve em um ModelPatcher para uso no fluxo de trabalho. Este nó suporta diferentes tipos de patch, incluindo blocos de controlnet, modelos de embedder de características e outras arquiteturas especializadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `name` | O nome do arquivo do patch de modelo a ser carregado do diretório `model_patches` | STRING | Sim | Todos os arquivos de patch de modelo disponíveis na pasta `model_patches` |

Nota: Este nó é marcado como experimental no ComfyUI. O tipo de patch é detectado automaticamente a partir do conteúdo do arquivo, portanto, um único nó pode lidar com vários tipos de patches.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL_PATCH` | O patch de modelo carregado, envolvido em um ModelPatcher para uso no fluxo de trabalho | MODEL_PATCH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7f5225521b82b39b85183ccc7957fc4172e64aed9289f66d53969ea4a2e81b7f`

O nó ModelPatchLoader carrega patches de modelo especializados da pasta model_patches. Ele detecta automaticamente o tipo de arquivo de patch e carrega a arquitetura de modelo apropriada, em seguida, a envolve em um ModelPatcher para uso no fluxo de trabalho. Este nó suporta diferentes tipos de patch, incluindo blocos controlnet, modelos de incorporação de recursos e outras arquiteturas especializadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `nome` | O nome do arquivo de patch de modelo a ser carregado do diretório model_patches | STRING | Sim | Todos os arquivos de patch de modelo disponíveis na pasta model_patches |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL_PATCH` | O patch de modelo carregado, encapsulado em um ModelPatcher para uso no fluxo de trabalho | MODEL_PATCH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e394e165cf416019ed53d9fde42d97c3c9b9f9afd843b12371a624467a4841bf`

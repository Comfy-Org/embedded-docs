# ModelPatchLoader

O nó ModelPatchLoader carrega arquivos especializados de patch de modelo da pasta model_patches. Ele detecta automaticamente o tipo de patch a partir do conteúdo do arquivo e carrega a arquitetura de modelo correspondente, em seguida, o encapsula em um ModelPatcher para uso no fluxo de trabalho. Este nó suporta diferentes tipos de patch, incluindo blocos de controlnet, modelos de incorporação de características e outras arquiteturas especializadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `nome` | O nome do arquivo do patch de modelo para carregar do diretório model_patches | STRING | Sim | Todos os arquivos de patch de modelo disponíveis na pasta model_patches |

Nota: Este nó é marcado como experimental. O tipo de patch é detectado automaticamente a partir do conteúdo do arquivo, portanto, nenhuma seleção manual de tipo é necessária.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL_PATCH` | O patch de modelo carregado encapsulado em um ModelPatcher para uso no fluxo de trabalho | MODEL_PATCH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7f5225521b82b39b85183ccc7957fc4172e64aed9289f66d53969ea4a2e81b7f`

# Luma UNI-1 Image Edit

Este nó edita uma imagem existente usando um prompt de texto, alimentado pelo modelo Luma UNI-1. Ele recebe uma imagem de origem e uma descrição da alteração desejada, gerando uma nova versão editada da imagem.

# Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `source` | Imagem de origem a ser editada. | IMAGE | Sim | - |
| `prompt` | Descrição da edição desejada. Padrão: "" (string vazia). | STRING | Sim | 1–6000 caracteres |
| `model` | Modelo a ser usado para edição. | MODEL | Sim | `"uni-1"`<br>`"uni-1-max"` |
| `seed` | A semente controla se o nó deve ser reexecutado; os resultados são não determinísticos independentemente da semente. Padrão: 0. | INT | Sim | 0 a 2147483647 |

**Restrições dos Parâmetros:**
- O `prompt` deve ter entre 1 e 6000 caracteres.
- O parâmetro `model` é uma combinação dinâmica que, quando definido como `"uni-1"` ou `"uni-1-max"`, fornece subparâmetros adicionais (como `style`, `web_search` e `image_ref`). O subparâmetro `image_ref` aceita no máximo 8 referências de imagem.

# Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem editada gerada pelo modelo Luma UNI-1. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7026e3ce818b0a9710624bd071fc2049950290f89c7d0365ff44236e9ad5eaed`

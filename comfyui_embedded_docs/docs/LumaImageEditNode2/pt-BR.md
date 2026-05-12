> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/pt-BR.md)

## Visão Geral

Este nó edita uma imagem existente usando um prompt de texto, alimentado pelo modelo Luma UNI-1. Ele recebe uma imagem de origem e uma descrição da alteração desejada, gerando uma nova versão editada da imagem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `source` | IMAGE | Sim | - | Imagem de origem a ser editada. |
| `prompt` | STRING | Sim | 1–6000 caracteres | Descrição da edição desejada. Padrão: "" (string vazia). |
| `model` | MODEL | Sim | `"uni-1"`<br>`"uni-1-max"` | Modelo a ser usado para edição. |
| `seed` | INT | Sim | 0 a 2147483647 | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. Padrão: 0. |

**Restrições dos Parâmetros:**
- O `prompt` deve ter entre 1 e 6000 caracteres.
- O parâmetro `model` é uma combinação dinâmica que, quando definido como `"uni-1"` ou `"uni-1-max"`, fornece subparâmetros adicionais (como `style`, `web_search` e `image_ref`). O subparâmetro `image_ref` aceita no máximo 8 referências de imagem.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | A imagem editada gerada pelo modelo Luma UNI-1. |
# Salvar Conjunto de Imagens e Textos na Pasta

Save Image-Text (to Folder) é um nó de saída que salva um conjunto de dados de imagens emparelhadas com legendas de texto em uma pasta dentro do diretório de saída do ComfyUI. Cada imagem é salva como um arquivo PNG e, quando as legendas são fornecidas, um arquivo TXT correspondente com o mesmo nome base é criado para cada imagem. Isso é útil para construir conjuntos de dados organizados de imagens geradas e suas descrições.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `images` | Lista de imagens para salvar. | IMAGE | Sim | - |
| `texts` | Lista de legendas de texto para salvar. Esta entrada é opcional. | STRING | Não | - |
| `folder_name` | Nome da pasta para salvar as imagens (dentro do diretório de saída). (padrão: "dataset") | STRING | Sim | - |
| `filename_prefix` | Prefixo para os nomes de arquivo das imagens salvas. (padrão: "image") | STRING | Sim | - |
| `mode` | Se deve sobrescrever arquivos existentes ou incrementar os nomes dos arquivos para evitar sobrescrita. (padrão: "overwrite") | COMBO | Sim | "overwrite"<br>"increment" |

**Observação:** A entrada `images` é uma lista. A entrada `texts` é opcional; se for fornecida, deve ser uma lista de legendas de texto. As legendas são emparelhadas com as imagens em ordem, e cada legenda é salva como um arquivo `.txt` em UTF-8 com o mesmo nome base da imagem correspondente (por exemplo, `image_00000.txt` para `image_00000.png`). Se houver menos legendas do que imagens, as imagens restantes são salvas sem legendas; quaisquer legendas extras são ignoradas.

Entradas com valores padrão (`folder_name`, `filename_prefix`, `mode`) não precisam ser conectadas; seus valores padrão são usados automaticamente.

Quando `mode` está definido como `overwrite` (o padrão), as imagens são salvas com nomes como `image_00000.png`, substituindo quaisquer arquivos existentes com o mesmo nome. Quando `mode` está definido como `increment`, um contador automaticamente crescente é adicionado aos nomes dos arquivos para que os arquivos existentes não sejam sobrescritos.

O valor de `folder_name` deve resolver para um local dentro do diretório de saída do ComfyUI. Nomes de pasta que tentam escapar do diretório de saída (por exemplo, usando `..`) são rejeitados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| - | Este nó não tem saídas. Ele salva arquivos diretamente no sistema de arquivos. | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`

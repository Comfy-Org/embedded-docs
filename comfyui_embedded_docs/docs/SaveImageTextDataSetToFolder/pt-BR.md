# Salvar Conjunto de Imagens e Textos na Pasta

Save Image-Text (to Folder) salva um conjunto de dados de pares de imagem e legenda de texto em uma pasta dentro do diretório de saída do ComfyUI. Cada imagem é gravada como um arquivo PNG, e sua legenda correspondente é gravada como um arquivo TXT com o mesmo nome base, de modo que cada imagem acaba pareada com sua descrição.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | Lista de imagens a salvar. | IMAGE | Sim | - |
| `texts` | Lista de legendas de texto a salvar. Esta entrada é opcional. | STRING | Não | - |
| `folder_name` | Nome da pasta na qual salvar as imagens (dentro do diretório de saída). (padrão: "dataset") | STRING | Sim | - |
| `filename_prefix` | Prefixo para os nomes de arquivo das imagens salvas. (padrão: "image") | STRING | Sim | - |
| `mode` | Define se deve sobrescrever arquivos existentes ou incrementar nomes de arquivo para evitar sobrescrita. (padrão: "overwrite") | COMBO | Sim | "overwrite"<br>"increment" |

**Nota:** A entrada `images` é uma lista, e o nó recebe tanto `images` quanto `texts` como listas. A entrada `texts` é opcional; se fornecida, deve ser uma lista de legendas de texto e deve conter o mesmo número de itens que `images`. Cada legenda é salva como um arquivo `.txt` correspondente à sua imagem pareada. No modo `overwrite`, os arquivos são nomeados `{filename_prefix}_{index}.png` e substituem quaisquer arquivos existentes com o mesmo nome. No modo `increment`, um contador exclusivo é adicionado aos nomes de arquivo para que arquivos existentes não sejam sobrescritos. O `folder_name` deve resolver para um caminho dentro do diretório de saída; nomes de pasta que tentam escapar dele (por exemplo, com `..`) são rejeitados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| - | Este nó não retorna dados. Ele salva arquivos diretamente no sistema de arquivos. | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`

# Salvar Conjunto de Imagens e Textos na Pasta

O nó Save Image-Text (to Folder) salva uma lista de imagens e suas legendas de texto correspondentes em uma pasta especificada dentro do diretório de saída do ComfyUI. Para cada imagem salva como arquivo PNG, um arquivo TXT correspondente com o mesmo nome base é criado para armazenar sua legenda, o que torna útil para criar conjuntos de dados organizados de imagens geradas emparelhadas com suas descrições.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagens` | Lista de imagens para salvar. | IMAGE | Sim | - |
| `textos` | Lista de legendas de texto para salvar. Esta entrada é opcional. | STRING | Não | - |
| `nome_da_pasta` | Nome da pasta para salvar as imagens (dentro do diretório de saída). (padrão: "dataset") | STRING | Sim | - |
| `prefixo_do_arquivo` | Prefixo para os nomes de arquivo de imagem salvos. (padrão: "image") | STRING | Sim | - |
| `modo` | Se deve sobrescrever arquivos existentes ou incrementar nomes de arquivo para evitar sobrescrever. (padrão: "overwrite") | COMBO | Sim | "overwrite"<br>"increment" |

**Nota:** A entrada `images` é uma lista. A entrada `texts` é opcional; se for fornecida, deve ser uma lista de legendas de texto e deve conter o mesmo número de itens que `images`. Cada legenda é salva como um arquivo `.txt` correspondente à sua imagem emparelhada. No modo `overwrite`, os arquivos são nomeados como `{filename_prefix}_{index}.png` e substituem quaisquer arquivos existentes com o mesmo nome. No modo `increment`, um contador único é adicionado aos nomes de arquivo para que os arquivos existentes não sejam sobrescritos. O `folder_name` deve resolver para um caminho dentro do diretório de saída; nomes de pasta que tentem escapar dele (por exemplo, com `..`) são rejeitados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| - | Este nó não retorna dados. Ele salva arquivos diretamente no sistema de arquivos. | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`

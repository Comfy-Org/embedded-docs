# Salvar Conjunto de Imagens na Pasta

Este nó salva uma lista de imagens em uma pasta especificada dentro do diretório de saída do ComfyUI. Ele grava cada imagem no disco como um arquivo PNG usando um prefixo de nome de arquivo configurável. Este nó está obsoleto e foi substituído pelos nós Save Image existentes, nos quais a pasta de destino pode ser especificada no prefixo do nome de arquivo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagens` | Lista de imagens a serem salvas. | IMAGE | Sim | N/A |
| `nome_da_pasta` | Nome da pasta para salvar as imagens (dentro do diretório de saída). Padrão: "dataset". | STRING | Não | N/A |
| `prefixo_do_arquivo` | Prefixo para os nomes de arquivo das imagens salvas. Padrão: "image". Parâmetro avançado. | STRING | Não | N/A |
| `modo` | Se deve sobrescrever arquivos existentes ou incrementar os nomes de arquivo para evitar sobrescrita. Padrão: "overwrite". | COMBO | Não | "overwrite"<br>"increment" |

**Observações:**

- A entrada `images` é uma lista, portanto várias imagens podem ser salvas em uma única execução.
- Os parâmetros `folder_name`, `filename_prefix` e `mode` são valores escalares; se uma lista for conectada, apenas o primeiro valor dessa lista será usado.
- O `folder_name` deve resolver para um local dentro do diretório de saída do ComfyUI. Valores que escapam do diretório de saída (por exemplo, caminhos contendo `..` ou caminhos absolutos) são rejeitados com um erro.
- No modo "overwrite", os arquivos são salvos como `{prefix}_00000.png`, `{prefix}_00001.png` e assim por diante, substituindo quaisquer arquivos existentes. No modo "increment", um contador é inserido no nome do arquivo para que os arquivos existentes não sejam sobrescritos.

## Saídas

Este nó não possui saídas. É um nó de saída que realiza uma operação de salvamento no sistema de arquivos.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`

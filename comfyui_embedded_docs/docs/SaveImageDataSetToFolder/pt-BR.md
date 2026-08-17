# Salvar Conjunto de Imagens na Pasta

Este nó salva uma lista de imagens como arquivos PNG em uma pasta especificada dentro do diretório de saída do ComfyUI. Ele está obsoleto: é redundante e substituído pelos nós Save Image existentes, nos quais a pasta de destino pode ser especificada no prefixo do nome do arquivo. O nó grava cada imagem recebida no disco usando um prefixo de nome de arquivo personalizável e pode sobrescrever arquivos existentes ou gerar nomes de arquivos incrementados para evitar sobrescrita.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `images` | Lista de imagens a serem salvas. | IMAGE | Sim | N/A |
| `folder_name` | Nome da pasta em que as imagens serão salvas (dentro do diretório de saída). O valor padrão é "dataset". | STRING | Não | N/A |
| `filename_prefix` | Prefixo para os nomes dos arquivos de imagem salvos. O valor padrão é "image". | STRING | Não | N/A |
| `mode` | Define se os arquivos existentes serão sobrescritos ou se os nomes de arquivo serão incrementados para evitar sobrescrita. O valor padrão é "overwrite". | COMBO | Não | "overwrite"<br>"increment" |

**Nota:** A entrada `images` é uma lista, ou seja, pode receber e processar várias imagens de uma só vez. Todas as entradas são recebidas como listas; para `folder_name`, `filename_prefix` e `mode`, apenas o primeiro valor da lista conectada é usado. O `folder_name` deve corresponder a uma pasta dentro do diretório de saída do ComfyUI — nomes de pasta que saiam dele (por exemplo, usando "..", um caminho absoluto ou uma letra de unidade) são rejeitados com erro. As imagens são sempre salvas no formato PNG. O parâmetro `filename_prefix` é uma opção avançada.

## Saídas

Este nó não possui saídas de dados. É um nó de saída que realiza uma operação de salvamento no sistema de arquivos.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`

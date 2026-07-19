# Salvar Conjunto de Imagens na Pasta

Este nó salva uma lista de imagens em uma pasta especificada dentro do diretório de saída do ComfyUI. Ele recebe múltiplas imagens como entrada e as grava no disco com um prefixo de nome de arquivo personalizável.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagens` | Lista de imagens a serem salvas. | IMAGE | Sim | N/A |
| `nome_da_pasta` | Nome da pasta para salvar as imagens (dentro do diretório de saída). O valor padrão é "dataset". | STRING | Não | N/A |
| `prefixo_do_arquivo` | Prefixo para os nomes dos arquivos de imagem salvos. O valor padrão é "image". | STRING | Não | N/A |

**Observação:** A entrada `images` é uma lista, o que significa que pode receber e processar múltiplas imagens de uma só vez. Os parâmetros `folder_name` e `filename_prefix` são valores escalares; se uma lista for conectada, apenas o primeiro valor dessa lista será utilizado.

## Saídas

Este nó não possui saídas. É um nó de saída que realiza uma operação de salvamento no sistema de arquivos.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `65c7905caa8ff2811054bec2830c1359d0c441b5d93f50bc4d0bf10645046556`

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/pt-BR.md)

Este nó salva uma lista de imagens em uma pasta especificada dentro do diretório de saída do ComfyUI. Ele recebe múltiplas imagens como entrada e as grava no disco com um prefixo de nome de arquivo personalizável.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sim | N/A | Lista de imagens a serem salvas. |
| `folder_name` | STRING | Não | N/A | Nome da pasta para salvar as imagens (dentro do diretório de saída). O valor padrão é "dataset". |
| `filename_prefix` | STRING | Não | N/A | Prefixo para os nomes dos arquivos de imagem salvos. O valor padrão é "image". |

**Observação:** A entrada `images` é uma lista, o que significa que pode receber e processar múltiplas imagens de uma vez. Os parâmetros `folder_name` e `filename_prefix` são valores escalares; se uma lista for conectada, apenas o primeiro valor dessa lista será utilizado.

## Saídas

Este nó não possui nenhuma saída. É um nó de saída que executa uma operação de salvamento no sistema de arquivos.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/en.md)

## Visão Geral

Carrega um modelo de remoção de fundo a partir de um arquivo. Este nó prepara o modelo para ser utilizado na remoção de fundos de imagens.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `bg_removal_name` | STRING | Sim | Lista de arquivos de modelo disponíveis | O modelo usado para remover fundos de imagens. Selecione a partir da lista de arquivos de modelo de remoção de fundo disponíveis. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `bg_model` | BACKGROUND_REMOVAL | O modelo de remoção de fundo carregado, pronto para ser usado por outros nós no processamento de imagens. |
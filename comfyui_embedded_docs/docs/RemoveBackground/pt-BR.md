> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/en.md)

## Visão Geral

O nó Remove Background utiliza um modelo de remoção de fundo para gerar uma máscara que separa o objeto principal do fundo de uma imagem de entrada. Ele recebe uma imagem e um modelo de remoção de fundo, produzindo uma máscara que destaca o objeto principal.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | N/A | Imagem de entrada para remover o fundo |
| `bg_removal_model` | BACKGROUND_REMOVAL_MODEL | Sim | N/A | Modelo de remoção de fundo usado para gerar a máscara |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `mask` | MASK | Máscara do objeto gerada, destacando o assunto principal da imagem de entrada |
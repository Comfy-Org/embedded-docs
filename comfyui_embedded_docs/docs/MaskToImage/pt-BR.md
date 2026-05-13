> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskToImage/pt-BR.md)

O nó `MaskToImage` foi projetado para converter uma máscara em formato de imagem. Essa transformação permite a visualização e o processamento adicional de máscaras como imagens, facilitando a ponte entre operações baseadas em máscaras e aplicações baseadas em imagens.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|---------------|-----------|
| `mask`    | `MASK`        | A entrada de máscara é essencial para o processo de conversão, servindo como os dados de origem que serão transformados em formato de imagem. Essa entrada determina a forma e o conteúdo da imagem resultante. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|---------------|-----------|
| `image`   | `IMAGE`       | A saída é uma representação em imagem da máscara de entrada, permitindo inspeção visual e manipulações adicionais baseadas em imagem. |
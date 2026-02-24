> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImage/pt-BR.md)

O nó LoadImage foi projetado para carregar e pré-processar imagens de um caminho especificado. Ele lida com formatos de imagem com múltiplos quadros, aplica transformações necessárias, como rotação com base nos dados EXIF, normaliza os valores dos pixels e, opcionalmente, gera uma máscara para imagens com um canal alfa. Este nó é essencial para preparar imagens para processamento ou análise posterior dentro de um fluxo de trabalho.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|--------------|-------------|
| `image`   | COMBO[STRING] | O parâmetro `image` especifica o identificador da imagem a ser carregada e processada. É crucial para determinar o caminho do arquivo de imagem e, subsequentemente, carregar a imagem para transformação e normalização. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | A imagem processada, com valores de pixel normalizados e transformações aplicadas conforme necessário. Está pronta para processamento ou análise posterior. |
| `mask`    | `MASK`      | Uma saída opcional que fornece uma máscara para a imagem, útil em cenários onde a imagem inclui um canal alfa para transparência. |

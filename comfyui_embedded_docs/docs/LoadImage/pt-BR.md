> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImage/pt-BR.md)

O nó LoadImage foi projetado para carregar e pré-processar imagens a partir de um caminho especificado. Ele lida com formatos de imagem que possuem múltiplos quadros, aplica transformações necessárias, como rotação baseada em dados EXIF, normaliza valores de pixels e, opcionalmente, gera uma máscara para imagens com canal alfa. Este nó é essencial para preparar imagens para processamento ou análise posterior dentro de um pipeline.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|--------------|-----------|
| `imagem`   | COMBO[STRING] | O parâmetro `imagem` especifica o identificador da imagem a ser carregada e processada. Ele é crucial para determinar o caminho do arquivo de imagem e, subsequentemente, carregar a imagem para transformação e normalização. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|--------------|-----------|
| `imagem`   | `IMAGE`      | A imagem processada, com valores de pixels normalizados e transformações aplicadas conforme necessário. Está pronta para processamento ou análise adicional. |
| `mask`    | `MASK`       | Uma saída opcional que fornece uma máscara para a imagem, útil em cenários onde a imagem inclui um canal alfa para transparência. |
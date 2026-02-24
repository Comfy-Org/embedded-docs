> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageToMask/pt-BR.md)

O nó ImageToMask é projetado para converter uma imagem em uma máscara com base em um canal de cor especificado. Ele permite a extração de camadas de máscara correspondentes aos canais vermelho, verde, azul ou alfa de uma imagem, facilitando operações que exigem mascaramento ou processamento específico por canal.

## Entradas

| Parâmetro   | Tipo de Dados | Descrição                                                                                                          |
|-------------|-------------|----------------------------------------------------------------------------------------------------------------------|
| `image`     | `IMAGE`     | O parâmetro `image` representa a imagem de entrada a partir da qual uma máscara será gerada com base no canal de cor especificado. Ele desempenha um papel crucial na determinação do conteúdo e das características da máscara resultante. |
| `channel`   | COMBO[STRING] | O parâmetro `channel` especifica qual canal de cor (vermelho, verde, azul ou alfa) da imagem de entrada deve ser usado para gerar a máscara. Essa escolha influencia diretamente a aparência da máscara e quais partes da imagem são destacadas ou mascaradas. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | A saída `mask` é uma representação binária ou em tons de cinza do canal de cor especificado da imagem de entrada, útil para operações posteriores de processamento de imagem ou mascaramento. |

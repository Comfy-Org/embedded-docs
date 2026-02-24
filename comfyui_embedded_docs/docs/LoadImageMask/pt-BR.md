> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageMask/pt-BR.md)

O nó LoadImageMask foi projetado para carregar imagens e suas máscaras associadas a partir de um caminho especificado, processando-as para garantir compatibilidade com tarefas subsequentes de manipulação ou análise de imagem. Ele se concentra no tratamento de vários formatos e condições de imagem, como a presença de um canal alfa para máscaras, e prepara as imagens e máscaras para processamento posterior, convertendo-as para um formato padronizado.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `image`   | COMBO[STRING] | O parâmetro 'image' especifica o arquivo de imagem a ser carregado e processado. Ele desempenha um papel crucial na determinação da saída, fornecendo a imagem de origem para extração da máscara e conversão de formato. |
| `channel` | COMBO[STRING] | O parâmetro 'channel' especifica o canal de cor da imagem que será usado para gerar a máscara. Isso permite flexibilidade na criação de máscaras com base em diferentes canais de cor, aumentando a utilidade do nó em vários cenários de processamento de imagem. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | Este nó gera como saída a máscara criada a partir da imagem e do canal especificados, preparada em um formato padronizado adequado para processamento posterior em tarefas de manipulação de imagem. |

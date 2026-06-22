# Salvar PNG Animado

O nó SaveAnimatedPNG é projetado para criar e salvar imagens PNG animadas a partir de uma sequência de quadros. Ele gerencia a montagem de quadros individuais em uma animação coesa, permitindo a personalização da duração dos quadros, repetição e inclusão de metadados.

## Entradas

| Campo | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagens` | Uma lista de imagens a serem processadas e salvas como um PNG animado. Cada imagem na lista representa um quadro na animação. | `IMAGE` |
| `prefixo_do_arquivo` | Especifica o nome base para o arquivo de saída, que será usado como prefixo para os arquivos PNG animados gerados. | `STRING` |
| `fps` | A taxa de quadros por segundo da animação, controlando a velocidade com que os quadros são exibidos. | `FLOAT` |
| `nível_de_compressão` | O nível de compressão aplicado aos arquivos PNG animados, afetando o tamanho do arquivo e a clareza da imagem. | `INT` |

## Saídas

| Campo | Descrição | Tipo de Dados |
| --- | --- | --- |
| `ui` | Fornece um componente de interface do usuário exibindo as imagens PNG animadas geradas e indicando se a animação é de quadro único ou múltiplos quadros. | N/A |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedPNG/pt-BR.md)

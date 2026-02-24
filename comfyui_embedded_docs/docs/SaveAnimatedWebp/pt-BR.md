> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedWEBP/pt-BR.md)

Este nó foi projetado para salvar uma sequência de imagens como um arquivo WEBP animado. Ele gerencia a agregação de quadros individuais em uma animação coesa, aplica metadados especificados e otimiza a saída com base nas configurações de qualidade e compressão.

## Entradas

| Campo | Tipo de Dados | Descrição |
| :--- | :--- | :--- |
| `images` | `IMAGE` | Uma lista de imagens a serem salvas como quadros no WEBP animado. Este parâmetro é essencial para definir o conteúdo visual da animação. |
| `filename_prefix` | `STRING` | Especifica o nome base para o arquivo de saída, ao qual será adicionado um contador e a extensão '.webp'. Este parâmetro é crucial para identificar e organizar os arquivos salvos. |
| `fps` | `FLOAT` | A taxa de quadros por segundo para a animação, influenciando a velocidade de reprodução. |
| `lossless` | `BOOLEAN` | Um booleano que indica se deve ser usada compressão sem perdas, afetando o tamanho do arquivo e a qualidade da animação. |
| `quality` | `INT` | Um valor entre 0 e 100 que define o nível de qualidade da compressão, com valores mais altos resultando em melhor qualidade de imagem, mas em tamanhos de arquivo maiores. |
| `method` | COMBO[STRING] | Especifica o método de compressão a ser usado, o que pode impactar a velocidade de codificação e o tamanho do arquivo. |

## Saídas

| Campo | Tipo de Dados | Descrição |
| :--- | :--- | :--- |
| `ui` | N/A | Fornece um componente de interface do usuário que exibe as imagens WEBP animadas salvas junto com seus metadados e indica se a animação está habilitada. |

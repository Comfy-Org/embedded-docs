> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedPNG/pt-BR.md)

O nó SaveAnimatedPNG é projetado para criar e salvar imagens PNG animadas a partir de uma sequência de quadros. Ele gerencia a montagem de quadros de imagem individuais em uma animação coesa, permitindo a personalização da duração dos quadros, do loop e da inclusão de metadados.

## Entradas

| Campo | Tipo de Dados | Descrição |
| :--- | :--- | :--- |
| `images` | `IMAGE` | Uma lista de imagens a serem processadas e salvas como um PNG animado. Cada imagem na lista representa um quadro na animação. |
| `filename_prefix` | `STRING` | Especifica o nome base para o arquivo de saída, que será usado como prefixo para os arquivos PNG animados gerados. |
| `fps` | `FLOAT` | A taxa de quadros por segundo para a animação, controlando a velocidade com que os quadros são exibidos. |
| `compress_level` | `INT` | O nível de compressão aplicado aos arquivos PNG animados, afetando o tamanho do arquivo e a clareza da imagem. |

## Saídas

| Campo | Tipo de Dados | Descrição |
| :--- | :--- | :--- |
| `ui` | N/A | Fornece um componente de interface do usuário que exibe as imagens PNG animadas geradas e indica se a animação possui um único quadro ou múltiplos quadros. |

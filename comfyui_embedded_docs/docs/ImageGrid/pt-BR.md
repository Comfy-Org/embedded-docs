> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageGrid/pt-BR.md)

O nó Image Grid combina várias imagens em uma única grade ou colagem organizada. Ele recebe uma lista de imagens e as organiza em um número especificado de colunas, redimensionando cada imagem para caber em um tamanho de célula definido e adicionando um espaçamento opcional entre elas. O resultado é uma única imagem nova contendo todas as imagens de entrada em um layout de grade.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sim | - | Uma lista de imagens a serem organizadas na grade. O nó requer pelo menos uma imagem para funcionar. |
| `columns` | INT | Não | 1 - 20 | O número de colunas na grade (padrão: 4). |
| `cell_width` | INT | Não | 32 - 2048 | A largura, em pixels, de cada célula na grade (padrão: 256). |
| `cell_height` | INT | Não | 32 - 2048 | A altura, em pixels, de cada célula na grade (padrão: 256). |
| `padding` | INT | Não | 0 - 50 | A quantidade de espaçamento, em pixels, a ser colocada entre as imagens na grade (padrão: 4). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem de saída única contendo todas as imagens de entrada organizadas em uma grade. |

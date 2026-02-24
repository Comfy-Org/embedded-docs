> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CenterCropImages/pt-BR.md)

O nó Center Crop Images recorta uma imagem a partir do seu centro para uma largura e altura especificadas. Ele calcula a região central da imagem de entrada e extrai uma área retangular com as dimensões definidas. Se o tamanho de recorte solicitado for maior que a imagem, o recorte será limitado às bordas da imagem.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser recortada. |
| `width` | INT | Não | 1 a 8192 | A largura da área de recorte (padrão: 512). |
| `height` | INT | Não | 1 a 8192 | A altura da área de recorte (padrão: 512). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem resultante após a operação de recorte central. |

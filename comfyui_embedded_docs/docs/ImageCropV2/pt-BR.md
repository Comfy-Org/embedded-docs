> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropV2/pt-BR.md)

O nó Image Crop extrai uma seção retangular de uma imagem de entrada. Você define a região a ser mantida especificando suas coordenadas do canto superior esquerdo, largura e altura. O nó então retorna a porção recortada da imagem original.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | N/A | A imagem de entrada a ser recortada. |
| `crop_region` | BOUNDINGBOX | Sim | N/A | Define a área retangular a ser extraída da imagem. É especificada por `x` (início horizontal), `y` (início vertical), `width` (largura) e `height` (altura). Se a região definida se estender além das bordas da imagem, ela será automaticamente ajustada para caber dentro das dimensões da imagem. |

**Nota sobre Restrições de Região:** A região de corte é automaticamente restringida para permanecer dentro dos limites da imagem de entrada. Se a coordenada `x` ou `y` especificada for maior que a largura ou altura da imagem, ela será definida para a posição válida máxima. A largura e altura resultantes do corte serão ajustadas para que a região não ultrapasse as bordas da imagem.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A seção recortada da imagem de entrada original. |
> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomCropImages/pt-BR.md)

O nó Random Crop Images seleciona aleatoriamente uma seção retangular de cada imagem de entrada e a recorta para uma largura e altura especificadas. Isso é comumente usado para aumento de dados (data augmentation) para criar variações de imagens de treinamento. A posição aleatória para o recorte é determinada por um valor de semente (seed), garantindo que o mesmo recorte possa ser reproduzido.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem a ser recortada. |
| `width` | INT | Não | 1 - 8192 | A largura da área de recorte (padrão: 512). |
| `height` | INT | Não | 1 - 8192 | A altura da área de recorte (padrão: 512). |
| `seed` | INT | Não | 0 - 18446744073709551615 | Um número usado para controlar a posição aleatória do recorte (padrão: 0). |

**Observação:** Os parâmetros `width` e `height` devem ser menores ou iguais às dimensões da imagem de entrada. Se uma dimensão especificada for maior que a imagem, o recorte será limitado ao limite da imagem.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem resultante após a aplicação do recorte aleatório. |

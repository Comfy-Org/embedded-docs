> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/pt-BR.md)

O nó PikaScenes v2.2 combina múltiplas imagens para criar um vídeo que incorpora objetos de todas as imagens de entrada. Você pode fazer upload de até cinco imagens diferentes como ingredientes e gerar um vídeo de alta qualidade que as mistura de forma perfeita.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | Sim | - | Descrição textual do que gerar |
| `negative_prompt` | STRING | Sim | - | Descrição textual do que evitar na geração |
| `seed` | INT | Sim | - | Valor de semente aleatória para a geração |
| `resolution` | STRING | Sim | - | Resolução de saída para o vídeo |
| `duration` | INT | Sim | - | Duração do vídeo gerado |
| `ingredients_mode` | COMBO | Não | "creative"<br>"precise" | Modo para combinar os ingredientes (padrão: "creative") |
| `aspect_ratio` | FLOAT | Não | 0.4 - 2.5 | Proporção de aspecto (largura / altura) (padrão: 1.778) |
| `image_ingredient_1` | IMAGE | Não | - | Imagem que será usada como ingrediente para criar um vídeo |
| `image_ingredient_2` | IMAGE | Não | - | Imagem que será usada como ingrediente para criar um vídeo |
| `image_ingredient_3` | IMAGE | Não | - | Imagem que será usada como ingrediente para criar um vídeo |
| `image_ingredient_4` | IMAGE | Não | - | Imagem que será usada como ingrediente para criar um vídeo |
| `image_ingredient_5` | IMAGE | Não | - | Imagem que será usada como ingrediente para criar um vídeo |

**Nota:** Você pode fornecer até 5 imagens como ingredientes, mas pelo menos uma imagem é necessária para gerar um vídeo. O nó usará todas as imagens fornecidas para criar a composição final do vídeo.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado combinando todas as imagens de entrada |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/pt-BR.md)

O nó PikaScenes v2.2 combina várias imagens para criar um vídeo que incorpora objetos de todas as imagens de entrada. Você pode enviar até cinco imagens diferentes como ingredientes e gerar um vídeo de alta qualidade que as mescla perfeitamente.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | Sim | - | Descrição textual do que deve ser gerado |
| `negative_prompt` | STRING | Sim | - | Descrição textual do que deve ser evitado na geração |
| `seed` | INT | Sim | - | Valor de semente aleatória para geração |
| `resolution` | STRING | Sim | - | Resolução de saída do vídeo |
| `duration` | INT | Sim | - | Duração do vídeo gerado |
| `ingredients_mode` | STRING | Não | "creative"<br>"precise" | Modo de combinação dos ingredientes (padrão: "creative") |
| `aspect_ratio` | FLOAT | Não | 0.4 - 2.5 | Proporção de aspecto (largura / altura) (padrão: 1.778) |
| `image_ingredient_1` | IMAGE | Não | - | Imagem que será usada como ingrediente para criar um vídeo |
| `image_ingredient_2` | IMAGE | Não | - | Imagem que será usada como ingrediente para criar um vídeo |
| `image_ingredient_3` | IMAGE | Não | - | Imagem que será usada como ingrediente para criar um vídeo |
| `image_ingredient_4` | IMAGE | Não | - | Imagem que será usada como ingrediente para criar um vídeo |
| `image_ingredient_5` | IMAGE | Não | - | Imagem que será usada como ingrediente para criar um vídeo |

**Nota:** Você pode fornecer até 5 ingredientes de imagem, mas pelo menos uma imagem é necessária para gerar um vídeo. O nó usará todas as imagens fornecidas para criar a composição final do vídeo.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado combinando todas as imagens de entrada |

---
**Source fingerprint (SHA-256):** `dda8f10a58527c2b9037744f59f30821cdde37ad23427b856ba5e699a05acafd`

# PikaScenesV2_2

O nó PikaScenes v2.2 combina várias imagens para criar um vídeo que incorpora objetos de todas as imagens de entrada. Você pode enviar até cinco imagens diferentes como ingredientes e gerar um vídeo de alta qualidade que as mescla perfeitamente.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt_text` | Descrição textual do que deve ser gerado | STRING | Sim | - |
| `negative_prompt` | Descrição textual do que deve ser evitado na geração | STRING | Sim | - |
| `seed` | Valor de semente aleatória para geração | INT | Sim | - |
| `resolution` | Resolução de saída do vídeo | STRING | Sim | - |
| `duration` | Duração do vídeo gerado | INT | Sim | - |
| `ingredients_mode` | Modo de combinação dos ingredientes (padrão: "creative") | STRING | Não | "creative"<br>"precise" |
| `aspect_ratio` | Proporção de aspecto (largura / altura) (padrão: 1.778) | FLOAT | Não | 0.4 - 2.5 |
| `image_ingredient_1` | Imagem que será usada como ingrediente para criar um vídeo | IMAGE | Não | - |
| `image_ingredient_2` | Imagem que será usada como ingrediente para criar um vídeo | IMAGE | Não | - |
| `image_ingredient_3` | Imagem que será usada como ingrediente para criar um vídeo | IMAGE | Não | - |
| `image_ingredient_4` | Imagem que será usada como ingrediente para criar um vídeo | IMAGE | Não | - |
| `image_ingredient_5` | Imagem que será usada como ingrediente para criar um vídeo | IMAGE | Não | - |

**Nota:** Você pode fornecer até 5 ingredientes de imagem, mas pelo menos uma imagem é necessária para gerar um vídeo. O nó usará todas as imagens fornecidas para criar a composição final do vídeo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo gerado combinando todas as imagens de entrada | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dda8f10a58527c2b9037744f59f30821cdde37ad23427b856ba5e699a05acafd`

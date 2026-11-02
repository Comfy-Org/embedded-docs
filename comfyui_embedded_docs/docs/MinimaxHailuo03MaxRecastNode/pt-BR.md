# MiniMax H3 Max Recast

Recast substitui as pessoas em um vídeo pelas pessoas das fotos de referência, mantendo o movimento, a câmera, os cortes e o som do clipe de origem. O vídeo é enviado, a tarefa do Hailuo 03 Max é consultada e o vídeo recast retorna na resolução escolhida.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo a ser usado para geração de vídeo. | DYNAMIC_COMBO | Sim | "MiniMax H3 Max" |

### Entradas do MiniMax H3 Max

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `video` | Vídeo de origem, com 5 a 30 segundos de duração; cada cena deve ter 15 segundos ou menos. A proporção de aspecto deve estar entre 0,4 e 2,5. | VIDEO | Sim | 5 a 30 segundos |
| `reference_images` | Slot expansível: conecte de 1 a 4 fotos (`image_1`...`image_4`), uma para cada nova pessoa, com pelo menos 256x256 pixels. Por padrão, elas substituem as pessoas principais no vídeo da esquerda para a direita. | IMAGE | Sim | 1 a 4 imagens |
| `prompt` | Opcional. Quem se torna quem, ou o que mais manter ou alterar. Refira-se às fotos como `@Image1`..`@Image4`, por exemplo, "o homem se torna @Image2". | STRING | Sim | 0 a 2000 caracteres |
| `resolution` | Resolução do vídeo de saída (padrão: "768P"). | COMBO | Sim | "768P"<br>"1080P" |
| `enhance_realism` | Texturas de pele mais naturais e melhor integração das novas pessoas à cena (padrão: false). | BOOLEAN | Não | true<br>false |
| `seed` | Semente aleatória. A mesma solicitação com a mesma semente fornece resultados semelhantes, mas não necessariamente idênticos (padrão: 42). | INT | Sim | 0 a 4294967295 |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `video` | O vídeo recast com as novas pessoas no lugar. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxRecastNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a9e6f9edf12653f9f361992a097d1d57e7ba14b3e7dd20008b0e022cabc14c1b`

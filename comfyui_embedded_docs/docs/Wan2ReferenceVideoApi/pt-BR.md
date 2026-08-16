# Wan 2.7 Referência para Vídeo

Este nó gera um vídeo apresentando uma pessoa ou objeto com base nos materiais de referência fornecidos. Ele usa o modelo Wan 2.7 para criar vídeos a partir de um prompt de texto, suportando performances de um único personagem e interações com múltiplos personagens. Você deve fornecer pelo menos um vídeo de referência ou imagem de referência para que a geração funcione.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo específico a ser usado para geração de vídeo. | DYNAMIC_COMBO | Sim | "wan2.7-r2v" |
| `seed` | Semente a ser usada para geração, que ajuda a controlar a aleatoriedade da saída (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: False). Esta é uma configuração avançada. | BOOLEAN | Sim | True<br>False |

### wan2.7-r2v Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt descrevendo o vídeo. Use identificadores como 'character1' e 'character2' para se referir aos personagens de referência. Deve conter pelo menos um personagem. | STRING | Sim | - |
| `negative_prompt` | Prompt negativo descrevendo o que evitar (padrão: vazio). | STRING | Não | - |
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | "720P"<br>"1080P" |
| `ratio` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | A duração do vídeo gerado em segundos (padrão: 5). | INT | Sim | 2 a 10 |

### Entradas de Referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `reference_videos` | Slot expansível: conecte até 3 vídeos de referência (slots `video1` a `video3`). Pelo menos um vídeo ou imagem de referência é necessário no total. | VIDEO | Não | 0 a 3 itens |
| `reference_images` | Slot expansível: conecte até 5 imagens de referência (slots `image1` a `image5`). Pelo menos um vídeo ou imagem de referência é necessário no total. | IMAGE | Não | 0 a 5 itens |

**Restrições Importantes:**

* Você deve fornecer pelo menos um vídeo de referência ou imagem de referência nas entradas `model.reference_videos` ou `model.reference_images`.
* O número total combinado de vídeos de referência e imagens de referência não pode exceder 5.
* A entrada `model.prompt` deve conter pelo menos um personagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `52ac550522bf3fe8f57444ce8586fe83be470b893ff8c01292743553cfbd623d`

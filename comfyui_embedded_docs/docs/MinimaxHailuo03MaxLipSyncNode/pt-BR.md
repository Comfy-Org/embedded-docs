# MiniMax H3 Max Lip Sync

Este nó anima uma imagem estática para que os movimentos da boca acompanhem uma faixa de áudio fornecida. A imagem e o áudio são enviados, o job de sincronização labial do Hailuo 03 Max é consultado e o vídeo com fala retorna na resolução escolhida. O vídeo de saída tem a mesma duração do áudio.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo a ser usado para geração de vídeo. | DYNAMIC_COMBO | Sim | "MiniMax H3 Max" |

### Entradas do MiniMax H3 Max

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image` | Imagem a ser animada, com pelo menos 256x256 pixels. A proporção da imagem deve estar entre 0.4 e 2.5. | IMAGE | Sim | Imagem única |
| `audio` | Áudio para sincronização labial, com duração de 5 a 899 segundos. | AUDIO | Sim | 5 a 899 segundos |
| `resolution` | Resolução de saída (padrão: "768P"). A proporção é a suportada mais próxima da imagem. | COMBO | Sim | "480P"<br>"768P"<br>"1080P"<br>"2K" |
| `transcription` | Transcrever o áudio para orientar a sincronização labial (padrão: false). | BOOLEAN | Não | true<br>false |
| `seed` | Semente aleatória. A mesma requisição com a mesma semente produz resultados semelhantes, mas não necessariamente idênticos (padrão: 42). | INT | Sim | 0 a 2147483647 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | O vídeo com fala, com a mesma duração do áudio de entrada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxLipSyncNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0af4166f9f3237cacc3506d6c6544c0374a330cf998f8bd2ef1f4f7162e2f9ab`

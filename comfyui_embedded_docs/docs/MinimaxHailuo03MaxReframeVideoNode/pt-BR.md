# MiniMax H3 Max Reframe Video

Este nó adapta um vídeo a uma nova proporção de aspecto, ajustando-o em uma nova tela e gerando as áreas ao redor. A temporização e o áudio do vídeo de origem são preservados. Use-o para transformar um clipe horizontal em vertical, ou vice-versa, sem cortar o assunto para fora do enquadramento.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo a ser usado para geração de vídeo. | DYNAMIC_COMBO | Sim | "MiniMax H3 Max" |

### Entradas do MiniMax H3 Max

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `video` | Vídeo de origem a ser reenquadrado, com duração de 0.5 a 300 segundos. | VIDEO | Sim | 0.5 a 300 segundos |
| `aspect_ratio` | Proporção de aspecto da tela de saída (padrão: "9:16"). | COMBO | Sim | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9"<br>"9:21" |
| `resolution` | Resolução do vídeo de saída (padrão: "768P"). | COMBO | Sim | "480P"<br>"768P"<br>"1080P" |
| `prompt` | Orientação opcional para as áreas ao redor geradas. | STRING | Sim | 0 a 50000 caracteres |
| `seed` | Semente aleatória. A mesma solicitação com a mesma semente fornece resultados semelhantes, mas não necessariamente idênticos (padrão: 42). | INT | Sim | 0 a 4294967295 |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `video` | O vídeo reenquadrado na proporção de aspecto selecionada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxReframeVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `83d780c2fe8c42475d4ad25ad5b318f2a4c135edef9c0ca1ff0d1fd07d90c1c6`

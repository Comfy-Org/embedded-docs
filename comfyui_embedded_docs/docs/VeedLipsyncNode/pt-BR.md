# VEED Lipsync 2.0

Ressincronize a boca de um falante em um vídeo com uma nova faixa de fala usando o VEED Lipsync. Use-o para dublar um clipe ou substituir seu diálogo mantendo a filmagem original. A saída mantém a resolução do vídeo a 25 fps e tem a mesma duração do áudio, com um falante por vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo a usar. A seleção de um modelo revela os parâmetros específicos dele: `video`, `audio` e `seed`. | DYNAMIC_COMBO | Sim | `"lipsync-2.0"` |
| `video` | Filmagem de um falante de frente. Se for mais curta que o áudio, ela é reproduzida para frente e para trás até o áudio terminar. | VIDEO | Sim | - |
| `audio` | Nova fala, com até 600 segundos. Define a duração do vídeo. | AUDIO | Sim | Até 600 segundos |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados não são determinísticos independentemente da seed. (padrão: 42) | INT | Sim | 0 a 2147483647 |

O nó é interrompido com um erro quando a faixa de fala tem mais de 600 segundos ou quando o job do VEED falha.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `VIDEO` | O vídeo ressincronizado: a filmagem original com a boca sincronizada à nova fala. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedLipsyncNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1a1e854b6923b5bad0fd6f3a79e76c70231dee31a12e9cf0b22be6bdcc741168`

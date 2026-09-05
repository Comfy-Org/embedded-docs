# VideoTrim

Este nó corta um vídeo para uma janela de tempo escolhida, definindo um tempo inicial e uma duração. Ele também oferece um modo estrito que gera um erro quando a duração solicitada não pode ser alcançada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `video` | O vídeo a ser cortado. | VIDEO | Sim | — |
| `trim` | Janela de corte usando quadros inicial/final. A janela é convertida em um tempo inicial (em segundos a partir do início do vídeo) e uma duração (em segundos). Quando o tempo inicial e a duração são ambos 0, o vídeo é retornado sem nenhum corte. | VIDEO_EDIT | Sim | start_time: >= 0, default 0<br>duration: >= 0, default 0 |
| `strict_duration` | Se True, quando a duração especificada não for possível, um erro será gerado. (padrão: False) | BOOLEAN | Não | true<br>false |

Nota: A duração do corte deve ser >= 0; valores negativos geram um erro. A janela de corte solicitada deve caber dentro do vídeo de origem. Se o corte não puder ser aplicado, um erro será gerado informando a duração da origem, o tempo inicial e a duração de destino.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo cortado. Quando a janela de corte está vazia (tempo inicial e duração ambos 0), o vídeo original é retornado inalterado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTrim/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ba8f8ccbae7e8aebda553810b81ccaa427d45523142bd00746c4e2f4e5b41a1b`

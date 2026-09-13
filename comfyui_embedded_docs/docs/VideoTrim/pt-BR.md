# Aparar Vídeo (Avançado)

Este nó corta um vídeo para uma janela de tempo escolhida definindo um tempo de início e uma duração. Ele também oferece um modo estrito que gera um erro quando a duração solicitada não pode ser alcançada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `video` | O vídeo a ser cortado. | VIDEO | Sim | — |
| `trim` | Janela de corte usando quadros de início/fim. A janela é convertida em um tempo de início (em segundos desde o início do vídeo) e uma duração (em segundos). Quando tanto o tempo de início quanto a duração forem 0, o vídeo é retornado sem nenhum corte. | VIDEO_EDIT | Sim | start_time: >= 0, padrão 0<br>duration: >= 0, padrão 0 |
| `strict_duration` | Se True, quando a duração especificada não for possível, um erro será gerado. (padrão: False) | BOOLEAN | Não | true<br>false |

Observação: A duração do corte deve ser >= 0; valores negativos geram um erro. A janela de corte solicitada deve caber dentro do vídeo de origem. Se o corte não puder ser aplicado, um erro será gerado informando a duração da origem, o tempo de início e a duração desejada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo cortado. Quando a janela de corte está vazia (tempo de início e duração ambos 0), o vídeo original é retornado sem alterações. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTrim/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ba8f8ccbae7e8aebda553810b81ccaa427d45523142bd00746c4e2f4e5b41a1b`

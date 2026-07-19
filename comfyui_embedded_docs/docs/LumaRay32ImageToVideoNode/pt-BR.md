# LumaRay32ImageToVideoNode

Gere um vídeo a partir de um quadro inicial e/ou final usando o modelo Ray 3.2 da Luma. Gerações ancoradas em imagem têm sempre 5 segundos de duração.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para a geração do vídeo. | STRING | Sim | 1 a 6000 caracteres |
| `resolution` | A resolução de saída do vídeo gerado (padrão: "720p"). | COMBO | Sim | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `loop` | Faz o vídeo repetir-se sem emendas. Não disponível quando um `end_frame` é definido. | BOOLEAN | Sim | Verdadeiro<br>Falso |
| `seed` | Valor de semente para geração reproduzível. | INT | Sim | 0 a 2147483647 |
| `start_frame` | Primeiro quadro do vídeo gerado. | IMAGE | Não | - |
| `end_frame` | Último quadro do vídeo gerado. | IMAGE | Não | - |

**Nota:** Pelo menos um dos parâmetros `start_frame` ou `end_frame` deve ser fornecido. Se ambos forem fornecidos, o vídeo gerado fará uma transição do quadro inicial para o quadro final. A opção `loop` não pode ser ativada quando um `end_frame` é definido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `video` | A saída do vídeo gerado. | VIDEO |
| `generation_id` | O identificador único para a solicitação de geração. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ff479c196f10153ffa09af6acfb4e286d1934aa28a5e9b413613097a2cfb5f2a`

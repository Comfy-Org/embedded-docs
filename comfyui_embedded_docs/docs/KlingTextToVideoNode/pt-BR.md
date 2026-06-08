O nó Kling Text to Video converte descrições textuais em conteúdo de vídeo. Ele recebe prompts de texto e gera sequências de vídeo correspondentes com base nas configurações especificadas. O nó suporta diferentes proporções de aspecto e modos de geração para produzir vídeos de durações e qualidades variadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt de texto positivo | STRING | Sim | - |
| `negative_prompt` | Prompt de texto negativo | STRING | Sim | - |
| `cfg_scale` | Valor da escala de configuração (padrão: 1.0) | FLOAT | Não | 0.0 a 1.0 |
| `aspect_ratio` | Configuração da proporção de aspecto do vídeo (padrão: "16:9") | COMBO | Não | Opções do KlingVideoGenAspectRatio |
| `mode` | Configuração a ser usada para a geração do vídeo seguindo o formato: modo / duração / nome_do_modelo. (padrão: modes[8]) | COMBO | Não | Múltiplas opções disponíveis |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo gerado como saída | VIDEO |
| `video_id` | Identificador único para o vídeo gerado | STRING |
| `duration` | Informação de duração do vídeo gerado | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `467f89a47890bfbfe6cebac8897fef3bce37d888d3419b248d13be89bed442f3`

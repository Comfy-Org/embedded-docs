> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/pt-BR.md)

O nó Kling Text to Video converte descrições textuais em conteúdo de vídeo. Ele recebe prompts de texto e gera sequências de vídeo correspondentes com base nas configurações especificadas. O nó suporta diferentes proporções de aspecto e modos de geração para produzir vídeos de durações e qualidades variadas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | - | Prompt de texto positivo |
| `negative_prompt` | STRING | Sim | - | Prompt de texto negativo |
| `cfg_scale` | FLOAT | Não | 0.0 a 1.0 | Valor da escala de configuração (padrão: 1.0) |
| `aspect_ratio` | COMBO | Não | Opções do KlingVideoGenAspectRatio | Configuração da proporção de aspecto do vídeo (padrão: "16:9") |
| `mode` | COMBO | Não | Múltiplas opções disponíveis | Configuração a ser usada para a geração do vídeo seguindo o formato: modo / duração / nome_do_modelo. (padrão: modes[8]) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O vídeo gerado como saída |
| `video_id` | STRING | Identificador único para o vídeo gerado |
| `duration` | STRING | Informação de duração do vídeo gerado |

---
**Source fingerprint (SHA-256):** `467f89a47890bfbfe6cebac8897fef3bce37d888d3419b248d13be89bed442f3`

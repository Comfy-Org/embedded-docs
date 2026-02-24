> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/pt-BR.md)

O nó Kling Text to Video converte descrições de texto em conteúdo de vídeo. Ele recebe prompts de texto e gera sequências de vídeo correspondentes com base nas configurações especificadas. O nó suporta diferentes proporções de tela e modos de geração para produzir vídeos de durações e qualidades variadas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Prompt de texto positivo (padrão: nenhum) |
| `negative_prompt` | STRING | Sim | - | Prompt de texto negativo (padrão: nenhum) |
| `cfg_scale` | FLOAT | Não | 0.0-1.0 | Valor da escala de configuração (padrão: 1.0) |
| `aspect_ratio` | COMBO | Não | Opções de KlingVideoGenAspectRatio | Configuração da proporção de tela do vídeo (padrão: "16:9") |
| `mode` | COMBO | Não | Múltiplas opções disponíveis | A configuração a ser usada para a geração do vídeo, seguindo o formato: modo / duração / nome_do_modelo. (padrão: modes[4]) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | A saída de vídeo gerada |
| `video_id` | STRING | Identificador único para o vídeo gerado |
| `duration` | STRING | Informação de duração para o vídeo gerado |

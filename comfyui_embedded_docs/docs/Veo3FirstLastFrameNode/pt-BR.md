> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/pt-BR.md)

O Veo3FirstLastFrameNode utiliza o modelo Veo 3 do Google para gerar um vídeo. Ele cria um vídeo com base em um prompt de texto, usando um primeiro e um último quadro fornecidos para orientar o início e o fim da sequência.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | N/A | Descrição textual do vídeo (padrão: string vazia). |
| `negative_prompt` | STRING | Não | N/A | Prompt de texto negativo para orientar o que evitar no vídeo (padrão: string vazia). |
| `resolution` | COMBO | Sim | `"720p"`<br>`"1080p"` | A resolução do vídeo de saída. |
| `aspect_ratio` | COMBO | Não | `"16:9"`<br>`"9:16"` | Proporção de aspecto do vídeo de saída (padrão: "16:9"). |
| `duration` | INT | Não | 4 a 8 | Duração do vídeo de saída em segundos (padrão: 8). |
| `seed` | INT | Não | 0 a 4294967295 | Semente para a geração do vídeo (padrão: 0). |
| `first_frame` | IMAGE | Sim | N/A | O quadro inicial para o vídeo. |
| `last_frame` | IMAGE | Sim | N/A | O quadro final para o vídeo. |
| `model` | COMBO | Não | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"` | O modelo específico do Veo 3 a ser usado para a geração (padrão: "veo-3.1-fast-generate"). |
| `generate_audio` | BOOLEAN | Não | N/A | Gerar áudio para o vídeo (padrão: True). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado. |

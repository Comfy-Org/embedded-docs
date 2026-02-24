> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoExtendNode/pt-BR.md)

O nó Kling Video Extend permite estender vídeos criados por outros nós Kling. Ele recebe um vídeo existente identificado pelo seu ID de vídeo e gera conteúdo adicional com base nos seus prompts de texto. O nó funciona enviando sua solicitação de extensão para a API Kling e retornando o vídeo estendido junto com seu novo ID e duração.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Não | - | Prompt de texto positivo para orientar a extensão do vídeo |
| `negative_prompt` | STRING | Não | - | Prompt de texto negativo para elementos a serem evitados no vídeo estendido |
| `cfg_scale` | FLOAT | Não | 0.0 - 1.0 | Controla a força da orientação do prompt (padrão: 0.5) |
| `video_id` | STRING | Sim | - | O ID do vídeo a ser estendido. Suporta vídeos gerados por operações de texto-para-vídeo, imagem-para-vídeo e extensão de vídeo anteriores. Não pode exceder 3 minutos de duração total após a extensão. |

**Observação:** O `video_id` deve referenciar um vídeo criado por outros nós Kling, e a duração total após a extensão não pode exceder 3 minutos.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo estendido gerado pela API Kling |
| `video_id` | STRING | O identificador único para o vídeo estendido |
| `duration` | STRING | A duração do vídeo estendido |

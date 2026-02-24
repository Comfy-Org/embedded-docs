> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/pt-BR.md)

O nó Kling Image to Video gera conteúdo de vídeo a partir de uma imagem inicial usando prompts de texto. Ele utiliza uma imagem de referência e cria uma sequência de vídeo com base nas descrições de texto positivas e negativas fornecidas, com várias opções de configuração para seleção de modelo, duração e proporção de tela.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | Sim | - | A imagem de referência usada para gerar o vídeo. |
| `prompt` | STRING | Sim | - | Prompt de texto positivo. |
| `negative_prompt` | STRING | Sim | - | Prompt de texto negativo. |
| `model_name` | COMBO | Sim | Múltiplas opções disponíveis | Seleção do modelo para geração de vídeo (padrão: "kling-v2-master"). |
| `cfg_scale` | FLOAT | Sim | 0.0-1.0 | Parâmetro de escala de configuração (padrão: 0.8). |
| `mode` | COMBO | Sim | Múltiplas opções disponíveis | Seleção do modo de geração de vídeo (padrão: std). |
| `aspect_ratio` | COMBO | Sim | Múltiplas opções disponíveis | Proporção de tela para o vídeo gerado (padrão: field_16_9). |
| `duration` | COMBO | Sim | Múltiplas opções disponíveis | Duração do vídeo gerado (padrão: field_5). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | A saída do vídeo gerado. |
| `video_id` | STRING | Identificador único para o vídeo gerado. |
| `duration` | STRING | Informação de duração para o vídeo gerado. |

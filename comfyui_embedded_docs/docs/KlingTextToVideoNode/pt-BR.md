# Kling Texto para Vídeo

O nó Kling Text to Video gera vídeos a partir de descrições de texto usando a API de geração de vídeo Kling. Ele envia o prompt e as configurações (proporção de tela, modo de geração e escala CFG) para a API, aguarda a conclusão da tarefa de geração e então retorna o vídeo resultante junto com seu ID e duração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto positivo | STRING | Sim | Máximo de 2500 caracteres |
| `negative_prompt` | Prompt de texto negativo | STRING | Não | Máximo de 2500 caracteres |
| `cfg_scale` | Valor da escala de configuração que controla quão fielmente o vídeo segue o prompt (padrão: 1.0) | FLOAT | Não | 0.0 a 1.0 |
| `aspect_ratio` | Configuração de proporção de tela do vídeo (padrão: "16:9") | COMBO | Não | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | A configuração a ser usada para a geração do vídeo, seguindo o formato: mode / duration / model_name (padrão: "pro mode / 5s duration / kling-v2-5-turbo") | COMBO | Não | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

Nota: O parâmetro `prompt` é obrigatório e não pode estar vazio. Tanto `prompt` quanto `negative_prompt` são limitados a no máximo 2500 caracteres. A opção `mode` de 10 segundos custa mais que a opção de 5 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A saída de vídeo gerada | VIDEO |
| `video_id` | Identificador único para o vídeo gerado | STRING |
| `duration` | Informação de duração do vídeo gerado | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`

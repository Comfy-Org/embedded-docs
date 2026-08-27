# Kling Imagem (Primeiro Quadro) para Vídeo

O nó Kling Image to Video gera um vídeo curto usando uma imagem inicial como primeiro quadro. Ele combina a imagem com prompts de texto e configurações de geração e, em seguida, retorna o vídeo resultante junto com seu ID e duração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | A imagem de referência usada para gerar o vídeo. A imagem deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2.5 e 2.5:1. | IMAGE | Sim | - |
| `prompt` | Prompt de texto positivo. Não deve estar vazio. Máximo de 500 caracteres. | STRING | Sim | - |
| `negative_prompt` | Prompt de texto negativo. Máximo de 500 caracteres. Deixe vazio se não for usado. | STRING | Sim | - |
| `model_name` | O modelo usado para geração de vídeo (padrão: `"kling-v2-5-turbo"`). | COMBO | Sim | `"kling-v2-5-turbo"` |
| `cfg_scale` | Controla o quanto o vídeo segue o prompt. Valores maiores significam aderência mais forte (padrão: 0.8). | FLOAT | Sim | 0.0 a 1.0 |
| `mode` | O modo de geração (padrão: `"pro"`). | COMBO | Sim | `"pro"` |
| `aspect_ratio` | A proporção de aspecto do vídeo gerado (padrão: `"16:9"`). | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | A duração do vídeo gerado em segundos (padrão: `"5"`). | COMBO | Sim | `"5"`<br>`"10"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A saída de vídeo gerada. | VIDEO |
| `video_id` | Identificador exclusivo do vídeo gerado. | STRING |
| `duration` | Informações de duração do vídeo gerado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f4a461819bc05f92d867bddcc78a66ad7beaa10707ef8cae3e7eb9e6f72c890a`

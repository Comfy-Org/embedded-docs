# Kling Imagem (Primeiro Quadro) para Vídeo

O nó Kling Image to Video gera um vídeo a partir de uma imagem de referência inicial usando prompts de texto. Ele usa a imagem como primeiro quadro e cria uma sequência de vídeo com base em descrições de texto positivas e negativas, com opções configuráveis para modelo, duração, modo de geração e proporção de aspecto.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | A imagem de referência usada para gerar o vídeo. Deve ter pelo menos 300x300 pixels com proporção de aspecto entre 1:2.5 e 2.5:1. | IMAGE | Sim | - |
| `prompt` | Prompt de texto positivo. Máximo de 500 caracteres. | STRING | Sim | - |
| `negative_prompt` | Prompt de texto negativo. Máximo de 500 caracteres. Pode ser deixado vazio. | STRING | Sim | - |
| `model_name` | O modelo usado para a geração de vídeo (padrão: `"kling-v2-5-turbo"`). | COMBO | Sim | `"kling-v2-5-turbo"` |
| `cfg_scale` | Controla o quão fielmente o vídeo segue o prompt. Valores mais altos significam maior fidelidade (padrão: 0.8). | FLOAT | Sim | 0.0 a 1.0 |
| `mode` | O modo de geração (padrão: `"pro"`). | COMBO | Sim | `"pro"` |
| `aspect_ratio` | A proporção de aspecto do vídeo gerado (padrão: `"16:9"`). | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | A duração do vídeo gerado em segundos (padrão: `"5"`). | COMBO | Sim | `"5"`<br>`"10"` |

Nota: O prompt positivo não pode estar vazio. Tanto o prompt positivo quanto o negativo são limitados a 500 caracteres. A imagem de entrada deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2.5 e 2.5:1.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `output` | O vídeo gerado. | VIDEO |
| `video_id` | Identificador único do vídeo gerado. | STRING |
| `duration` | Duração do vídeo gerado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f4a461819bc05f92d867bddcc78a66ad7beaa10707ef8cae3e7eb9e6f72c890a`

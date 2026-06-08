O nó Kling Image to Video gera um vídeo a partir de uma imagem de referência inicial usando prompts de texto. Ele utiliza uma imagem como primeiro quadro e cria uma sequência de vídeo com base em descrições de texto positivas e negativas, com opções configuráveis para modelo, duração, proporção de tela e modo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `start_frame` | A imagem de referência usada para gerar o vídeo. | IMAGE | Sim | - |
| `prompt` | Prompt de texto positivo. | STRING | Sim | - |
| `negative_prompt` | Prompt de texto negativo. | STRING | Sim | - |
| `model_name` | O modelo usado para geração de vídeo (padrão: `"kling-v2-master"`). | COMBO | Sim | `"kling-v2-master"`<br>`"kling-v2-1-master"`<br>`"kling-v2-5-turbo"`<br>`"kling-v2-1"`<br>`"kling-v1-6"`<br>`"kling-v1-5"`<br>`"kling-v1-4"`<br>`"kling-v1-0"` |
| `cfg_scale` | Controla o quão fielmente o vídeo segue o prompt. Valores mais altos indicam maior aderência (padrão: 0.8). | FLOAT | Sim | 0.0 a 1.0 |
| `mode` | O modo de geração. `"std"` é qualidade padrão, `"pro"` é qualidade superior (padrão: `"std"`). | COMBO | Sim | `"std"`<br>`"pro"` |
| `aspect_ratio` | A proporção de tela do vídeo gerado (padrão: `"16:9"`). | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | A duração do vídeo gerado em segundos (padrão: `"5"`). | COMBO | Sim | `"5"`<br>`"10"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A saída do vídeo gerado. | VIDEO |
| `video_id` | Identificador único para o vídeo gerado. | STRING |
| `duration` | Informações de duração do vídeo gerado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2f82997307265dba6714733523e265d1e0a25fd7491b043f05d7d000b7b9b2f3`

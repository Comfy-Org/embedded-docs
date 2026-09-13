# Kling Texto para Vídeo com Áudio

O nó Kling Text to Video with Audio gera um vídeo curto a partir de uma descrição de texto. Ele envia uma solicitação ao serviço Kling AI, que processa o prompt e retorna um arquivo de vídeo. O nó também pode gerar áudio de acompanhamento para o vídeo com base no texto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `model_name` | O modelo de IA específico a ser usado para a geração de vídeo. | COMBO | Sim | `"kling-v2-6"` |
| `prompt` | Prompt de texto positivo. A descrição usada para gerar o vídeo. Deve ter entre 1 e 2500 caracteres. | STRING | Sim | - |
| `mode` | O modo operacional para a geração de vídeo. | COMBO | Sim | `"pro"` |
| `aspect_ratio` | A proporção de aspecto desejada para o vídeo gerado. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | A duração do vídeo em segundos. | COMBO | Sim | `5`<br>`10` |
| `generate_audio` | Controla se o áudio é gerado para o vídeo. Quando ativado, a IA criará som com base no prompt (padrão: `True`). | BOOLEAN | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ddd2f3c1799abac067a05f3f5d6442ad4fe023d2f4f9afbde2894ca66854977e`

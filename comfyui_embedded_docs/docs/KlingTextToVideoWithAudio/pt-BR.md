# Kling Texto para Vídeo com Áudio

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/en.md)

O nó Kling Text to Video with Audio gera um vídeo curto a partir de uma descrição textual. Ele envia uma solicitação ao serviço de IA da Kling, que processa o prompt e retorna um arquivo de vídeo. O nó também pode gerar áudio de acompanhamento para o vídeo com base no texto.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model_name` | O modelo de IA específico a ser usado para geração de vídeo. | COMBO | Sim | `"kling-v2-6"` |
| `prompt` | Prompt textual positivo. A descrição usada para gerar o vídeo. Deve ter entre 1 e 2500 caracteres. | STRING | Sim | - |
| `mode` | O modo operacional para a geração do vídeo. | COMBO | Sim | `"pro"` |
| `aspect_ratio` | A proporção largura-altura desejada para o vídeo gerado. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | A duração do vídeo em segundos. | COMBO | Sim | `5`<br>`10` |
| `generate_audio` | Controla se o áudio é gerado para o vídeo. Quando ativado, a IA criará som com base no prompt. (padrão: `True`) | BOOLEAN | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `eff4549816c347a090e2f6e8ae8ba832bd2c5b7aef7c729b51c9d72b7a814d5a`

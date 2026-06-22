# Kling Lip Sync Vídeo com Texto

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/en.md)

Nó de Vídeo de Sincronização Labial com Texto Kling sincroniza os movimentos da boca em um arquivo de vídeo para corresponder a um prompt de texto. Ele recebe um vídeo de entrada e gera um novo vídeo onde os movimentos labiais do personagem são alinhados com o texto fornecido. O nó usa síntese de voz para criar uma sincronização de fala com aparência natural.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `vídeo` | Arquivo de vídeo de entrada para sincronização labial | VIDEO | Sim | - |
| `texto` | Conteúdo de texto para geração de vídeo com sincronização labial. Obrigatório quando o modo é text2video. Comprimento máximo de 120 caracteres. | STRING | Sim | - |
| `voz` | Seleção de voz para o áudio de sincronização labial (padrão: "Melody") | COMBO | Não | "Melody"<br>"Bella"<br>"Aria"<br>"Ethan"<br>"Ryan"<br>"Dorothy"<br>"Nathan"<br>"Lily"<br>"Aaron"<br>"Emma"<br>"Grace"<br>"Henry"<br>"Isabella"<br>"James"<br>"Katherine"<br>"Liam"<br>"Mia"<br>"Noah"<br>"Olivia"<br>"Sophia" |
| `velocidade_da_voz` | Taxa de fala. Faixa válida: 0,8~2,0, precisão de uma casa decimal. (padrão: 1) | FLOAT | Não | 0.8-2.0 |

**Requisitos de Vídeo:**

- O arquivo de vídeo não deve ser maior que 100MB
- A altura/largura deve estar entre 720px e 1920px
- A duração deve estar entre 2s e 10s

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | Vídeo gerado com áudio sincronizado labialmente | VIDEO |
| `video_id` | Identificador único para o vídeo gerado | STRING |
| `duration` | Informação de duração para o vídeo gerado | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f16200d52ba05acfedebc027dde91e2c91bdbb80086888d947c9f56a4e92856d`

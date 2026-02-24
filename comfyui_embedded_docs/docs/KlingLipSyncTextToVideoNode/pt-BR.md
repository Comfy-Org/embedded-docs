> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/pt-BR.md)

O nó Kling Lip Sync Text to Video sincroniza os movimentos da boca em um arquivo de vídeo para corresponder a um prompt de texto. Ele recebe um vídeo de entrada e gera um novo vídeo onde os movimentos labiais do personagem estão alinhados com o texto fornecido. O nó usa síntese de voz para criar uma sincronização de fala com aparência natural.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sim | - | Arquivo de vídeo de entrada para sincronização labial |
| `text` | STRING | Sim | - | Conteúdo de Texto para Geração de Vídeo Lip-Sync. Obrigatório quando o modo é text2video. Comprimento máximo de 120 caracteres. |
| `voice` | COMBO | Não | "Melody"<br>"Bella"<br>"Aria"<br>"Ethan"<br>"Ryan"<br>"Dorothy"<br>"Nathan"<br>"Lily"<br>"Aaron"<br>"Emma"<br>"Grace"<br>"Henry"<br>"Isabella"<br>"James"<br>"Katherine"<br>"Liam"<br>"Mia"<br>"Noah"<br>"Olivia"<br>"Sophia" | Seleção de voz para o áudio de sincronização labial (padrão: "Melody") |
| `voice_speed` | FLOAT | Não | 0.8-2.0 | Taxa de Fala. Intervalo válido: 0.8~2.0, com precisão de uma casa decimal. (padrão: 1) |

**Requisitos do Vídeo:**

- O arquivo de vídeo não deve ser maior que 100MB
- Altura/largura deve estar entre 720px e 1920px
- A duração deve estar entre 2s e 10s

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | Vídeo gerado com áudio sincronizado labialmente |
| `video_id` | STRING | Identificador único para o vídeo gerado |
| `duration` | STRING | Informação de duração para o vídeo gerado |

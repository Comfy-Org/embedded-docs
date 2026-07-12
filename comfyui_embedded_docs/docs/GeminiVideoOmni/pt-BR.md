# Google Gemini Omni (Vídeo)

Gere um vídeo com áudio a partir de um prompt de texto usando o modelo Gemini Omni Flash do Google. Opcionalmente, forneça imagens e/ou vídeos de referência para guiar ou editar o resultado. Descreva o comprimento desejado (3-10s) e a proporção (16:9 ou 9:16) diretamente no prompt.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo Gemini de vídeo usado para gerar o vídeo. | MODEL | Yes | "Omni Flash" |
| `seed` | Seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente do seed. | INT | Yes | 0 to 2147483647 |
| `prompt` | The text prompt describing the video to generate. Must be at least one non-whitespace character after stripping leading/trailing whitespace. | STRING | Yes | Minimum 1 character after stripping whitespace |
| `images` | Optional reference images to guide the video generation. Maximum of 14 images total. | IMAGE | No | Multiple images allowed (max 14) |
| `videos` | Optional reference videos to guide or edit the video generation. Maximum of 3 videos, each up to 10 seconds. | VIDEO | No | Multiple videos allowed (max 3, each max 10s) |
| `temperature` | Controls randomness in generation (default: 1.0). | FLOAT | No | 0.0 to 2.0 |
| `top_p` | Nucleus sampling parameter (default: 0.95). | FLOAT | No | 0.0 to 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `VIDEO` | The generated video with audio from the Gemini model. | VIDEO |
| `STRING` | Any text response from the model, such as reasoning or explanations. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/pt-BR.md)

---
**Source fingerprint (SHA-256):** `046842b7ec736283bba355aaa038b02fcf2416020f5f7aee7b0150d2a05bcbe6`

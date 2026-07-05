# GeminiVideoOmni

Gere um vídeo com áudio a partir de um prompt de texto usando o modelo Google Gemini Omni Flash. Opcionalmente, forneça imagens e/ou vídeos de referência para orientar ou editar o resultado. Descreva a duração desejada (3-10s) e a proporção de aspecto (16:9 ou 9:16) diretamente no prompt.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de vídeo Gemini usado para gerar o vídeo. | MODEL | Sim | "Omni Flash" |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 42). | INT | Sim | 0 a 2147483647 |
| `prompt` | O prompt de texto descrevendo o vídeo a ser gerado. | STRING | Sim | Mínimo de 1 caractere após remover espaços em branco |
| `images` | Imagens de referência opcionais para orientar a geração do vídeo. Máximo de 14 imagens no total. | IMAGE | Não | Múltiplas imagens permitidas (máx. 14) |
| `videos` | Vídeos de referência opcionais para orientar ou editar a geração do vídeo. Máximo de 3 vídeos, cada um com até 10 segundos. | VIDEO | Não | Múltiplos vídeos permitidos (máx. 3, cada um máx. 10s) |
| `temperature` | Controla a aleatoriedade na geração (padrão: 1.0). | FLOAT | Não | 0.0 a 2.0 |
| `top_p` | Parâmetro de amostragem por núcleo (padrão: 0.95). | FLOAT | Não | 0.0 a 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado com áudio do modelo Gemini. | VIDEO |
| `STRING` | Qualquer resposta de texto do modelo, como raciocínio ou explicações. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/pt-BR.md)

---
**Source fingerprint (SHA-256):** `046842b7ec736283bba355aaa038b02fcf2416020f5f7aee7b0150d2a05bcbe6`

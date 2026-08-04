# Google Gemini Omni (Vídeo)

Gere um vídeo com áudio a partir de um prompt de texto usando o modelo Google Gemini Omni Flash. Opcionalmente, forneça imagens e/ou vídeos de referência para orientar ou editar o resultado. Descreva a duração desejada (3-10s) e a proporção de tela (16:9 ou 9:16) diretamente no prompt.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|----------------|--------------|-----------|
| `model` | O modelo de vídeo Gemini usado para gerar o vídeo. | COMBO | Sim | "Omni Flash" |
| `seed` | O `seed` controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente do seed (padrão: 42). | INT | Sim | 0 a 2147483647 |
| `prompt` | O prompt de texto que descreve o vídeo a ser gerado. Deve ter pelo menos um caractere que não seja espaço em branco após remover espaços em branco no início e no final. | STRING | Sim | Mínimo de 1 caractere após remover espaços em branco |
| `images` | Imagens de referência opcionais para orientar a geração do vídeo. Máximo de 14 imagens no total. | IMAGE | Não | Múltiplas imagens permitidas (máx. 14) |
| `videos` | Vídeos de referência opcionais para orientar ou editar a geração do vídeo. Máximo de 3 vídeos, cada um com até 10 segundos. | VIDEO | Não | Múltiplos vídeos permitidos (máx. 3, cada um com até 10s) |
| `temperature` | Controla a aleatoriedade na geração (padrão: 1.0). | FLOAT | Não | 0.0 a 2.0 |
| `top_p` | Parâmetro de amostragem de núcleo (padrão: 0.95). | FLOAT | Não | 0.0 a 1.0 |

Notas:
- Se uma entrada de imagem contiver vários quadros, cada quadro conta para o máximo de 14 imagens.
- Quando `images` ou `videos` forem fornecidos, o tamanho combinado da mídia codificada deve permanecer abaixo de cerca de 90 MB; caso contrário, o nó gerará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado com áudio a partir do modelo Gemini. | VIDEO |
| `STRING` | Qualquer resposta de texto do modelo, como raciocínio ou explicações. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1b7ca51d07cfb6a166cfed2a7e7174fd62f3290abcc1bdfdce94369dda242d3f`

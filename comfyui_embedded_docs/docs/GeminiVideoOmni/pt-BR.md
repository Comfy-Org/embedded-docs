# Google Gemini Omni (Vídeo)

Gere um vídeo com áudio a partir de um prompt de texto usando o modelo Gemini Omni Flash do Google. Opcionalmente, forneça imagens e/ou vídeos de referência para orientar ou editar o resultado. Descreva a duração desejada (3 a 10 segundos) e a proporção de tela (16:9 ou 9:16) diretamente no prompt.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de vídeo Gemini usado para gerar o vídeo. | DYNAMIC_COMBO | Sim | "Omni Flash" |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed (padrão: 42). | INT | Sim | 0 a 2147483647 |

### Entradas do Omni Flash

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descreva o vídeo a ser gerado. Especifique a duração e a proporção de tela diretamente no prompt, por exemplo, "um clipe de 6 segundos em 16:9". A duração pode ser de 3 a 10 segundos; a proporção deve ser 16:9 (paisagem) ou 9:16 (retrato). A saída é 720p, 24 FPS, com áudio. | STRING | Sim | Mínimo de 1 caractere após remover espaços em branco |
| `images` | Slot expansível: conecte uma ou mais imagens de referência (`image_1`...`image_14`) para orientar ou animar o vídeo. Até 14 imagens no total. | IMAGE | Não | 0 a 14 imagens |
| `videos` | Slot expansível: conecte um ou mais vídeos de referência (`video_1`...`video_3`) para orientar ou editar. Até 3 vídeos, cada um com no máximo 10 segundos. | VIDEO | Não | 0 a 3 vídeos, cada um com no máximo 10 segundos |
| `temperature` | Controla a aleatoriedade. Quanto menor, mais focado/determinístico; quanto maior, mais variado (padrão: 1.0). | FLOAT | Não | 0.0 a 2.0 |
| `top_p` | Amostragem por núcleo (nucleus sampling): amostre a partir do menor conjunto de tokens cuja probabilidade cumulativa atinja top_p (padrão: 0.95). | FLOAT | Não | 0.0 a 1.0 |

Notas:
- Se uma entrada de imagem contiver vários quadros, cada quadro conta para o máximo de 14 imagens.
- Quando imagens ou vídeos de referência são fornecidos, o tamanho total da mídia codificada deve permanecer abaixo de cerca de 90 MB; caso contrário, o nó gera um erro.
- Quando nenhuma imagem ou vídeo de referência é fornecido, o nó gera o vídeo apenas a partir do prompt de texto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado com áudio a partir do modelo Gemini. | VIDEO |
| `STRING` | Qualquer resposta de texto do modelo, como raciocínio ou explicações. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1b7ca51d07cfb6a166cfed2a7e7174fd62f3290abcc1bdfdce94369dda242d3f`

# Google Gemini Omni (Vídeo)

Gere um vídeo com áudio a partir de um prompt de texto usando o modelo Gemini Omni Flash do Google. Opcionalmente, forneça imagens e/ou vídeos de referência para guiar ou editar o resultado. Descreva a duração desejada (3-10s) e a proporção de aspecto (16:9 ou 9:16) diretamente no prompt.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de vídeo Gemini usado para gerar o vídeo. | DYNAMIC_COMBO | Sim | "Omni Flash" |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 42). | INT | Sim | 0 a 2147483647 |

### Entradas do Omni Flash

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descreva o vídeo a ser gerado. Especifique a duração e a proporção de aspecto diretamente no prompt, ex.: "um clipe de 6 segundos em 16:9". A duração pode ser de 3 a 10 segundos; a proporção de aspecto deve ser 16:9 (paisagem) ou 9:16 (retrato). A saída é 720p, 24 FPS, com áudio. | STRING | Sim | Mínimo de 1 caractere após remover espaços em branco |
| `temperature` | Controla a aleatoriedade. Valores mais baixos são mais focados/determinísticos, valores mais altos são mais variados (padrão: 1.0). | FLOAT | Não | 0.0 a 2.0 |
| `top_p` | Amostragem de núcleo: amostra do menor conjunto de tokens cuja probabilidade cumulativa atinja top_p (padrão: 0.95). | FLOAT | Não | 0.0 a 1.0 |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | Slot expansível: conecte uma ou mais imagens de referência (`image_1`...`image_14`) para guiar ou animar o vídeo. Até 14 imagens no total. | IMAGE | Não | 0 a 14 imagens |
| `videos` | Slot expansível: conecte um ou mais vídeos de referência (`video_1`...`video_3`) para guiar ou editar. Até 3 vídeos, cada um com até 10 segundos de duração. | VIDEO | Não | 0 a 3 vídeos, cada um com no máximo 10 segundos |

Notas:
- Se uma entrada de imagem contiver vários frames, cada frame conta para o máximo de 14 imagens.
- Quando imagens ou vídeos de referência são fornecidos, o tamanho total da mídia codificada deve permanecer abaixo de cerca de 90 MB; caso contrário, o nó gera um erro.
- Quando nenhuma imagem ou vídeo de referência é fornecido, o nó gera o vídeo apenas a partir do prompt de texto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado com áudio do modelo Gemini. | VIDEO |
| `STRING` | Qualquer resposta de texto do modelo, como raciocínio ou explicações. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/pt-BR.md)

---
**Source fingerprint (SHA-256):** `648844868affb68298d2eac8ac20095bfe378d32e721396781de330ef6a6d69f`

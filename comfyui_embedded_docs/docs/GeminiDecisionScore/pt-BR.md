# Google Gemini Decision (Score)

Avalie o texto, as imagens, o áudio ou o vídeo que você conectar de 1 a 10 e receba a pontuação mais um booleano que muda em um limite definido por você. Use isso para filtrar ou ordenar saídas, por exemplo, para manter apenas imagens com pontuação de pelo menos 7, e conecte `result` a um nó If/Else Switch para agir sobre isso.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar (padrão: `"gemini-decision-1"`). | COMBO | Sim | `"gemini-decision-1"` |
| `question` | O que avaliar, dizendo o que 1 e 10 significam (padrão: "Rate the technical quality of the image from 1 (worst) to 10 (best)."). | STRING | Sim | 1 a 5000 caracteres |
| `threshold` | `result` é verdadeiro quando a pontuação é pelo menos este valor. Imagens limpas e nítidas pontuam cerca de 7 a 8, e imagens muito danificadas cerca de 3 a 5 (padrão: 6.0). | FLOAT | Sim | 1.0 a 10.0 (passo 0.1) |
| `images` | Imagens a avaliar, até 16 nos slots expansíveis (`image_1` ... `image_16`). Uma imagem em lote conta uma vez por imagem. | IMAGE | Não | Até 16 imagens |
| `audio` | Clipe de áudio a avaliar. | AUDIO | Não | - |
| `video` | Clipe de vídeo a avaliar. | VIDEO | Não | - |
| `text` | Texto sobre o qual a pergunta trata, como um prompt ou uma resposta de LLM, até 20000 caracteres. | STRING | Não | Até 20000 caracteres |

Conecte pelo menos um entre `text`, `images`, `audio` ou `video`; o nó gera um erro quando não há nada para avaliar. Com várias imagens, nomeie-as `image_1`, `image_2` e assim por diante dentro da pergunta.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `result` | Verdadeiro quando a pontuação for pelo menos `threshold`; caso contrário, falso. | BOOLEAN |
| `score` | A avaliação de 1 a 10. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionScore/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9b0a68cc7f29b1d4d23e23e051a008f34932aac6d1fe1a16e45a0e70b4df412f`

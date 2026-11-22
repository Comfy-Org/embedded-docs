# HeyGen Decision (Score)

Avalie de 1 a 10 o texto, as imagens, o áudio ou o vídeo que você conectar e receba a pontuação mais um booleano que muda de estado no limite definido por você. Use isso para filtrar ou classificar saídas e conecte `result` a um nó If/Else Switch para agir com base na pontuação.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a usar. `heygen-decision-1-turbo` é mais rápido e custa menos que `heygen-decision-1` (padrão: `"heygen-decision-1"`). | COMBO | Sim | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `pergunta` | O que avaliar, indicando o que 1 e 10 significam (padrão: "Rate the technical quality of the image from 1 (worst) to 10 (best)."). | STRING | Sim | 1 a 5000 caracteres |
| `limiar` | `result` é true quando a pontuação é pelo menos este valor. Imagens limpas e nítidas pontuam cerca de 7; imagens muito danificadas, cerca de 3 a 5 (padrão: 6.0). | FLOAT | Sim | 1.0 a 10.0 (passo: 0.1) |
| `imagens` | Imagens para avaliar, até 4 no total, contando cada quadro de um lote. Elas são numeradas de `image_1` a `image_4` em ordem entre os soquetes. | IMAGE | Não | Até 4 imagens |
| `audio_1` | Áudio para avaliar, até 30 minutos. | AUDIO | Não | Até 30 minutos |
| `video_1` | Vídeo para avaliar, até 60 segundos. | VIDEO | Não | Até 60 segundos |
| `texto` | Texto sobre o qual a pergunta trata, como um prompt ou uma resposta de LLM, até 20000 caracteres. | STRING | Não | Até 20000 caracteres |

Conecte pelo menos uma entrada para avaliar e nomeie-as pelo soquete dentro da pergunta, por exemplo "Quão nítida está a image_1?".

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `result` | True quando a pontuação é pelo menos `threshold`; caso contrário, false. | BOOLEAN |
| `score` | A pontuação de 1 a 10. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionScore/pt-BR.md)

---
**Source fingerprint (SHA-256):** `47f7aeab15292a2156b8da23c9911f4155c5b05c9ea9c0c502c30221aa522b58`

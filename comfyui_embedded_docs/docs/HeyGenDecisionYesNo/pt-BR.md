# HeyGen Decision (Yes/No)

Faça uma pergunta de sim/não sobre o texto, as imagens, o áudio ou o vídeo que você conectar e obtenha um booleano para rotear. Conecte `result` a um nó If/Else Switch para escolher entre dois caminhos, e leia `answer` e `probability` para ver quão clara foi a resposta.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a usar. `heygen-decision-1-turbo` é mais rápido e custa menos que `heygen-decision-1` (padrão: `"heygen-decision-1"`). | COMBO | Sim | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `pergunta` | A pergunta de sim/não sobre o que está conectado, com até 5000 caracteres. Faça-a de modo que "sim" seja o caso em que você age (padrão: "Is there a person in the image?"). | STRING | Sim | 1 a 5000 caracteres |
| `limiar` | Probabilidade de "sim" na qual `result` se torna verdadeiro; respostas claras ficam próximas de 0 ou 1 (padrão: 0.5). | FLOAT | Sim | 0.01 a 0.99 (passo 0.01) |
| `imagens` | Imagens sobre as quais perguntar, até 4 no total, contando cada quadro de um lote. Elas são numeradas de `image_1` a `image_4` em ordem entre os soquetes. | IMAGE | Não | Até 4 imagens |
| `audio_1` | Áudio sobre o qual perguntar, até 30 minutos. | AUDIO | Não | Até 30 minutos |
| `video_1` | Vídeo sobre o qual perguntar, até 60 segundos. | VIDEO | Não | Até 60 segundos |
| `texto` | Texto sobre o qual a pergunta é feita, como um prompt ou uma resposta de LLM, com até 20000 caracteres. | STRING | Não | Até 20000 caracteres |

Conecte pelo menos um de `text`, `images`, `audio_1` ou `video_1`, e refira-se a eles pelo nome do soquete dentro da pergunta, por exemplo: "A image_2 mostra a mesma pessoa que image_1?".

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `result` | Verdadeiro quando a probabilidade de "sim" atinge `threshold`, falso caso contrário. | BOOLEAN |
| `answer` | O veredito como a string `"yes"` ou `"no"`, seguindo o mesmo `threshold` que `result`. | STRING |
| `probability` | Probabilidade de "sim" entre 0 e 1. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionYesNo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5a6a606d5c6ef62eb3424bd54a0da3dc177da7d0acf4b5c235a62b78ad8d2df1`

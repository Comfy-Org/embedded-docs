# Google Gemini Decision (Yes/No)

Faça uma pergunta de sim/não sobre o texto, imagens, áudio ou vídeo que você conectar e obtenha um booleano para rotear. Conecte `result` a um nó If/Else Switch para enviar a execução por um de dois caminhos e leia `answer` e `probability` quando quiser ver por que o modelo respondeu dessa forma.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a usar (padrão: `"gemini-decision-1"`). | COMBO | Sim | `"gemini-decision-1"` |
| `pergunta` | A pergunta de sim/não sobre o que está conectado, com até 5000 caracteres. Faça a pergunta de modo que "sim" seja o caso sobre o qual você age (padrão: "Is there a person in the image?"). | STRING | Sim | 1 a 5000 caracteres |
| `limiar` | Probabilidade de "sim" na qual `result` se torna True. Respostas claras de "sim" têm pontuação de cerca de 0.85 a 0.92, então 0.9 ou mais rejeita muitas delas (padrão: 0.5). | FLOAT | Sim | 0.01 a 0.99 (passo 0.01) |
| `imagens` | Imagens sobre as quais perguntar, até 16 nos slots expansíveis (`image_1` ... `image_16`). Uma imagem em lote é contada uma vez por imagem. | IMAGE | Não | Até 16 imagens |
| `áudio` | Clipe de áudio sobre o qual perguntar. | AUDIO | Não | - |
| `vídeo` | Clipe de vídeo sobre o qual perguntar. | VIDEO | Não | - |
| `texto` | Texto sobre o qual a pergunta é feita, como um prompt ou uma resposta de LLM, com até 20000 caracteres. | STRING | Não | Até 20000 caracteres |

Conecte pelo menos um de `text`, `images`, `audio` ou `video`; o nó gera um erro quando não há nada para examinar. Com várias imagens, nomeie-as `image_1`, `image_2` e assim por diante dentro da pergunta: um lote é expandido quadro a quadro, então os números contam quadros individuais entre os slots na ordem de conexão.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `result` | True quando a probabilidade de "sim" atinge `threshold`, False caso contrário. | BOOLEAN |
| `answer` | O veredito como a string `"yes"` ou `"no"`, seguindo o mesmo `threshold` de `result`. | STRING |
| `probability` | Probabilidade de "sim" entre 0 e 1. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionYesNo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0339031baf5648609b82526bed97ce8744986878bcbb706dcd3aa79a7370d83f`

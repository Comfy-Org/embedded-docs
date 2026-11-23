# TypeSafe Jev (Yes/No)

O nó TypeSafe Jev (Yes/No) faz uma pergunta de sim ou não sobre o texto, as imagens ou ambos conectados e retorna a resposta como um booleano. Conecte `result` a um nó If/Else Switch para rotear o fluxo de trabalho, ou leia `probability` para agir conforme o quão confiante o modelo está. Este é um nó de API: ele é executado nos servidores da Comfy e exige uma conta em Comfy.org com créditos.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo Jev a usar. Apenas um modelo está disponível no momento: `jev-1.14.0`. | COMBO | Sim | `"jev-1.14.0"` |
| `question` | A pergunta de sim ou não que o texto e as imagens conectados respondem. Faça-a de modo que o sim seja o caso sobre o qual você age; com várias conexões de imagem, use os nomes delas, por exemplo `Does image_2 show the same person as image_1?` (padrão: `Is there a person in the image?`). | STRING | Sim | 1 a 1000 caracteres |
| `threshold` | A resposta será sim quando a probabilidade de sim for pelo menos este valor (padrão: 0.5). | FLOAT | Sim | 0.01 a 0.99 (passo 0.01) |
| `images` | As imagens sobre as quais a pergunta trata. Até 32 imagens no total; uma entrada em lote conta uma vez por imagem. O lado maior de cada imagem é limitado pelo número total de imagens: 1568 px para até 4 imagens, 1024 px para até 8, 768 px para até 16 e 512 px para até 32, então um lote maior pode reduzir o detalhe em cada imagem. | AUTOGROW | Não | 0 a 32 imagens |
| `text` | O texto sobre o qual a pergunta trata, como um prompt ou uma resposta de LLM. | STRING | Não | 0 a 3000 caracteres |

**Notas:**

- Conecte texto ou pelo menos uma imagem; o nó gera um erro quando ambos estão vazios.
- `result` é verdadeiro quando `probability` é pelo menos `threshold`, e `answer` retorna o mesmo veredito na forma de `yes` ou `no`.
- A cobrança é baseada em tokens; o selo de preço no nó mostra a taxa aproximada por 1 milhão de tokens.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `result` | A resposta como booleano: verdadeiro quando a probabilidade de sim for pelo menos `threshold`. | BOOLEAN |
| `answer` | A resposta como o texto `yes` ou `no`. | STRING |
| `probability` | Probabilidade de sim, de 0 (definitivamente não) a 1 (definitivamente sim). | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`

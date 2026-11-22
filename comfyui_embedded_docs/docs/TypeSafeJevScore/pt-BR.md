# TypeSafe Jev (Score)

O nó TypeSafe Jev (Score) avalia texto, imagens ou ambos conectados de 1 a 10 e compara a avaliação com um limite. Conecte `result` a um nó If/Else Switch para agir com base na pontuação, ou leia `score` para usar a avaliação bruta. Este é um nó de API e requer uma conta no Comfy.org e uma chave de API.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo Jev a usar. Apenas um modelo está disponível no momento: `jev-1.14.0`. | COMBO | Sim | `"jev-1.14.0"` |
| `question` | O que avaliar, em uma escala de 1 a 10. Diga o que 1 e 10 significam, como no padrão (padrão: `Rate the technical quality of the image from 1 (worst) to 10 (best).`). | STRING | Sim | 1 a 1000 caracteres |
| `threshold` | `result` é True quando a pontuação é pelo menos este valor (padrão: 5.0). | FLOAT | Sim | 1.0 a 10.0 (passo: 0.1) |
| `images` | As imagens sobre as quais a pergunta se refere. Até 32 imagens no total; uma entrada em lote conta uma vez por imagem, e mais de 4 imagens são enviadas em um tamanho menor. | AUTOGROW | Não | 0 a 32 imagens |
| `text` | O texto sobre o qual a pergunta se refere, como um prompt ou uma resposta de LLM. | STRING | Não | 0 a 3000 caracteres |

**Observações:**

- Conecte texto ou pelo menos uma imagem; o nó gera um erro quando ambos estão vazios.
- A pontuação é reportada de 1 a 10, e `result` é True quando ela é pelo menos `threshold`.
- A cobrança é baseada em tokens; o selo de preço no nó mostra a tarifa aproximada por 1 milhão de tokens.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `result` | True quando `score` é pelo menos `threshold`. | BOOLEAN |
| `score` | A avaliação de 1 (pior) a 10 (melhor). | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevScore/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7e1970e903d2099ab3d7481a758c5291e87614b9eaf116d0ced6a1bcd36dc126`

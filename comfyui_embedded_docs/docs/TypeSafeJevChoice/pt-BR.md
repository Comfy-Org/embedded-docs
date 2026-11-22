# TypeSafe Jev (Choice)

O nó TypeSafe Jev (Choice) escolhe uma das suas próprias opções para texto conectado, imagens ou ambos. Conecte `choice` a um nó Branch cujas entradas carregam os nomes das opções, ou use `option_index` para alternar com base na posição da opção escolhida. Este é um nó de API e requer uma conta Comfy.org e uma chave de API.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo Jev a usar. Apenas um modelo está disponível atualmente: `jev-1.14.0`. | COMBO | Sim | `"jev-1.14.0"` |
| `question` | A pergunta que as opções respondem. Com vários sockets de imagem, use seus nomes, por exemplo `Which season is shown in image_1?` (padrão: `What style is the image?`). | STRING | Sim | 1 a 1000 caracteres |
| `options` | As opções para escolher, uma por linha. Adicione uma opção como `other` para entradas que não se encaixem em nenhuma delas (padrão: `photo`, `illustration`, `3d render`, `anime`, `sketch` e `other`, uma por linha). | STRING | Sim | 2 a 50 opções, até 40 caracteres cada |
| `images` | As imagens sobre as quais a pergunta é feita. Até 32 imagens no total; uma entrada em lote conta uma vez por imagem, e mais de 4 imagens são enviadas em um tamanho menor. | AUTOGROW | Não | 0 a 32 imagens |
| `text` | O texto sobre o qual a pergunta é feita, como um prompt ou uma resposta de LLM. | STRING | Não | 0 a 3000 caracteres |

**Notas:**

- Conecte texto ou pelo menos uma imagem; o nó gera um erro quando ambos estão vazios.
- O nó gera um erro quando menos de 2 ou mais de 50 opções são fornecidas, quando uma opção tem mais de 40 caracteres, ou quando duas opções diferem apenas por maiúsculas/minúsculas.
- `option_index` conta a partir de 0, então a primeira opção da lista tem índice 0.
- A cobrança é baseada em tokens; o selo de preço no nó mostra a taxa aproximada por 1M de tokens.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `choice` | A opção escolhida, escrita exatamente como aparece em `options`. | STRING |
| `option_index` | Posição da opção escolhida na lista de opções, começando em 0. | INT |
| `confidence` | O quão segura a Jev está, de 0 (nenhum vencedor claro) a 1 (certeza). | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`

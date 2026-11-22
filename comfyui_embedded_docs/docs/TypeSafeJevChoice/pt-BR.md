# TypeSafe Jev (Choice)

O nó TypeSafe Jev (Choice) escolhe uma das suas próprias opções para texto conectado, imagens ou ambos. Conecte `choice` a um nó Branch cujas entradas carregam os nomes das opções, ou use `option_index` para alternar conforme a posição da opção escolhida. Um nó Branch aceita no máximo 32 entradas, então uma lista com mais opções do que isso só pode ser encaminhada por `option_index`. Este é um nó de API: ele é executado nos servidores da Comfy e requer uma conta Comfy.org com créditos.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo Jev a usar. Apenas um modelo está disponível atualmente: `jev-1.14.0`. | COMBO | Sim | `"jev-1.14.0"` |
| `question` | A pergunta que as opções respondem. Com várias entradas de imagem, use os nomes delas, por exemplo, `Which season is shown in image_1?` (padrão: `What style is the image?`). | STRING | Sim | 1 a 1000 caracteres |
| `options` | As opções entre as quais escolher, uma por linha. Espaços em branco no início e no fim são removidos de cada linha, e as opções devem ser exclusivas ignorando maiúsculas e minúsculas, então uma opção repetida ou duas opções que difiram apenas em maiúsculas/minúsculas são rejeitadas. Adicione uma opção como `other` para entradas que não se encaixem em nenhuma delas (padrão: `photo`, `illustration`, `3d render`, `anime`, `sketch` e `other`, uma por linha). | STRING | Sim | 2 a 50 opções, até 40 caracteres cada |
| `images` | As imagens sobre as quais a pergunta trata. Até 32 imagens no total; uma entrada em lote conta uma vez por imagem. O lado maior de cada imagem é limitado pelo número total de imagens: 1568 px para até 4 imagens, 1024 px para até 8, 768 px para até 16 e 512 px para até 32, assim, um lote maior pode reduzir o detalhe em cada imagem. | AUTOGROW | Não | 0 a 32 imagens |
| `text` | O texto sobre o qual a pergunta trata, como um prompt ou uma resposta de LLM. | STRING | Não | 0 a 3000 caracteres |

**Notas:**

- Conecte texto ou pelo menos uma imagem; o nó gera um erro quando ambos estão vazios.
- O nó gera um erro quando menos de 2 ou mais de 50 opções são fornecidas, quando uma opção tem mais de 40 caracteres, ou quando duas opções são iguais ignorando maiúsculas e minúsculas.
- `option_index` conta a partir de 0, então a primeira opção da lista tem índice 0.
- A cobrança é baseada em tokens; o selo de preço no nó mostra a taxa aproximada por 1M de tokens.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `choice` | A opção escolhida, com espaços em branco no início e no fim removidos. Uma entrada Branch cujo nome mantenha esses espaços não corresponderá. | STRING |
| `option_index` | Posição da opção escolhida na lista de opções, começando em 0. | INT |
| `confidence` | O grau de certeza da Jev, de 0 (nenhum vencedor claro) a 1 (certeza). | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`

# TypeSafe Jev (Pick Image)

O nó TypeSafe Jev (Pick Image) escolhe uma imagem de um lote. Conecte o mesmo lote de imagens a Get Image from Batch junto com `index` para manter a imagem escolhida, ou leia `confidence` para decidir se a escolha é suficientemente boa. Este é um nó de API: ele é executado nos servidores da Comfy e exige uma conta em Comfy.org com créditos.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo Jev a usar. Apenas um modelo está disponível no momento: `jev-1.14.0`. | COMBO | Sim | `"jev-1.14.0"` |
| `question` | Qual imagem escolher. Conecte o prompt a `text` para escolher a imagem que melhor corresponde a ele (padrão: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | Sim | 1 a 1000 caracteres |
| `images` | As imagens entre as quais escolher. Uma entrada em lote conta uma vez por imagem, então cada imagem do lote é uma candidata. O lado maior de cada imagem é limitado pelo tamanho do lote antes do upload: 1568 px para até 4 imagens, 1024 px para até 8, 768 px para até 16 e 512 px para até 32, portanto, um lote maior significa menos detalhe em cada imagem. | IMAGE | Sim | 2 a 32 imagens |
| `text` | O texto sobre o qual a pergunta trata, como o prompt a partir do qual as imagens foram geradas. | STRING | Não | 0 a 3000 caracteres |

**Observações:**

- O nó gera um erro quando menos de 2 ou mais de 32 imagens estão conectadas.
- `index` conta a partir de 0, que é a posição que Get Image from Batch espera.
- A cobrança é baseada em tokens; o selo de preço no nó mostra a taxa aproximada por 1M de tokens.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `index` | Posição da imagem escolhida no lote, começando em 0. | INT |
| `confidence` | O quão segura a Jev está, de 0 (nenhum vencedor claro) a 1 (certeza). | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`

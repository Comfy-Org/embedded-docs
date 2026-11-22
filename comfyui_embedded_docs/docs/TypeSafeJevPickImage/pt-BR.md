# TypeSafe Jev (Pick Image)

O nó TypeSafe Jev (Pick Image) escolhe uma imagem de um lote. Conecte `index` a Get Image from Batch para manter a imagem escolhida, ou leia `confidence` para decidir se a escolha é boa o suficiente. Este é um nó de API e requer uma conta Comfy.org e uma chave de API.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo Jev a usar. Apenas um modelo está disponível atualmente: `jev-1.14.0`. | COMBO | Sim | `"jev-1.14.0"` |
| `question` | Qual imagem escolher. Conecte o prompt a `text` para escolher a imagem que melhor corresponde a ele (padrão: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | Sim | 1 a 1000 caracteres |
| `images` | As imagens entre as quais escolher. Uma entrada em lote conta uma vez por imagem, então cada imagem do lote é uma candidata. | IMAGE | Sim | 2 a 32 imagens |
| `text` | O texto sobre o qual a pergunta trata, como o prompt a partir do qual as imagens foram geradas. | STRING | Não | 0 a 3000 caracteres |

**Notas:**

- O nó gera um erro quando menos de 2 ou mais de 32 imagens estão conectadas.
- `index` conta a partir de 0, que é a posição que Get Image from Batch espera.
- A cobrança é baseada em tokens; o selo de preço no nó mostra a taxa aproximada por 1M de tokens.

## Saídas

| Nome de Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `index` | Posição da imagem escolhida no lote, começando em 0. | INT |
| `confidence` | O quão confiante o Jev está, de 0 (nenhum vencedor claro) a 1 (certeza). | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`

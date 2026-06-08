O nó TripleCLIPLoader carrega três modelos de codificador de texto diferentes simultaneamente e os combina em um único modelo CLIP. Isso é útil para cenários avançados de codificação de texto onde múltiplos codificadores de texto são necessários, como em fluxos de trabalho SD3 que exigem que os modelos clip-l, clip-g e t5 trabalhem juntos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip_name1` | O primeiro modelo de codificador de texto a ser carregado dentre os codificadores de texto disponíveis | STRING | Sim | Múltiplas opções disponíveis |
| `clip_name2` | O segundo modelo de codificador de texto a ser carregado dentre os codificadores de texto disponíveis | STRING | Sim | Múltiplas opções disponíveis |
| `clip_name3` | O terceiro modelo de codificador de texto a ser carregado dentre os codificadores de texto disponíveis | STRING | Sim | Múltiplas opções disponíveis |

**Nota:** Todos os três parâmetros do codificador de texto devem ser selecionados dentre os modelos de codificador de texto disponíveis em seu sistema. O nó carregará todos os três modelos e os combinará em um único modelo CLIP para processamento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CLIP` | Um modelo CLIP combinado contendo todos os três codificadores de texto carregados | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7a9e61090d9d3b0a776d49006dddece08bc4b463b2acd0a9a0f808170ebde348`

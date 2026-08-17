# TripleCLIPLoader

O nó TripleCLIPLoader carrega três modelos de codificador de texto ao mesmo tempo e os combina em um único modelo CLIP. Isso é útil para cenários avançados de codificação de texto onde vários codificadores de texto são necessários, como em fluxos de trabalho SD3 que exigem modelos clip-l, clip-g e t5 trabalhando juntos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|------------|----------|-------|
| `clip_name1` | O primeiro modelo de codificador de texto a carregar entre os codificadores de texto disponíveis | COMBO | Sim | Todos os arquivos de codificador de texto na pasta text_encoders |
| `clip_name2` | O segundo modelo de codificador de texto a carregar entre os codificadores de texto disponíveis | COMBO | Sim | Todos os arquivos de codificador de texto na pasta text_encoders |
| `clip_name3` | O terceiro modelo de codificador de texto a carregar entre os codificadores de texto disponíveis | COMBO | Sim | Todos os arquivos de codificador de texto na pasta text_encoders |

**Nota:** Todos os três parâmetros de codificador de texto devem ser selecionados entre os modelos de codificador de texto disponíveis no seu sistema. O nó carrega os três modelos na ordem fornecida e os combina em um único modelo CLIP para processamento. Para fluxos de trabalho SD3, use clip-l, clip-g e t5 como os três codificadores.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-----------|-------------|------------|
| `CLIP` | Um modelo CLIP combinado contendo os três codificadores de texto carregados | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`

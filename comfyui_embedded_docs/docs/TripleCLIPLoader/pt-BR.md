# TripleCLIPLoader

O TripleCLIPLoader carrega três modelos de codificador de texto ao mesmo tempo e os combina em um único modelo CLIP. Ele é usado em fluxos de trabalho que precisam de múltiplos codificadores de texto trabalhando juntos, como o SD3, que utiliza os modelos clip-l, clip-g e t5.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `clip_name1` | O primeiro modelo de codificador de texto a carregar entre os codificadores de texto disponíveis | COMBO | Sim | Múltiplas opções disponíveis (todos os arquivos na pasta text_encoders) |
| `clip_name2` | O segundo modelo de codificador de texto a carregar entre os codificadores de texto disponíveis | COMBO | Sim | Múltiplas opções disponíveis (todos os arquivos na pasta text_encoders) |
| `clip_name3` | O terceiro modelo de codificador de texto a carregar entre os codificadores de texto disponíveis | COMBO | Sim | Múltiplas opções disponíveis (todos os arquivos na pasta text_encoders) |

**Nota:** Todos os três parâmetros são obrigatórios. As opções disponíveis são os arquivos de codificador de texto na sua pasta text_encoders. Se um arquivo selecionado não for encontrado, o nó gera um erro. O nó carrega todos os três modelos selecionados e os combina em um único modelo CLIP.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `CLIP` | Um modelo CLIP combinado contendo todos os três codificadores de texto carregados | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`

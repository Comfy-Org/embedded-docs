# Breeze Voice Selector

Seleciona uma voz Breeze em destaque, ou qualquer id de voz Breeze, e a envia para o Breeze Text to Speech. O nó apenas resolve um id e não faz nenhuma chamada de API.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `language` | Grupo de idioma das vozes em destaque, ou `custom` para inserir um id. Padrão: `"English"`. | DYNAMIC_COMBO | Sim | `"English"`<br>`"Chinese"`<br>`"Japanese"`<br>`"custom"` |

### Entradas para os idiomas "English", "Chinese" e "Japanese"

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `voice` | Voz em destaque nesse idioma. | COMBO | Sim | Várias opções disponíveis |

### Entradas para o idioma "custom"

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `voice_id` | Qualquer id de voz Breeze, como uma voz criada pelos outros nós Breeze. Apenas letras, dígitos, `_` e `-`. Padrão: vazio. | STRING | Sim | id de voz Breeze |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `voice` | A voz Breeze selecionada. | BREEZE_VOICE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceSelector/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0bded8f1b6ec92abaec514ed843b3c138d804e3736758f5df3a2faf52e89a8b0`

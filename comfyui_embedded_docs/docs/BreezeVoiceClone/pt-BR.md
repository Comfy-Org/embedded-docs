# Breeze Voice Clone

Cria uma voz Breeze a partir da gravação de um único falante. A voz é salva na sua conta e retornada como um identificador de voz, junto com uma prévia de áudio de como ela soa.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `audio` | Gravação de um único falante, com pelo menos 3 segundos de duração. Apenas os primeiros 60 segundos são usados. | AUDIO | Sim | - |
| `remove_background_noise` | Limpa a gravação antes da clonagem. Padrão: false. | BOOLEAN | Não | true<br>false |
| `seed` | Controla se o nó é executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Não | 0 a 2147483647 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `voice` | A nova voz Breeze, para Breeze Text to Speech. | BREEZE_VOICE |
| `preview` | Prévia de áudio da voz clonada. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceClone/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3c2e461a8e1a38bfa494a687f5b77a375e9e81c77964493181d7c622a682c56f`

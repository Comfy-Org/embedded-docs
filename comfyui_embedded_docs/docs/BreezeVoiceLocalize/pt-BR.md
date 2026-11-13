# Breeze Voice Localize

Cria uma cópia de uma voz que fala outro idioma nativamente, em vez de ler um idioma estrangeiro com seu sotaque original. A cópia é salva na sua conta e retornada com uma prévia de áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `voice` | Voz Breeze a ser copiada. | BREEZE_VOICE | Sim | - |
| `language` | Idioma que a nova voz fala. Padrão: `"English"`. | COMBO | Sim | Múltiplas opções disponíveis |
| `seed` | Controla se o nó é executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Não | 0 a 2147483647 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `voice` | A cópia localizada da voz, nomeada com base na voz original e no idioma. | BREEZE_VOICE |
| `preview` | Prévia de áudio da voz localizada. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceLocalize/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a997fbc3426669f6e5725c455f49f3e16d5e14806ea3fac26657459f63e99db1`

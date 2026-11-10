# Breeze Voice Remix

Cria uma cópia alterada de uma voz no mesmo idioma, seja a partir de uma descrição escrita da alteração, seja a partir de um preset nomeado. A cópia é salva na sua conta e retornada com uma prévia de áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `voice` | Voz Breeze a ser alterada. | BREEZE_VOICE | Sim | - |
| `change` | `custom` descreve a alteração em texto, `preset` seleciona uma alteração nomeada. Padrão: `"custom"`. | DYNAMIC_COMBO | Sim | `"custom"`<br>`"preset"` |
| `strength` | Valores mais altos alteram mais a voz. Padrão: 4.0. | FLOAT | Não | 1.0 a 10.0 (passo: 0.1) |
| `seed` | Controla se o nó é executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Não | 0 a 2147483647 |

### Entradas de alteração "custom"

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `prompt` | Como a voz deve mudar, por exemplo, mais velha e rouca. Padrão: vazio. | STRING | Sim | Texto multilinha |

### Entradas de alteração "preset"

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `preset` | Alteração nomeada, agrupada por idade, gênero, tom, ritmo, energia e emoção. | COMBO | Sim | Várias opções disponíveis |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `voice` | A cópia alterada da voz. | BREEZE_VOICE |
| `preview` | Prévia de áudio da voz remixada. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceRemix/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1bb135706fa760c6a6e8f4b9cb12a3f1506db375ee09cbd511b62d2bb24a9d2c`

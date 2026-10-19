# HeyGen Voice 1.0 Text to Speech

Sintetize o texto em uma voz clonada com o HeyGen Voice 1.0 Instant Clone. O nó envia o texto e o ID da voz ao HeyGen e retorna a fala gerada como áudio. Dois modelos estão disponíveis: `heygen-voice-1` e o mais rápido `heygen-voice-1-turbo`, que custa metade do valor.

Selecionar um `model` revela os parâmetros específicos desse modelo.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `model` | Modelo a usar. `heygen-voice-1-turbo` é mais rápido e custa metade do valor. Selecionar um modelo revela os parâmetros específicos dele: `voice_id`, `text`, `language` e `expressiveness_boost`. | DYNAMIC_COMBO | Sim | `"heygen-voice-1"`<br>`"heygen-voice-1-turbo"` |
| `voice_id` | Voz do HeyGen Voice 1.0 Instant Clone (padrão: vazio). | STRING | Sim | N/A |
| `text` | Texto a ser falado. Até 5000 caracteres; falas com duração superior a cerca de 12 minutos falham, portanto, divida textos muito longos em chinês ou japonês (padrão: vazio). | STRING | Sim | 1 a 5000 caracteres |
| `language` | Idioma do texto. Defina-o para idiomas próximos, como sérvio ou malaio, que a detecção automática pode confundir (padrão: "auto"). | COMBO | Sim | `"auto"`<br>Várias predefinições de idioma |
| `expressiveness_boost` | Valores mais altos são mais expressivos; valores mais baixos ficam mais próximos da voz original (padrão: 0.5). | FLOAT | Sim | 0.0 a 1.0 (passo 0.05) |

**Nota:** `voice_id` deve ser uma voz criada pelo HeyGen Voice 1.0 Instant Clone; o nó é interrompido com um erro quando ele está vazio. `text` deve conter pelo menos um caractere.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---------------|-----------|---------------|
| `AUDIO` | A fala gerada a partir do texto, falada na voz clonada. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceTextToSpeechNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `61e345563db04a4dfc61e8862a328d5062aa2a77af57c2209ca4ca3862930be8`

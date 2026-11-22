# HeyGen Voice 1.0 Instant Clone Text to Speech

Clone uma voz a partir de uma gravação de um único falante e fale texto com ela usando o HeyGen Voice 1.0. O nó envia a gravação, sintetiza a fala e a retorna como áudio, de modo que um único nó leva de uma amostra de voz à fala finalizada.

Selecionar um `model` revela os parâmetros específicos dele: `audio`, `text`, `language`, `expressiveness_boost`, `recording_language`, `similarity`, `remove_background_noise` e `seed`.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar. `heygen-voice-1-turbo` é mais rápido e custa menos (padrão: `"heygen-voice-1"`). | DYNAMIC_COMBO | Sim | `"heygen-voice-1"`<br>`"heygen-voice-1-turbo"` |
| `audio` | Gravação de um único falante para clonar. Use pelo menos 10 segundos de fala clara; apenas os primeiros 3 minutos são usados. | AUDIO | Sim | - |
| `text` | Texto a ser falado, com até 5000 caracteres. Uma fala com mais de cerca de 12 minutos falha, então divida textos muito longos em chinês ou japonês (padrão: vazio). | STRING | Sim | 1 a 5000 caracteres |
| `language` | Idioma do texto. Defina-o para idiomas próximos, como sérvio ou malaio, que a detecção automática pode confundir (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>Várias predefinições de idioma |
| `expressiveness_boost` | Valores mais altos são mais expressivos; valores mais baixos permanecem mais próximos da voz original (padrão: 0.5). | FLOAT | Sim | 0.0 a 1.0 (passo 0.05) |
| `recording_language` | Idioma falado na gravação, o que restringe o clone a esse idioma (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>Várias predefinições de idioma |
| `similarity` | O quão fielmente a voz segue a gravação (padrão: `"max"`). | COMBO | Sim | `"medium"`<br>`"high"`<br>`"extra_high"`<br>`"max"` |
| `remove_background_noise` | Limpar o ruído de fundo na gravação antes da clonagem (padrão: True). | BOOLEAN | Sim | `True`<br>`False` |
| `seed` | A `seed` controla se o nó é executado novamente; os resultados são não determinísticos independentemente da seed (padrão: 42). | INT | Sim | 0 a 2147483647 |

`text` deve conter pelo menos um caractere e `audio` é obrigatório: uma gravação com vários falantes, ou uma ruidosa demais para clonar, gera uma voz ruim. Defina `recording_language` quando o idioma da amostra não for óbvio.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `AUDIO` | O texto falado na voz clonada. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceCloneTextToSpeechNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ea18e2abce687e106ed0b37eb7afd723fbe72a3b4d58124a143c00b66d2fe7c9`

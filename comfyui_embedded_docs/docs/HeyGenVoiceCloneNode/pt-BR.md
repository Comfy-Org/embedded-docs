# HeyGen Voice 1.0 Instant Clone

Clone uma voz a partir de uma gravação de um único falante com o mecanismo Voice 1.0 da HeyGen. O nó faz o upload da gravação, cria um clone de voz instantâneo, aguarda até que a HeyGen termine de processá-lo e retorna o `voice_id`. Conecte-o ao HeyGen Voice 1.0 Text to Speech, ou a `custom_voice_id` em HeyGen Avatar Video e HeyGen Talking Photo. A criação do clone é gratuita; você é cobrado pela fala que gerar com a voz.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `audio` | Gravação de um único falante. Use pelo menos 10 segundos de fala clara; apenas os primeiros 3 minutos são usados. | AUDIO | Sim | N/A |
| `language` | Idioma falado na gravação (padrão: "auto"). | COMBO | Sim | `"auto"`<br>Várias predefinições de idioma |
| `similarity` | O quão fielmente a voz segue a gravação (padrão: "max"). | COMBO | Sim | `"medium"`<br>`"high"`<br>`"extra_high"`<br>`"max"` |
| `remove_background_noise` | Limpa o ruído de fundo da gravação antes da clonagem (padrão: True). | BOOLEAN | Sim | True<br>False |
| `seed` | Altere a seed para clonar a gravação novamente; cada clone é uma voz ligeiramente diferente (padrão: 42). | INT | Sim | 0 a 2147483647 |

**Observação:** A voz é criada como "ComfyUI Voice" na sua conta HeyGen, e o nó imprime o `voice_id` na UI para que você possa copiá-lo para reutilização. Deixe `language` em "auto" a menos que o falante fale um idioma que possa ser facilmente confundido com outro proximamente relacionado. A entrada `seed` inclui um controle fixo Control After Generate na UI, então altere-o manualmente quando quiser outro clone.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `voice_id` | O ID da voz clonada, para reutilização no nó HeyGen Voice 1.0 Text to Speech ou como um `custom_voice_id`. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceCloneNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0bf5c7170d140936841cc4afd28022574df8e4c2280137607dcfca8e36862317`

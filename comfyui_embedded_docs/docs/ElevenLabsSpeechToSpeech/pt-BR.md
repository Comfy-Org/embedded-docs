Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/en.md)

O nó ElevenLabs Speech to Speech transforma um arquivo de áudio de entrada de uma voz para outra. Ele usa a API ElevenLabs para converter a fala, preservando o conteúdo original e o tom emocional do áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `voz` | Voz de destino para a transformação. Conecte a partir do Seletor de Voz ou Clone de Voz Instantâneo. | CUSTOM | Sim | - |
| `áudio` | Áudio de origem a ser transformado. | AUDIO | Sim | - |
| `estabilidade` | Estabilidade da voz. Valores mais baixos proporcionam uma gama emocional mais ampla; valores mais altos produzem uma fala mais consistente, mas potencialmente monótona (padrão: 0.5). | FLOAT | Não | 0.0 - 1.0 |
| `modelo` | Modelo a ser usado para a transformação de fala para fala. Cada opção fornece um conjunto específico de configurações de voz (similarity_boost, style, use_speaker_boost, speed). | DYNAMICCOMBO | Não | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` |
| `formato_de_saida` | Formato de saída do áudio (padrão: "mp3_44100_192"). | COMBO | Não | `"mp3_44100_192"`<br>`"opus_48000_192"` |
| `semente` | Semente para reprodutibilidade (padrão: 0). | INT | Não | 0 - 4294967295 |
| `remover_ruído_de_fundo` | Remove o ruído de fundo do áudio de entrada usando isolamento de áudio (padrão: False). | BOOLEAN | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `áudio` | O arquivo de áudio transformado no formato de saída especificado. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/pt-BR.md)

---
**Source fingerprint (SHA-256):** `118fe6e85b146d0649b104d814abb518d37f69ade2e53becac365a0ec90146fd`

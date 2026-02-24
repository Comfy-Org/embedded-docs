> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/pt-BR.md)

O nó ElevenLabs Speech to Speech transforma um arquivo de áudio de entrada de uma voz para outra. Ele usa a API da ElevenLabs para converter a fala, preservando o conteúdo original e o tom emocional do áudio.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `voice` | CUSTOM | Sim | - | Voz de destino para a transformação. Conecte a partir do Seletor de Voz ou da Clonagem Instantânea de Voz. |
| `audio` | AUDIO | Sim | - | Áudio de origem a ser transformado. |
| `stability` | FLOAT | Não | 0.0 - 1.0 | Estabilidade da voz. Valores mais baixos proporcionam uma gama emocional mais ampla, valores mais altos produzem uma fala mais consistente, mas potencialmente monótona (padrão: 0.5). |
| `model` | DYNAMICCOMBO | Não | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` | Modelo a ser usado para a transformação de fala em fala. Cada opção fornece um conjunto específico de configurações de voz (similarity_boost, style, use_speaker_boost, speed). |
| `output_format` | COMBO | Não | `"mp3_44100_192"`<br>`"opus_48000_192"` | Formato de saída do áudio (padrão: "mp3_44100_192"). |
| `seed` | INT | Não | 0 - 4294967295 | Semente para reprodutibilidade (padrão: 0). |
| `remove_background_noise` | BOOLEAN | Não | - | Remove o ruído de fundo do áudio de entrada usando isolamento de áudio (padrão: False). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `audio` | AUDIO | O arquivo de áudio transformado no formato de saída especificado. |
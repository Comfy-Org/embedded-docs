> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/pt-BR.md)

O nó ElevenLabs Instant Voice Clone cria um novo modelo de voz único analisando de 1 a 8 gravações de áudio da voz de uma pessoa. Ele envia essas amostras para a API da ElevenLabs, que as processa para gerar um clone de voz que pode ser usado para síntese de texto em fala.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `audio_*` | AUDIO | Sim | 1 a 8 arquivos | Gravações de áudio para clonagem de voz. Você deve fornecer entre 1 e 8 arquivos de áudio. |
| `remove_background_noise` | BOOLEAN | Não | Verdadeiro / Falso | Remove ruído de fundo das amostras de voz usando isolamento de áudio. (padrão: Falso) |

**Observação:** Você deve fornecer pelo menos um arquivo de áudio, podendo fornecer até oito. O nó criará automaticamente slots de entrada para os arquivos de áudio que você adicionar.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `voice` | ELEVENLABS_VOICE | O identificador único para o modelo de voz clonado recém-criado. Esta saída pode ser conectada a outros nós de texto em fala da ElevenLabs. |

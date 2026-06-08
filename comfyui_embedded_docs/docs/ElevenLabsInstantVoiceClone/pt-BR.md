Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/en.md)

O nó ElevenLabs Instant Voice Clone cria um novo modelo de voz único analisando de 1 a 8 gravações de áudio da voz de uma pessoa. Ele envia essas amostras para a API do ElevenLabs, que as processa para gerar um clone de voz que pode ser usado para síntese de texto para fala.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `audio_*` | Gravações de áudio para clonagem de voz. Você deve fornecer entre 1 e 8 arquivos de áudio. | AUDIO | Sim | 1 a 8 arquivos |
| `remover_ruído_de_fundo` | Remove ruído de fundo das amostras de voz usando isolamento de áudio. (padrão: Falso) | BOOLEAN | Não | Verdadeiro / Falso |

**Nota:** Você deve fornecer pelo menos um arquivo de áudio e pode fornecer até oito. O nó criará automaticamente slots de entrada para os arquivos de áudio que você adicionar.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `voice` | O identificador único para o modelo de voz clonado recém-criado. Esta saída pode ser conectada a outros nós de texto para fala do ElevenLabs. | ELEVENLABS_VOICE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/pt-BR.md)

---
**Source fingerprint (SHA-256):** `297598e183df3ccddabc75d6903c5c69f10648adeea430e546f9c5f6df49bdb2`

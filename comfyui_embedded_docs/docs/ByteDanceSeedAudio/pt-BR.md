# ByteDanceSeedAudio

Gere fala, música, efeitos sonoros e diálogo com múltiplos falantes a partir de um único prompt com o ByteDance Seed Audio 1.0. Descreva a(s) voz(es), emoção, ambiente, música de fundo e efeitos sonoros no prompt, e inclua as falas a serem ditas. Opcionalmente, escolha uma voz predefinida integrada, clone vozes de até 3 clipes de referência (marcados como @Audio1-3 no prompt) ou derive uma voz a partir de uma imagem de personagem. Até 2 minutos de áudio por execução.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `text_prompt` | Descreva a(s) voz(es), emoção, ritmo, ambiente, música de fundo e efeitos sonoros, e inclua as falas a serem ditas (nomeie os personagens inline para diálogo). No modo 'referência de áudio', refira-se aos clipes conectados por ordem como @Audio1, @Audio2, @Audio3. Com o modelo multilíngue, uma linha entre aspas pode começar com um intervalo de carimbo de tempo que controla quando e por quanto tempo ela é falada, ex.: `[5.5s:8.0s] Espere por mim!`. Escreva o prompt no mesmo idioma das falas. Mínimo de 1 caractere, Máximo de 3000 caracteres. | STRING | Sim | 1 a 3000 caracteres |
  - **"referência de áudio"**: Requer que pelo menos um de `reference_audio_1`, `reference_audio_2` ou `reference_audio_3` esteja conectado. Os clipes de referência devem ser conectados em ordem, sem lacunas. Cada clipe é limitado a no máximo 30 segundos. Se tags @AudioN forem usadas no prompt, o número de tag mais alto não deve exceder o número de clipes de referência conectados.
| `reference_audio_1` | Clipe de referência para clonagem de voz, marcado como @Audio1 no prompt. Até 30s. Disponível apenas quando `reference_mode` for "referência de áudio". | AUDIO | Não | Até 30 segundos |
| `reference_audio_2` | Clipe de referência marcado como @Audio2 no prompt. Até 30s. Disponível apenas quando `reference_mode` for "referência de áudio". | AUDIO | Não | Até 30 segundos |
| `reference_audio_3` | Clipe de referência marcado como @Audio3 no prompt. Até 30s. Disponível apenas quando `reference_mode` for "referência de áudio". | AUDIO | Não | Até 30 segundos |
  - **"referência de imagem"**: Requer que `reference_image` esteja conectado. Tags @AudioN não são usadas; o prompt deve conter apenas o texto a ser sintetizado.
  - **"voz predefinida"**: Requer que uma voz predefinida seja selecionada. O prompt inteiro é lido na voz selecionada; tags @AudioN não são usadas como referência, e tags como @Audio2 ou superiores são rejeitadas.
| `sample_rate` | Taxa de amostragem de saída em Hz. (padrão: "24000") | COMBO | Sim | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | Velocidade da fala. 0 = normal, 100 = 2.0x, -50 = 0.5x. (padrão: 0) | INT | Sim | -50 a 100 |
| `loudness_rate` | Volume. 0 = normal, 100 = 2.0x, -50 = 0.5x. (padrão: 0) | INT | Sim | -50 a 100 |
| `pitch_rate` | Deslocamento de tom em semitons (-12 a 12). (padrão: 0) | INT | Sim | -12 a 12 |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 42) | INT | Sim | 0 a 2147483647 |
| `model` | Versão do modelo. `seed-audio-1.0-multilingual` suporta 20 idiomas e controle de tempo por frase via carimbos de tempo `[5.5s:8.0s]`. `seed-audio-1.0` suporta apenas inglês e chinês, sem controle de tempo. (padrão: "seed-audio-1.0-multilingual") | COMBO | Não | `"seed-audio-1.0-multilingual"`<br>`"seed-audio-1.0"` |

### Restrições dos Parâmetros

- **Dependências do modo de referência**: O parâmetro `reference_mode` determina quais outras entradas são necessárias:
  - **"apenas texto"**: Nenhuma entrada adicional necessária. O prompt não deve conter tags @AudioN.
Os clipes de referência devem ser conectados em ordem, sem lacunas. Cada clipe é limitado a no máximo 30 segundos. Se tags @AudioN forem usadas no prompt, o número de tag mais alto não deve exceder o número de clipes de referência conectados.
  - **"referência de imagem"**: Requer que `reference_image` esteja conectado. O prompt não deve conter tags @AudioN.
  - **"voz predefinida"**: Requer que `preset_voice` seja selecionado. O prompt não deve conter tags @AudioN (o prompt inteiro é lido na voz selecionada).

- **Ordenação da referência de áudio**: Ao usar o modo "referência de áudio", as entradas de áudio de referência devem ser conectadas sequencialmente, começando por `reference_audio_1`, sem lacunas. Por exemplo, você pode conectar _1 e _2, mas não _1 e _3 sem _2.

- **Máximo de tags de áudio**: No modo "referência de áudio", o prompt pode referenciar até 3 clipes de áudio (@Audio1, @Audio2, @Audio3), e a tag @AudioN mais alta no prompt não pode exceder o número de entradas de áudio de referência conectadas.

- **Diferenças de modelo**: O modelo `seed-audio-1.0-multilingual` suporta 20 idiomas (inglês, chinês, japonês, coreano, espanhol mexicano e castelhano, indonésio, alemão, português brasileiro, francês, tailandês, vietnamita, malaio, filipino, italiano, russo, holandês, polonês, turco, sueco) além do controle de tempo por frase usando carimbos de tempo no formato `[5.5s:8.0s]`. O modelo `seed-audio-1.0` suporta apenas inglês e chinês, sem controle de tempo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `AUDIO` | A saída de áudio gerada pelo ByteDance Seed Audio 1.0, contendo fala, música, efeitos sonoros ou diálogo com múltiplos falantes conforme descrito no prompt. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cefd5fca496b02c35022d25be3d99d3911c1304b6e3a751751b58841d5895ef7`

# ByteDance Seed Audio 1.0

Gere fala, música, efeitos sonoros e diálogo com vários falantes a partir de um único prompt com o ByteDance Seed Audio 1.0. Descreva a(s) voz(es), emoção, ambiência, música de fundo e efeitos sonoros no prompt, e inclua as falas a serem ditas. Opcionalmente, escolha uma voz predefinida integrada, clone vozes a partir de até 3 clipes de referência (marcados como @Audio1-3 no prompt) ou derive uma voz a partir de uma imagem de personagem. Até 2 minutos de áudio por execução. O modelo multilíngue oferece suporte a 20 idiomas e controle de temporização baseado em timestamps.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `text_prompt` | Descreva a(s) voz(es), emoção, ritmo, ambiência, música de fundo e efeitos sonoros, e inclua as falas a serem ditas (nomeie personagens no próprio texto para diálogo). No modo "audio reference", refira-se aos clipes conectados por ordem como @Audio1, @Audio2, @Audio3. Com o modelo multilíngue, uma fala entre aspas pode começar com um intervalo de timestamp que controla quando e por quanto tempo ela é dita, por exemplo, `[5.5s:8.0s] Wait for me!`. Escreva o prompt no mesmo idioma das falas a serem ditas. Mínimo de 1 caractere, máximo de 3000 caracteres. | STRING | Sim | 1 a 3000 caracteres |
| `reference_mode` | Como condicionar a voz: "text only" (descreva tudo no prompt), "audio reference" (clone até 3 vozes, marcadas como @Audio1-3), "image reference" (derive uma voz de uma imagem de personagem) ou "preset voice" (escolha uma voz nomeada integrada que lê o prompt). | COMBO | Sim | `"text only"`<br>`"audio reference"`<br>`"image reference"`<br>`"preset voice"` |
| `reference_audio_1` | Clipe de referência para clonagem de voz, marcado como @Audio1 no prompt. Até 30s. Disponível apenas quando `reference_mode` for "audio reference". | AUDIO | Não | Até 30 segundos |
| `reference_audio_2` | Clipe de referência marcado como @Audio2 no prompt. Até 30s. Disponível apenas quando `reference_mode` for "audio reference". | AUDIO | Não | Até 30 segundos |
| `reference_audio_3` | Clipe de referência marcado como @Audio3 no prompt. Até 30s. Disponível apenas quando `reference_mode` for "audio reference". | AUDIO | Não | Até 30 segundos |
| `reference_image` | Uma única imagem de personagem; o modelo deriva uma voz a partir dela. Não pode ser combinado com áudio de referência. Disponível apenas quando `reference_mode` for "image reference". | IMAGE | Não | - |
| `preset_voice` | Uma voz integrada do TTS 2.0 que lê o prompt. Nenhum clipe de referência é necessário, e tags @AudioN não são usadas neste modo. Obrigatório quando `reference_mode` for "preset voice". | COMBO | Não | Múltiplas opções de voz predefinida integradas (primeira opção selecionada por padrão) |
| `sample_rate` | Taxa de amostragem de saída em Hz. (padrão: "24000") | COMBO | Sim | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | Velocidade da fala. 0 = normal, 100 = 2.0x, -50 = 0.5x. (padrão: 0) | INT | Sim | -50 a 100 |
| `loudness_rate` | Volume. 0 = normal, 100 = 2.0x, -50 = 0.5x. (padrão: 0) | INT | Sim | -50 a 100 |
| `pitch_rate` | Deslocamento de tom em semitons (-12 a 12). (padrão: 0) | INT | Sim | -12 a 12 |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. (padrão: 42) | INT | Sim | 0 a 2147483647 |
| `model` | Versão do modelo. `seed-audio-1.0-multilingual` oferece suporte a 20 idiomas e controle de temporização por frase via timestamps `[5.5s:8.0s]`. `seed-audio-1.0` oferece suporte apenas a inglês e chinês, sem controle de temporização. (padrão: "seed-audio-1.0-multilingual") | COMBO | Não | `"seed-audio-1.0-multilingual"`<br>`"seed-audio-1.0"` |

### Restrições dos parâmetros

- **Dependências do modo de referência**: O parâmetro `reference_mode` determina quais outras entradas são necessárias:
  - **"text only"**: Nenhuma entrada adicional necessária. O prompt não deve conter tags @AudioN.
  - **"audio reference"**: Requer que pelo menos um entre `reference_audio_1`, `reference_audio_2` ou `reference_audio_3` esteja conectado. Os clipes de referência devem ser conectados em ordem, sem lacunas. Cada clipe é limitado a duração máxima de 30 segundos. Se tags @AudioN forem usadas no prompt, o maior número de tag não deve exceder o número de clipes de referência conectados.
  - **"image reference"**: Requer que `reference_image` esteja conectado. Tags @AudioN não são usadas; o prompt deve conter apenas o texto a ser sintetizado.
  - **"preset voice"**: Requer que uma voz predefinida seja selecionada. Todo o prompt é lido na voz selecionada; tags @AudioN não são usadas como referências, e tags como @Audio2 ou superiores são rejeitadas.

- **Ordenação de referências de áudio**: No modo "audio reference", as entradas de áudio de referência devem ser conectadas sequencialmente começando por `reference_audio_1`, sem lacunas. Por exemplo, você pode conectar `reference_audio_1` e `reference_audio_2`, mas não `reference_audio_1` e `reference_audio_3` sem `reference_audio_2`.

- **Máximo de tags de áudio**: No modo "audio reference", até 3 clipes de referência podem ser conectados (@Audio1, @Audio2, @Audio3), e a maior tag @AudioN no prompt não pode exceder o número de entradas de áudio de referência conectadas.

- **Diferenças entre modelos**: O modelo `seed-audio-1.0-multilingual` oferece suporte a 20 idiomas (inglês, chinês, japonês, coreano, espanhol mexicano e castelhano, indonésio, alemão, português brasileiro, francês, tailandês, vietnamita, malaio, filipino, italiano, russo, holandês, polonês, turco, sueco) além de controle de temporização por frase usando timestamps no formato `[5.5s:8.0s]`. O modelo `seed-audio-1.0` oferece suporte apenas a inglês e chinês, sem controle de temporização.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `AUDIO` | A saída de áudio gerada pelo ByteDance Seed Audio 1.0, contendo fala, música, efeitos sonoros ou diálogo com vários falantes conforme descrito no prompt. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e86e4edde424b4427d864350a9d3b082e271fbd2b1e335175637a9cc3ad51163`

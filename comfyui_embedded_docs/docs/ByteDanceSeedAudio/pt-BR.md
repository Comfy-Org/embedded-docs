# ByteDanceSeedAudio

Gere fala, música, efeitos sonoros e diálogo com múltiplos falantes a partir de um único prompt com o ByteDance Seed Audio 1.0. Descreva a(s) voz(es), emoção, ambiente, música de fundo e efeitos sonoros no prompt, e inclua as falas a serem ditas. Opcionalmente, escolha uma voz predefinida integrada, clone vozes de até 3 clipes de referência (marcados como @Audio1-3 no prompt) ou derive uma voz a partir de uma imagem de personagem. Até 2 minutos de áudio por execução.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `text_prompt` | Descreva a(s) voz(es), emoção, ritmo, ambiente, música de fundo e efeitos sonoros, e inclua as falas a serem ditas (nomeie os personagens inline para diálogo). No modo 'referência de áudio', refira-se aos clipes conectados por ordem como @Audio1, @Audio2, @Audio3. Máximo de 3000 caracteres. | STRING | Sim | 1 a 3000 caracteres |
| `reference_mode` | Como condicionar a voz: 'apenas texto' (descreva tudo no prompt), 'referência de áudio' (clone até 3 vozes, marcadas como @Audio1-3), 'referência de imagem' (derive uma voz de uma imagem de personagem) ou 'voz predefinida' (escolha uma voz nomeada integrada que lê o prompt). | COMBO | Sim | `"apenas texto"`<br>`"referência de áudio"`<br>`"referência de imagem"`<br>`"voz predefinida"` |
| `reference_audio_1` | Clipe de referência para clonagem de voz, marcado como @Audio1 no prompt. Até 30s. Disponível apenas quando `reference_mode` for "referência de áudio". | AUDIO | Não | Até 30 segundos |
| `reference_audio_2` | Clipe de referência marcado como @Audio2 no prompt. Até 30s. Disponível apenas quando `reference_mode` for "referência de áudio". | AUDIO | Não | Até 30 segundos |
| `reference_audio_3` | Clipe de referência marcado como @Audio3 no prompt. Até 30s. Disponível apenas quando `reference_mode` for "referência de áudio". | AUDIO | Não | Até 30 segundos |
| `reference_image` | Uma imagem de um único personagem; o modelo deriva uma voz a partir dela. Não pode ser combinada com áudio de referência. Disponível apenas quando `reference_mode` for "referência de imagem". | IMAGE | Não | - |
| `preset_voice` | Uma voz TTS 2.0 integrada que lê o prompt. Nenhum clipe de referência é necessário, e as tags @AudioN não são usadas neste modo. Disponível apenas quando `reference_mode` for "voz predefinida". | COMBO | Não | Múltiplas opções disponíveis (veja descrição) |
| `sample_rate` | Taxa de amostragem de saída em Hz. (padrão: "24000") | COMBO | Sim | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | Velocidade da fala. 0 = normal, 100 = 2.0x, -50 = 0.5x. (padrão: 0) | INT | Sim | -50 a 100 |
| `loudness_rate` | Volume. 0 = normal, 100 = 2.0x, -50 = 0.5x. (padrão: 0) | INT | Sim | -50 a 100 |
| `pitch_rate` | Deslocamento de tom em semitons (-12 a 12). (padrão: 0) | INT | Sim | -12 a 12 |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 42) | INT | Sim | 0 a 2147483647 |

### Restrições dos Parâmetros

- **Dependências do modo de referência**: O parâmetro `reference_mode` determina quais outras entradas são necessárias:
  - **"apenas texto"**: Nenhuma entrada adicional necessária. O prompt não deve conter tags @AudioN.
  - **"referência de áudio"**: Requer que pelo menos um dos `reference_audio_1`, `reference_audio_2` ou `reference_audio_3` esteja conectado. Os clipes de referência devem ser conectados em ordem, sem lacunas (por exemplo, _1, depois _2, depois _3). Cada clipe tem duração máxima limitada a 30 segundos. O prompt deve referenciar os clipes conectados usando as tags @Audio1, @Audio2, @Audio3.
  - **"referência de imagem"**: Requer que `reference_image` esteja conectado. O prompt não deve conter tags @AudioN.
  - **"voz predefinida"**: Requer que `preset_voice` seja selecionado. O prompt não deve conter tags @AudioN (o prompt inteiro é lido na voz selecionada).

- **Ordenação da referência de áudio**: Ao usar o modo "referência de áudio", as entradas de áudio de referência devem ser conectadas sequencialmente, começando por `reference_audio_1`, sem lacunas. Por exemplo, você pode conectar _1 e _2, mas não _1 e _3 sem _2.

- **Máximo de tags de áudio**: O prompt pode referenciar até 3 clipes de áudio (@Audio1, @Audio2, @Audio3) quando estiver no modo "referência de áudio". A tag com o número mais alto não deve exceder o número de entradas de áudio de referência conectadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `AUDIO` | A saída de áudio gerada pelo ByteDance Seed Audio 1.0, contendo fala, música, efeitos sonoros ou diálogo com múltiplos falantes conforme descrito no prompt. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cefd5fca496b02c35022d25be3d99d3911c1304b6e3a751751b58841d5895ef7`

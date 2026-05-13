> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/pt-BR.md)

O nó ElevenLabs Speech to Text transcreve arquivos de áudio em texto. Ele utiliza a API da ElevenLabs para converter palavras faladas em uma transcrição escrita, oferecendo suporte a recursos como detecção automática de idioma, identificação de diferentes falantes e marcação de sons não falados, como música ou risadas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sim | - | Áudio a ser transcrito. |
| `model` | COMBO | Sim | `"scribe_v2"` | Modelo a ser usado para transcrição. Selecionar este modelo revela parâmetros adicionais. |
| `tag_audio_events` | BOOLEAN | Não | - | Anotar sons como (risadas), (música), etc. na transcrição. Este parâmetro é revelado quando o modelo `"scribe_v2"` é selecionado. (padrão: False) |
| `diarize` | BOOLEAN | Não | - | Anotar qual falante está falando. Este parâmetro é revelado quando o modelo `"scribe_v2"` é selecionado. (padrão: False) |
| `diarization_threshold` | FLOAT | Não | 0,1 - 0,4 | Sensibilidade de separação de falantes. Valores menores são mais sensíveis a mudanças de falante. Este parâmetro é revelado quando o modelo `"scribe_v2"` é selecionado e `diarize` está ativado. (padrão: 0,22) |
| `temperature` | FLOAT | Não | 0,0 - 2,0 | Controle de aleatoriedade. 0,0 usa o padrão do modelo. Valores maiores aumentam a aleatoriedade. Este parâmetro é revelado quando o modelo `"scribe_v2"` é selecionado. (padrão: 0,0) |
| `timestamps_granularity` | COMBO | Não | `"word"`<br>`"character"`<br>`"none"` | Precisão de tempo para palavras da transcrição. Este parâmetro é revelado quando o modelo `"scribe_v2"` é selecionado. (padrão: "word") |
| `language_code` | STRING | Não | - | Código de idioma ISO-639-1 ou ISO-639-3 (ex.: 'en', 'es', 'fra'). Deixe vazio para detecção automática. (padrão: "") |
| `num_speakers` | INT | Não | 0 - 32 | Número máximo de falantes a prever. Defina como 0 para detecção automática. (padrão: 0) |
| `seed` | INT | Não | 0 - 2147483647 | Semente para reprodutibilidade (determinismo não garantido). (padrão: 1) |

**Nota:** O parâmetro `num_speakers` não pode ser definido com um valor maior que 0 quando a opção `diarize` está ativada. Você deve desativar `diarize` ou definir `num_speakers` como 0.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `text` | STRING | O texto transcrito do áudio. |
| `language_code` | STRING | O código do idioma detectado no áudio. |
| `words_json` | STRING | Uma string formatada em JSON contendo informações detalhadas em nível de palavra, incluindo timestamps e rótulos de falante, se ativados. |

---
**Source fingerprint (SHA-256):** `aca2ac04d7280ef2b604f7c8d29ad7fea1e7abcfc38beabb64ba6b268a8cade1`

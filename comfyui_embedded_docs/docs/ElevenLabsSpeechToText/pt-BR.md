# ElevenLabs Fala para Texto

O nó ElevenLabs Speech to Text transcreve arquivos de áudio em texto. Ele utiliza a API da ElevenLabs para converter palavras faladas em uma transcrição escrita, oferecendo suporte a recursos como detecção automática de idioma, identificação de diferentes falantes e marcação de sons não falados, como música ou risadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `áudio` | Áudio a ser transcrito. | AUDIO | Sim | - |
| `modelo` | Modelo a ser usado para transcrição. Selecionar este modelo revela parâmetros adicionais. | COMBO | Sim | `"scribe_v2"` |
| `tag_audio_events` | Anotar sons como (risadas), (música), etc. na transcrição. Este parâmetro é revelado quando o modelo `"scribe_v2"` é selecionado. (padrão: False) | BOOLEAN | Não | - |
| `diarize` | Anotar qual falante está falando. Este parâmetro é revelado quando o modelo `"scribe_v2"` é selecionado. (padrão: False) | BOOLEAN | Não | - |
| `diarization_threshold` | Sensibilidade de separação de falantes. Valores menores são mais sensíveis a mudanças de falante. Este parâmetro é revelado quando o modelo `"scribe_v2"` é selecionado e `diarize` está ativado. (padrão: 0,22) | FLOAT | Não | 0,1 - 0,4 |
| `temperature` | Controle de aleatoriedade. 0,0 usa o padrão do modelo. Valores maiores aumentam a aleatoriedade. Este parâmetro é revelado quando o modelo `"scribe_v2"` é selecionado. (padrão: 0,0) | FLOAT | Não | 0,0 - 2,0 |
| `timestamps_granularity` | Precisão de tempo para palavras da transcrição. Este parâmetro é revelado quando o modelo `"scribe_v2"` é selecionado. (padrão: "word") | COMBO | Não | `"word"`<br>`"character"`<br>`"none"` |
| `código_idioma` | Código de idioma ISO-639-1 ou ISO-639-3 (ex.: 'en', 'es', 'fra'). Deixe vazio para detecção automática. (padrão: "") | STRING | Não | - |
| `num_locs` | Número máximo de falantes a prever. Defina como 0 para detecção automática. (padrão: 0) | INT | Não | 0 - 32 |
| `semente` | Semente para reprodutibilidade (determinismo não garantido). (padrão: 1) | INT | Não | 0 - 2147483647 |

**Nota:** O parâmetro `num_speakers` não pode ser definido com um valor maior que 0 quando a opção `diarize` está ativada. Você deve desativar `diarize` ou definir `num_speakers` como 0.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `text` | O texto transcrito do áudio. | STRING |
| `código_idioma` | O código do idioma detectado no áudio. | STRING |
| `words_json` | Uma string formatada em JSON contendo informações detalhadas em nível de palavra, incluindo timestamps e rótulos de falante, se ativados. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/pt-BR.md)

---
**Source fingerprint (SHA-256):** `aca2ac04d7280ef2b604f7c8d29ad7fea1e7abcfc38beabb64ba6b268a8cade1`

# ElevenLabs Fala para Texto

O nó ElevenLabs Speech to Text transcreve áudio em texto usando a API de fala para texto da ElevenLabs. Ele oferece suporte à detecção automática de idioma, identifica qual locutor está falando e marca sons não relacionados à fala, como (risos) ou (música), na transcrição.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | Modelo a ser usado para transcrição. Selecionar um modelo revela seus parâmetros específicos. | DYNAMIC_COMBO | Sim | `"scribe_v2"` |
| `áudio` | Áudio a ser transcrito. | AUDIO | Sim | - |
| `código_idioma` | Código de idioma ISO-639-1 ou ISO-639-3 (ex.: 'en', 'es', 'fra'). Deixe vazio para detecção automática. (padrão: "") | STRING | Não | - |
| `num_locs` | Número máximo de locutores a prever. Defina como 0 para detecção automática. (padrão: 0) | INT | Não | 0 - 32 |
| `semente` | Semente para reprodutibilidade (determinismo não garantido). (padrão: 1) | INT | Não | 0 - 2147483647 |

### Entradas do Scribe v2

Estes parâmetros aparecem quando o modelo `"scribe_v2"` é selecionado.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `tag_audio_events` | Anota sons como (risos), (música), etc. na transcrição. (padrão: False) | BOOLEAN | Não | - |
| `diarize` | Anota qual locutor está falando. (padrão: False) | BOOLEAN | Não | - |
| `diarization_threshold` | Sensibilidade da separação de locutores. Valores mais baixos são mais sensíveis a mudanças de locutor. Usado somente quando `diarize` está ativado. (padrão: 0.22) | FLOAT | Não | 0.1 - 0.4 |
| `temperature` | Controle de aleatoriedade. 0.0 usa o padrão do modelo. Valores mais altos aumentam a aleatoriedade. (padrão: 0.0) | FLOAT | Não | 0.0 - 2.0 |
| `timestamps_granularity` | Precisão temporal para as palavras da transcrição. (padrão: "word") | COMBO | Não | `"word"`<br>`"character"`<br>`"none"` |

**Observação:** `num_locs` não pode ser definido com valor maior que 0 quando `diarize` está ativado. Desative `diarize` ou defina `num_locs` como 0; caso contrário, um erro será gerado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `text` | O texto transcrito do áudio. | STRING |
| `language_code` | O código de idioma detectado no áudio. | STRING |
| `words_json` | Uma string formatada em JSON contendo informações detalhadas em nível de palavra, incluindo timestamps e rótulos de locutor, se ativados. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7eb5d72615aa8a9e4a8014e45b39cf83dc8d8432d7ce0dccba20489be80a5830`

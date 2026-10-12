# ElevenLabsSpeechToText

Il nodo ElevenLabs Speech to Text trascrive l'audio in testo utilizzando l'API ElevenLabs. Supporta il rilevamento automatico della lingua, la diarizzazione dei parlanti (identificazione dei diversi parlanti) e l'etichettatura degli eventi audio (annotazione di suoni come risate o musica nella trascrizione).

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello da utilizzare per la trascrizione. Selezionando questo modello vengono visualizzati parametri aggiuntivi. | DYNAMIC_COMBO | Sì | `"scribe_v2"` |
| `audio` | Audio da trascrivere. | AUDIO | Sì | - |
| `language_code` | Codice lingua ISO-639-1 o ISO-639-3 (ad es. 'en', 'es', 'fra'). Lasciare vuoto per il rilevamento automatico. (predefinito: "") | STRING | No | - |
| `num_speakers` | Numero massimo di parlanti da prevedere. Impostare su 0 per il rilevamento automatico. (predefinito: 0) | INT | No | 0 - 32 |
| `seed` | Seme per la riproducibilità (determinismo non garantito). (predefinito: 1) | INT | No | 0 - 2147483647 |

### Input di Scribe v2

Questi parametri vengono mostrati quando è selezionato il modello `"scribe_v2"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `tag_audio_events` | Annota suoni come (laughter), (music), ecc. nella trascrizione. (predefinito: False) | BOOLEAN | No | - |
| `diarize` | Annota quale parlante sta parlando. (predefinito: False) | BOOLEAN | No | - |
| `diarization_threshold` | Sensibilità di separazione dei parlanti. Valori più bassi sono più sensibili ai cambi di parlante. Utilizzato solo quando `diarize` è abilitato. (predefinito: 0.22) | FLOAT | No | 0.1 - 0.4 |
| `temperature` | Controllo della casualità. 0.0 utilizza il valore predefinito del modello. Valori più alti aumentano la casualità. (predefinito: 0.0) | FLOAT | No | 0.0 - 2.0 |
| `timestamps_granularity` | Precisione temporale per le parole della trascrizione. (predefinito: "word") | COMBO | No | `"word"`<br>`"character"`<br>`"none"` |

**Nota:** `num_speakers` non può essere impostato su un valore maggiore di 0 quando `diarize` è abilitato. È necessario disabilitare `diarize` oppure impostare `num_speakers` su 0.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `text` | Il testo trascritto dall'audio. | STRING |
| `language_code` | Il codice lingua rilevato per l'audio. | STRING |
| `words_json` | Una stringa in formato JSON contenente informazioni dettagliate a livello di parola, compresi timestamp ed etichette dei parlanti, se abilitati. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/it.md)

---
**Source fingerprint (SHA-256):** `7eb5d72615aa8a9e4a8014e45b39cf83dc8d8432d7ce0dccba20489be80a5830`

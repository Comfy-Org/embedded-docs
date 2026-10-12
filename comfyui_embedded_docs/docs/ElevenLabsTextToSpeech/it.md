# ElevenLabsTextToSpeech

Il nodo Text to Speech di ElevenLabs converte il testo scritto in audio parlato utilizzando l'API ElevenLabs. Consente di selezionare una voce specifica e di regolare diverse caratteristiche del parlato, come stabilità, velocità e stile, per generare un output audio personalizzato. Il testo deve contenere almeno un carattere.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare per la sintesi vocale. Selezionando un modello vengono mostrati i suoi parametri specifici. | DYNAMIC_COMBO | No | `"eleven_v4"`<br>`"eleven_v4_turbo"`<br>`"eleven_multilingual_v2"`<br>`"eleven_v3"` |
| `voice` | Voce da utilizzare per la sintesi vocale. Connettila da Voice Selector o Instant Voice Clone. | CUSTOM | Sì | N/A |
| `text` | Il testo da convertire in parlato. Deve contenere almeno un carattere. | STRING | Sì | N/A |
| `stability` | Stabilità della voce. Valori più bassi offrono una gamma emotiva più ampia, valori più alti producono una voce più coerente ma potenzialmente monotona (predefinito: 0.5). | FLOAT | No | 0.0 - 1.0 |
| `apply_text_normalization` | Modalità di normalizzazione del testo. 'auto' lascia decidere al sistema, 'on' applica sempre la normalizzazione, 'off' la salta. | COMBO | No | `"auto"`<br>`"on"`<br>`"off"` |
| `language_code` | Codice lingua ISO 639-1 (ad esempio, 'en', 'es', 'ja'). Lasciare vuoto per il rilevamento automatico (predefinito: ""). | STRING | No | N/A |
| `seed` | Seme per la riproducibilità (determinismo non garantito) (predefinito: 1). | INT | No | 0 - 2147483647 |
| `output_format` | Formato di output audio. | COMBO | No | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Input di eleven_multilingual_v2

Questi parametri diventano disponibili quando `model` è impostato su `"eleven_multilingual_v2"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `speed` | Velocità del parlato. 1.0 è normale, <1.0 più lento, >1.0 più veloce (predefinito: 1.0). | FLOAT | No | 0.7 - 1.2 |
| `similarity_boost` | Incremento di somiglianza. Valori più alti rendono la voce più simile all'originale (predefinito: 0.75). | FLOAT | No | 0.0 - 1.0 |
| `use_speaker_boost` | Aumenta la somiglianza con la voce del parlante originale (predefinito: False). | BOOLEAN | No | True / False |
| `style` | Esagerazione dello stile. Valori più alti aumentano l'espressione stilistica ma possono ridurre la stabilità (predefinito: 0.0). | FLOAT | No | 0.0 - 0.2 |

### Input di eleven_v3

Questi parametri diventano disponibili quando `model` è impostato su `"eleven_v3"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `speed` | Velocità del parlato. 1.0 è normale, <1.0 più lento, >1.0 più veloce (predefinito: 1.0). | FLOAT | No | 0.7 - 1.3 |
| `similarity_boost` | Incremento di somiglianza. Valori più alti rendono la voce più simile all'originale (predefinito: 0.75). | FLOAT | No | 0.0 - 1.0 |

### Input di eleven_v4 e eleven_v4_turbo

Questi parametri diventano disponibili quando `model` è impostato su `"eleven_v4"` o `"eleven_v4_turbo"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `similarity_boost` | Incremento di somiglianza. Valori più alti rendono la voce più simile all'originale (predefinito: 0.75). | FLOAT | No | 0.0 - 1.0 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `audio` | L'audio generato dalla conversione da testo a voce. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/it.md)

---
**Source fingerprint (SHA-256):** `2f8aadca9f4fee9614ce4488aa206119ecf714518b7c0c340b1bfa766f59672e`

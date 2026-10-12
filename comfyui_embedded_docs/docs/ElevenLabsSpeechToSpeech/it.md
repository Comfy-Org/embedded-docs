# ElevenLabsSpeechToSpeech

Il nodo ElevenLabs Speech to Speech trasforma un file audio di input da una voce a un'altra. Utilizza l'API ElevenLabs per convertire il parlato preservando il contenuto originale e il tono emotivo dell'audio.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare per la trasformazione speech-to-speech. Il modello selezionato determina le impostazioni vocali disponibili elencate di seguito. | DYNAMIC_COMBO | Sì | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` |
| `voice` | Voce di destinazione per la trasformazione. Collegare da Voice Selector o Instant Voice Clone. | CUSTOM | Sì | - |
| `audio` | Audio sorgente da trasformare. | AUDIO | Sì | - |
| `stability` | Stabilità della voce. Valori più bassi offrono una gamma emotiva più ampia; valori più alti producono un parlato più coerente ma potenzialmente monotono (predefinito: 0.5). | FLOAT | Sì | 0.0 - 1.0 |
| `output_format` | Formato di output audio. | COMBO | Sì | `"mp3_44100_192"`<br>`"opus_48000_192"` |
| `seed` | Seed per la riproducibilità (predefinito: 0). | INT | Sì | 0 - 4294967295 |
| `remove_background_noise` | Rimuove il rumore di fondo dall'audio di input usando l'isolamento audio (predefinito: False). | BOOLEAN | Sì | - |

### Input di eleven_multilingual_sts_v2 e eleven_english_sts_v2

Entrambi i modelli forniscono lo stesso insieme di impostazioni vocali riportato di seguito.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `speed` | Velocità del parlato. 1.0 è normale, <1.0 più lento, >1.0 più veloce (predefinito: 1.0). | FLOAT | Sì | 0.7 - 1.3 |
| `similarity_boost` | Aumento della somiglianza. Valori più alti rendono la voce più simile all'originale (predefinito: 0.75). | FLOAT | Sì | 0.0 - 1.0 |
| `use_speaker_boost` | Aumenta la somiglianza con la voce originale del parlante (predefinito: False). | BOOLEAN | Sì | - |
| `style` | Esagerazione dello stile. Valori più alti aumentano l'espressione stilistica ma possono ridurre la stabilità (predefinito: 0.0). | FLOAT | Sì | 0.0 - 0.2 |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `audio` | Il file audio trasformato nel formato di output specificato. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/it.md)

---
**Source fingerprint (SHA-256):** `a3cd602181d134b9ab517bfac092ea30b62ef5a9942a905c0c3e6959b34370ca`

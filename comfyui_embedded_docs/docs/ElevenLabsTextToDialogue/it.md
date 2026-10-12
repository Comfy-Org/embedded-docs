# ElevenLabs Testo in Dialogo

Il nodo ElevenLabs Text to Dialogue genera un dialogo audio multi-voce a partire da un testo. Consente di creare una conversazione specificando diverse righe di testo e voci distinte per ciascun partecipante. Il nodo invia la richiesta di dialogo all'API di ElevenLabs e restituisce l'audio generato.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `stability` | Stabilità della voce. Valori più bassi offrono una gamma emotiva più ampia, valori più alti producono un parlato più coerente ma potenzialmente monotono. (predefinito: 0.5) | FLOAT | Sì | 0.0 - 1.0 |
| `apply_text_normalization` | Modalità di normalizzazione del testo. 'auto' lascia decidere al sistema, 'on' applica sempre la normalizzazione, 'off' la salta. | COMBO | Sì | `"auto"`<br>`"on"`<br>`"off"` |
| `model` | Modello da utilizzare per la generazione del dialogo (predefinito: `"eleven_v4"`). | COMBO | Sì | `"eleven_v3"`<br>`"eleven_v4"`<br>`"eleven_v4_turbo"` |
| `inputs` | Numero di voci di dialogo. Selezionando un numero si creano altrettante coppie di input testo e voce. | DYNAMIC_COMBO | Sì | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `language_code` | Codice lingua ISO 639-1 (ad es. 'en', 'es', 'ja'). Lasciare vuoto per il rilevamento automatico. (predefinito: vuoto) | STRING | Sì | - |
| `seed` | Seed per la riproducibilità. (predefinito: 1) | INT | Sì | 0 - 4294967295 |
| `output_format` | Formato di output audio. | COMBO | Sì | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Input delle voci di dialogo

Condivisi da tutte le opzioni di `inputs`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `text1` ... `text10` | Contenuto testuale per la corrispondente voce di dialogo. Il nodo crea un campo `text` per ogni voce di dialogo selezionata. Ogni valore di testo deve contenere almeno un carattere. | STRING | Sì | - |
| `voice1` ... `voice10` | Voce per la corrispondente voce di dialogo. Collegare da un nodo Voice Selector o Instant Voice Clone. Il nodo crea un campo `voice` per ogni voce di dialogo selezionata. | ELEVENLABS_VOICE | Sì | - |

**Nota:** Il selettore `inputs` può creare fino a 10 voci di dialogo. Ogni voce richiede sia un campo `text` sia un campo `voice`. Il valore di `text` non può essere vuoto. L'input `voice` richiede un ID voce fornito da un nodo voce ElevenLabs compatibile.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `audio` | L'audio del dialogo multi-voce generato nel formato di output selezionato. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/it.md)

---
**Source fingerprint (SHA-256):** `bff737be0c828990d7286de4372e995295a4716febd388d7cc02c2a9987a6c80`

# StabilityTextToAudio

Genera musica ed effetti sonori di alta qualità a partire da descrizioni testuali. Questo nodo utilizza la tecnologia di generazione audio di Stability AI per creare contenuti audio basati sui tuoi prompt testuali.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello di generazione audio da utilizzare (predefinito: "stable-audio-2.5") | COMBO | Sì | `"stable-audio-2.5"` |
| `prompt` | La descrizione testuale utilizzata per generare contenuti audio (predefinito: stringa vuota) | STRING | Sì | - |
| `duration` | Controlla la durata in secondi dell'audio generato (predefinito: 190) | INT | No | 1-190 |
| `seed` | Il seed casuale utilizzato per la generazione (predefinito: 0) | INT | No | 0-4294967294 |
| `steps` | Controlla il numero di passaggi di campionamento (predefinito: 8) | INT | No | 4-8 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `audio` | Il file audio generato in base al prompt testuale | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityTextToAudio/it.md)

---
**Source fingerprint (SHA-256):** `8dfe0eafb6157bc458c2ba3053a98e2bb5dfe896921cf90a70a88c695f8c5edc`

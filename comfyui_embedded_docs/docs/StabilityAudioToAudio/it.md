# StabilityAudioToAudio

Trasforma campioni audio esistenti in nuove composizioni di alta qualità utilizzando istruzioni testuali. Questo nodo riceve in ingresso un file audio e lo modifica in base al prompt testuale per creare nuovi contenuti audio.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello AI da utilizzare per la trasformazione audio | COMBO | Sì | "stable-audio-2.5" |
| `prompt` | Istruzioni testuali che descrivono come trasformare l'audio (predefinito: vuoto, lunghezza massima: 10000 caratteri) | STRING | Sì | |
| `audio` | L'audio deve avere una durata compresa tra 6 e 190 secondi | AUDIO | Sì | |
| `duration` | Controlla la durata in secondi dell'audio generato (predefinito: 190) | INT | No | 1-190 |
| `seed` | Il seed casuale utilizzato per la generazione (predefinito: 0) | INT | No | 0-4294967294 |
| `steps` | Controlla il numero di passaggi di campionamento (predefinito: 8) | INT | No | 4-8 |
| `strength` | Controlla quanto il parametro audio influenza l'audio generato (predefinito: 1.0) | FLOAT | No | 0.01-1.0 |

**Nota:** L'audio di input deve avere una durata compresa tra 6 e 190 secondi. Il testo del prompt ha una lunghezza massima di 10.000 caratteri.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `audio` | L'audio trasformato generato in base all'audio di input e al prompt testuale | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioToAudio/it.md)

---
**Source fingerprint (SHA-256):** `3df67797bf2eccf9d7464a1dd00ea5b6c5a9527f7290911c60a9ebff69302241`

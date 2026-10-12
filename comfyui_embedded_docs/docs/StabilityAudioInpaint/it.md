# StabilityAudioInpaint

Trasforma parte di un campione audio esistente utilizzando istruzioni testuali. Questo nodo consente di modificare sezioni specifiche dell'audio fornendo prompt descrittivi, di fatto eseguendo un'operazione di "inpainting" o rigenerando porzioni selezionate mentre il resto dell'audio viene preservato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello AI da utilizzare per l'inpainting audio. | STRING | Sì | `"stable-audio-2.5"` |
| `prompt` | Descrizione testuale che guida la trasformazione dell'audio (predefinito: vuoto). La lunghezza massima è di 10.000 caratteri. | STRING | Sì |  |
| `audio` | File audio di input da trasformare. L'audio deve avere una durata compresa tra 6 e 190 secondi. | AUDIO | Sì |  |
| `duration` | Controlla la durata in secondi dell'audio generato (predefinito: 190). | INT | No | 1 a 190 |
| `seed` | Il seed casuale utilizzato per la generazione (predefinito: 0). | INT | No | 0 a 4294967294 |
| `steps` | Controlla il numero di step di campionamento (predefinito: 8). | INT | No | 4 a 8 |
| `mask_start` | Posizione iniziale in secondi della sezione audio da trasformare (predefinito: 30). | INT | No | 0 a 190 |
| `mask_end` | Posizione finale in secondi della sezione audio da trasformare (predefinito: 190). | INT | No | 0 a 190 |

**Nota:** Il valore di `mask_end` deve essere maggiore del valore di `mask_start`. L'audio di input deve avere una durata compresa tra 6 e 190 secondi.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `audio` | L'output audio trasformato, con la sezione specificata modificata in base al prompt. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/it.md)

---
**Source fingerprint (SHA-256):** `3c180043c538311b1808cddd84b0c0ab22a6fa1d943b7f9ddc9edab0fb3413ad`

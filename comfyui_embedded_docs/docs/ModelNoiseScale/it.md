# ModelNoiseScale

Questo nodo regola la scala di rumore utilizzata durante il campionamento del modello. Crea una copia del modello di input, applica la scala di rumore specificata alla sua configurazione di campionamento e restituisce il modello modificato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui applicare la regolazione della scala di rumore. | MODEL | Sì | - |
| `noise_scale` | Scala di rumore assoluta per l'addestramento. Ad esempio HiDream-O1 base: 8.0, dev: 7.5. (predefinito: 1.0) | FLOAT | Sì | 0.0 a 64.0 (passo: 0.01) |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `MODEL` | Il modello modificato con la nuova scala di rumore applicata. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/it.md)

---
**Source fingerprint (SHA-256):** `75b0b99323fc15ff3cafc23de05a9d6b52d059494fbc229e5fb685d2908dd5d3`

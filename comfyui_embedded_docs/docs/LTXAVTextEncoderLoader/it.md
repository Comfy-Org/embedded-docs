# LTXAVTextEncoderLoader

Questo nodo carica un codificatore di testo specializzato per il modello audio LTXV. Combina un file di codificatore di testo con un file checkpoint per creare un modello CLIP utilizzato per il condizionamento testuale nella generazione audio. Secondo la descrizione del nodo, il codificatore di testo dovrebbe essere un modello Gemma 3 12B o un Gemma 4 corrispondente.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `text_encoder` | Il nome file del modello codificatore di testo LTXV da caricare. Le opzioni disponibili vengono caricate dalla cartella `text_encoders`. | COMBO | Sì | Più opzioni disponibili |
| `ckpt_name` | Il nome file del checkpoint da caricare. Le opzioni disponibili vengono caricate dalla cartella `checkpoints`. | COMBO | Sì | Più opzioni disponibili |
| `device` | Specifica il dispositivo su cui caricare il modello. Usa `"cpu"` per forzare il caricamento sulla CPU. Il comportamento predefinito (`"default"`) usa il posizionamento automatico del dispositivo da parte del sistema (predefinito: `"default"`). Questo è un parametro avanzato. | COMBO | No | `"default"`<br>`"cpu"` |

**Nota:** I parametri `text_encoder` e `ckpt_name` lavorano insieme. Il nodo carica entrambi i file specificati per creare un unico modello CLIP funzionale. I file devono essere compatibili con l'architettura LTXV, e il codificatore di testo dovrebbe essere un modello Gemma 3 12B o un Gemma 4 corrispondente.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `clip` | Il modello CLIP LTXV caricato, pronto per essere usato per codificare i prompt testuali per la generazione audio. | CLIP |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/it.md)

---
**Source fingerprint (SHA-256):** `1f3df2c1791203ba849a87897de14052e0cb8370100dbca19df4cf30169a0a2a`

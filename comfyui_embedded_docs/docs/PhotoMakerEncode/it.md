# PhotoMakerEncode

Il nodo PhotoMakerEncode combina un'immagine di riferimento con un prompt testuale per creare dati di condizionamento per la generazione di immagini. Quando il testo contiene la parola "photomaker", il nodo utilizza il modello PhotoMaker per inserire l'identità visiva dell'immagine di riferimento nel condizionamento in quella posizione del prompt.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `photomaker` | Il modello PhotoMaker usato per elaborare l'immagine di riferimento e generare embedding basati sull'immagine | PHOTOMAKER | Sì | - |
| `image` | L'immagine di riferimento che fornisce le caratteristiche visive per il condizionamento | IMAGE | Sì | - |
| `clip` | Il modello CLIP usato per la tokenizzazione e la codifica del testo | CLIP | Sì | - |
| `text` | Il prompt testuale per la generazione del condizionamento. Supporta testo multilinea e prompt dinamici (predefinito: "photograph of photomaker") | STRING | Sì | Qualsiasi stringa |

**Nota:** Quando il testo contiene "photomaker" come parola autonoma, il nodo rimuove quella parola dal prompt codificato e applica l'identità dell'immagine di riferimento in quella posizione usando il modello PhotoMaker. Se "photomaker" non viene trovato nel testo, il nodo restituisce un condizionamento testuale standard senza influenza dell'immagine.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CONDITIONING` | Dati di condizionamento contenenti gli embedding del testo e dell'immagine che guidano la generazione di immagini, insieme all'output pooled dell'encoder di testo CLIP | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/it.md)

---
**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`

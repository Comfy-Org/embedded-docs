# FluxDisabilitaGuida

Questo nodo disabilita completamente l'embedding di guidance sui modelli Flux e simili a Flux. Riceve in input dati di conditioning e imposta il suo valore di guidance su None, disattivando di fatto il condizionamento basato sulla guidance per il processo di generazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `conditioning` | I dati di conditioning da elaborare e da cui rimuovere la guidance | CONDITIONING | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `conditioning` | I dati di conditioning modificati con la guidance disabilitata | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/it.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`

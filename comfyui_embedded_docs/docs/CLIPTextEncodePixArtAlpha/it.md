# CLIPTextEncodePixArtAlpha

Codifica il testo e imposta il condizionamento della risoluzione per PixArt Alpha. Questo nodo elabora l'input testuale e aggiunge informazioni di larghezza e altezza per creare dati di condizionamento specificamente per i modelli PixArt Alpha. Non si applica ai modelli PixArt Sigma.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `width` | La dimensione di larghezza per il condizionamento della risoluzione (predefinito: 1024) | INT | Sì | 0 a MAX_RESOLUTION |
| `height` | La dimensione di altezza per il condizionamento della risoluzione (predefinito: 1024) | INT | Sì | 0 a MAX_RESOLUTION |
| `text` | Input testuale da codificare. Supporta input multilinea e prompt dinamici. | STRING | Sì | - |
| `clip` | Modello CLIP usato per la tokenizzazione e la codifica | CLIP | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `CONDITIONING` | Dati di condizionamento codificati con token di testo e informazioni sulla risoluzione | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/it.md)

---
**Source fingerprint (SHA-256):** `d25a4117d39e3528cd0f64bc34462cd7b4076c67cb4e454c77fcc66490f89be6`

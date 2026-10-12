# Recraft Remove Background

Questo nodo rimuove lo sfondo dalle immagini utilizzando il servizio API Recraft. Elabora ogni immagine del batch di input singolarmente e restituisce sia le immagini elaborate con sfondi trasparenti sia le maschere alpha corrispondenti che indicano le aree di sfondo rimosse.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine (o le immagini) di input da elaborare per la rimozione dello sfondo. Ogni immagine del batch viene elaborata singolarmente. | IMAGE | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | Immagini elaborate con sfondi trasparenti (formato RGBA) | IMAGE |
| `mask` | Maschere del canale alpha che indicano le aree di sfondo rimosse, in formato B,H,W | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/it.md)

---
**Source fingerprint (SHA-256):** `702dfdf2751d5ca33f23e10c0968496887514a21da7a0c42e3636a0ed4e82311`

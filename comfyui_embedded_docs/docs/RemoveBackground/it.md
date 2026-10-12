# Rimuovi Sfondo

## Panoramica

Il nodo Remove Background genera una maschera di primo piano che separa il soggetto principale dallo sfondo di un'immagine di input. Utilizza un modello di rimozione dello sfondo per analizzare l'immagine e produrre una maschera che evidenzia gli elementi in primo piano.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `bg_removal_model` | Modello di rimozione dello sfondo utilizzato per generare la maschera | BACKGROUND_REMOVAL_MODEL | Sì | N/A |
| `image` | Immagine di input da cui rimuovere lo sfondo | IMAGE | Sì | N/A |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `mask` | Maschera di primo piano generata | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/it.md)

---
**Source fingerprint (SHA-256):** `75b415acedaeaa1a694aeba2e4b0367524c6878e3e4a1f48b2a62898c68109f9`

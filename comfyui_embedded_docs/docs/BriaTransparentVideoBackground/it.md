# Bria Rimuovi Sfondo Video (Trasparente)

Questo nodo rimuove lo sfondo da un video utilizzando il servizio AI di Bria e restituisce i fotogrammi scontornati insieme a una maschera alpha. Collega entrambi gli output a un nodo di compositing, oppure passali a un nodo Save WEBM per salvare un video trasparente.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Il video di input da elaborare. Il video deve durare 60 secondi o meno. | VIDEO | Sì | - |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed (predefinito: 0) | INT | Sì | 0 a 2147483647 |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `images` | I fotogrammi del video con lo sfondo rimosso, come immagini RGB nell'intervallo da 0.0 a 1.0 | IMAGE |
| `mask` | La maschera alpha per i fotogrammi del video, seguendo la convenzione di Load Image in cui 1 indica trasparente | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/it.md)

---
**Source fingerprint (SHA-256):** `536bd52af29218d2a342086e92799d3d9310da5ae5cbf02d705ba7503a4d73c8`

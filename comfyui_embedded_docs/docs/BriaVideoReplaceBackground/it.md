# Bria Video Sostituisci Sfondo

Questo nodo sostituisce lo sfondo di un video con un'immagine o un video forniti tramite l'API di Bria. L'output mantiene la risoluzione e la frequenza dei fotogrammi del video in primo piano; uno sfondo con un rapporto d'aspetto diverso viene allungato per adattarsi, quindi rapporti d'aspetto corrispondenti producono risultati non distorti.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Video in primo piano il cui sfondo viene sostituito. | VIDEO | Sì | - |
| `background_image` | Immagine di sfondo da comporre dietro il primo piano. Fornisci un'immagine di sfondo o un video di sfondo, non entrambi. | IMAGE | No | - |
| `background_video` | Video di sfondo da comporre dietro il primo piano. Fornisci un'immagine di sfondo o un video di sfondo, non entrambi. | VIDEO | No | - |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 0) | INT | Sì | da 0 a 2147483647 |

**Nota:** Devi fornire esattamente uno tra `background_image` o `background_video` — non entrambi e nemmeno nessuno. Il video in primo piano e il video di sfondo (se utilizzato) devono avere ciascuno una durata di 60 secondi o inferiore. Quando si utilizza `background_image`, il suo canale alpha viene rimosso prima dell'elaborazione.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video risultante con lo sfondo sostituito, codificato in MP4 (H.264). | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/it.md)

---
**Source fingerprint (SHA-256):** `c487cf7dd434b8523ce64f241c2171c82bb5e0abdc5c3ca3e8b1a1259aeab490`

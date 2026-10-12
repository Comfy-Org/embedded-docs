# NormalizeVideoLatentStart

Questo nodo regola i primi frame di un latent video per renderli più simili ai frame che seguono. Calcola la media e la variazione da un insieme di frame di riferimento più avanti nel video e applica le stesse caratteristiche ai frame iniziali. Ciò aiuta a ridurre le differenze tra i frame iniziali e il resto del video, creando una transizione più fluida e coerente.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `latent` | La rappresentazione latente del video da elaborare. | LATENT | Sì | - |
| `start_frame_count` | Numero di frame latenti da normalizzare, contati dall'inizio (predefinito: 4). | INT | Sì | 1 a 16384 (risoluzione massima) |
| `reference_frame_count` | Numero di frame latenti dopo i frame iniziali da usare come riferimento (predefinito: 5). | INT | Sì | 1 a 16384 (risoluzione massima) |

**Nota:** I frame di riferimento vengono presi subito dopo i frame indicati da `start_frame_count`. Se sono disponibili meno frame di quanti ne richieda `reference_frame_count`, il nodo usa tutti quelli disponibili (al massimo uno in meno rispetto al numero totale di frame del latent). Se il latent video ha un solo frame, non viene eseguita alcuna normalizzazione e il latent originale viene restituito invariato.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | Il latent video elaborato con i frame iniziali normalizzati. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/it.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`

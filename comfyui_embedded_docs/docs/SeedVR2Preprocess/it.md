# SeedVR2Preprocess

Questo nodo prepara un'immagine o un video ridimensionati per il modello SeedVR2 aggiungendo padding fino alla forma attesa dal modello. I valori dei pixel vengono limitati all'intervallo 0-1, altezza e larghezza vengono portate a multipli di 16 tramite padding, e il numero di frame viene aumentato ripetendo l'ultimo frame finché non segue uno schema 4n+1 (1, 5, 9, 13, ...). Il canale alpha viene eliminato durante l'elaborazione; il nodo abbinato Post-Process SeedVR2 Output lo ripristina successivamente dall'immagine ridimensionata originale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `resized_images` | L'immagine ridimensionata da elaborare. | IMAGE | Sì | - |

Nota: l'input può essere un singolo frame, una sequenza di frame o un batch di video (tensori IMAGE 4-D o 5-D). Se ha più di 3 canali, il canale alpha viene eliminato e viene mantenuto solo RGB. Il lato più corto dell'input deve essere di almeno 2 pixel. Il padding spaziale viene riempito di nero (valore 0), e i conteggi di frame validi seguono uno schema 4n+1 (1, 5, 9, 13, ...).

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `images` | L'immagine con padding per la codifica VAE. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/it.md)

---
**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`

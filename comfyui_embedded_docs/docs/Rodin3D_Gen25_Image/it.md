# Rodin3D_Gen25_Image

## Panoramica

Questo nodo genera un modello 3D da una a cinque immagini di riferimento utilizzando l'API Rodin Gen-2.5. Puoi scegliere tra le modalità di qualità Fast, Regular o Extreme-High per bilanciare velocità e costo di generazione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `images` | Da una a cinque immagini di input. La prima immagine viene utilizzata per i materiali quando vengono fornite più immagini. | IMAGE | Sì | da 1 a 5 immagini |
| `mode` | La modalità di qualità di generazione. Le modalità di qualità più elevata producono risultati migliori ma costano di più. | COMBO | Sì | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `material` | Il tipo di materiale per il modello 3D generato. | COMBO | Sì | `"PBR"`<br>`"Matte"` |
| `geometry_file_format` | Il formato file di output per la geometria del modello 3D. | COMBO | Sì | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `texture_mode` | La modalità di generazione della texture. "Original" conserva le texture di input, "Clean" le rimuove e "Style" applica una texture stilizzata. | COMBO | Sì | `"Original"`<br>`"Clean"`<br>`"Style"` |
| `seed` | Un seed casuale per risultati riproducibili. Usa lo stesso seed per ottenere lo stesso output. | INT | Sì | da 0 a 2147483647 |
| `TAPose` | Se applicare la T-pose al modello generato. | BOOLEAN | Sì | True / False |
| `hd_texture` | Se generare una mappa di texture ad alta definizione. | BOOLEAN | Sì | True / False |
| `texture_delight` | Se rimuovere l'illuminazione dalle immagini di input prima della generazione della texture. | BOOLEAN | Sì | True / False |
| `use_original_alpha` | Se usare il canale alpha originale delle immagini di input. | BOOLEAN | Sì | True / False |
| `addon_highpack` | Se generare una versione ad alto numero di poligoni del modello in aggiunta a quella standard. | BOOLEAN | Sì | True / False |
| `bbox_width` | La larghezza del bounding box per il modello generato, in centimetri. | INT | Sì | da 1 a 1000 |
| `bbox_height` | L'altezza del bounding box per il modello generato, in centimetri. | INT | Sì | da 1 a 1000 |
| `bbox_length` | La lunghezza del bounding box per il modello generato, in centimetri. | INT | Sì | da 1 a 1000 |
| `height_cm` | L'altezza del modello generato in centimetri. | INT | Sì | da 1 a 300 |

**Nota sul numero di immagini:** Il nodo accetta da 1 a 5 immagini. Se fornisci un batch di immagini (ad es., un batch di 4 immagini), ogni immagine del batch viene considerata come un'immagine di input separata. Fornire più di 5 immagini causerà un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `model_file` | Il file del modello 3D generato nel formato geometrico selezionato. | FILE3D |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Image/it.md)

---
**Source fingerprint (SHA-256):** `6437f8d34624fccfb92505bcdc627db2df2f4159c929a4f7b00352906c609a25`

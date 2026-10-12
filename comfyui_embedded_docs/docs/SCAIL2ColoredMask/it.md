# Crea Maschera Colorata SCAIL-2

Questo nodo renderizza i dati di tracking SAM3 in maschere colorate che vengono utilizzate dal nodo WanSCAILToVideo. Elabora i dati di tracking da un video della posa di guida e opzionalmente un'immagine di riferimento, assegnando colori coerenti a ciascuna persona tracciata in entrambi gli output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `driving_track_data` | Traccia SAM3 del video della posa di guida. Verrà renderizzata nell'output pose_video_mask. | SAM3_TRACK_DATA | Sì | - |
| `ref_track_data` | Traccia SAM3 dell'immagine di riferimento (un'identità per oggetto, colorata in ordine di batch), o una MASK semplice del soggetto di riferimento (renderizzata come singola identità). | SAM3_TRACK_DATA or MASK | No | - |
| `object_indices` | Lista di indici di persona separati da virgola da includere (es. '0,2,3'). Applicata sia alle maschere di riferimento che a quelle del video di posa. Vuoto = tutti. (default: "") | STRING | Sì | - |
| `sort_by` | Ordine in cui i colori della palette vengono assegnati agli oggetti tracciati (applicato sia al riferimento che al video di posa in modo che ogni identità mantenga lo stesso colore). Gli oggetti che compaiono nei fotogrammi precedenti vengono sempre prima; all'interno di un fotogramma, left_to_right = l'oggetto più a sinistra (per centroide alla prima comparsa) riceve il primo colore, area = l'oggetto più grande (per area della maschera alla prima comparsa) riceve il primo colore; none = mantiene l'ordine di SAM3. (default: "left_to_right") | COMBO | Sì | `"none"`<br>`"left_to_right"`<br>`"area"` |
| `replacement_mode` | False = Modalità Animazione (pose_video_mask ha sfondo nero, reference_image_mask ha sfondo bianco). True = Modalità Sostituzione (pose_video_mask ha sfondo bianco, reference_image_mask ha sfondo nero). (default: False) | BOOLEAN | Sì | False<br>True |

Nota: `object_indices` accetta solo cifre separate da virgola; le voci non numeriche e gli indici fuori intervallo vengono ignorati. Quando `ref_track_data` non viene fornito, l'output `reference_image_mask` è un riempimento solido usando il colore di sfondo di riferimento (bianco in Modalità Animazione, nero in Modalità Sostituzione).

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `pose_video_mask` | Maschera colorata renderizzata dai dati di tracking del video della posa di guida. Il colore di sfondo segue l'impostazione replacement_mode. | IMAGE |
| `reference_image_mask` | Maschera colorata renderizzata dai dati di tracking dell'immagine di riferimento. Lo sfondo è nero in Modalità Sostituzione, bianco in Modalità Animazione. Se non vengono forniti dati di riferimento, restituisce un riempimento solido corrispondente al colore di sfondo di riferimento. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SCAIL2ColoredMask/it.md)

---
**Source fingerprint (SHA-256):** `ce0669ad0ed3c76cc18ef0ee7b620f5aa6eaa1e5b96c189941c0a5b744c3351f`

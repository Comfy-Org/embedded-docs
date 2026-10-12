# MoGeGeometryToFOV

Questo nodo deriva il campo visivo e la lunghezza focale dai parametri intrinseci della fotocamera memorizzati in un oggetto geometria MoGe. Può restituire il FOV verticale, orizzontale o diagonale, in gradi o radianti. L'output FOV verticale può essere usato, ad esempio, per alimentare il nodo SAM3DBody_Predict.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `moge_geometry` | L'oggetto geometria MoGe. Deve contenere una matrice intrinseca e almeno uno tra i dati `image`, `points` o `depth`, usato per leggere l'altezza in pixel per la conversione della lunghezza focale. | MOGE_GEOMETRY | Sì | — |
| `axis` | L'asse lungo cui viene calcolato il FOV: "vertical" (fov_y), "horizontal" (fov_x) o "diagonal" (predefinito: "vertical"). | COMBO | Sì | "vertical"<br>"horizontal"<br>"diagonal" |
| `unit` | Unità di output per il FOV (predefinito: "degrees"). | COMBO | Sì | "degrees"<br>"radians" |

Nota: il nodo genera un errore se `moge_geometry` non contiene parametri intrinseci (la geometria panorama non ne contiene) oppure se non contiene né dati `image`, né `points`, né `depth`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `fov` | Il campo visivo lungo l'asse selezionato, nell'unità selezionata (gradi o radianti). | FLOAT |
| `focal_pixels` | La lunghezza focale dell'obiettivo in pixel, derivata dal parametro intrinseco verticale e dall'altezza in pixel. | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/it.md)

---
**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`

# DA3GeometryToPointCloud

Converte una mappa di profondità da un oggetto DA3_GEOMETRY in una nuvola di punti 3D. Applica un filtraggio basato sulla confidenza e sulle maschere del cielo e trasforma i punti in un sistema di coordinate mondiali comune, adatto a scene multi-vista.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `da3_geometry` | L'oggetto DA3_GEOMETRY contenente i dati di profondità e, facoltativamente, l'immagine e le mappe di confidenza e del cielo | DA3_GEOMETRY | Sì | - |
| `batch_index` | Quale immagine di un batch convertire (predefinito: 0) | INT | Sì | 0 to 4096 |
| `confidence_threshold` | Esclude i pixel la cui confidenza normalizzata per immagine è inferiore a questo valore (0 = mantieni tutto). Usato quando la geometria dispone di una mappa di confidenza (modelli Small/Base). (predefinito: 0.1) | FLOAT | Sì | 0.0 to 1.0 |
| `use_sky_mask` | Esclude i pixel con probabilità di cielo (sky >= 0.5). Usato quando la geometria dispone di una mappa del cielo (modelli Mono/Metric). (predefinito: True) | BOOLEAN | Sì | True or False |
| `downsample` | Prende ogni N-esimo pixel (1 = risoluzione completa). Valori più alti producono meno punti e un'elaborazione più rapida. (predefinito: 1) | INT | Sì | 1 to 16 |

**Note:**
- `batch_index` deve essere inferiore alla dimensione del batch della geometria di input; in caso contrario il nodo genera un errore.
- Se il filtraggio rimuove tutti i pixel, il nodo genera un errore. Ridurre `confidence_threshold` o disabilitare `use_sky_mask` può evitarlo.
- `confidence_threshold` viene applicato solo quando la geometria include una mappa di confidenza (modelli Small/Base).
- `use_sky_mask` viene applicato solo quando la geometria include una mappa del cielo (modelli Mono/Metric).
- Quando `downsample` è maggiore di 1, i parametri intrinseci della camera vengono scalati di conseguenza, in modo che i punti proiettati rimangano corretti.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `point_cloud` | Una nuvola di punti contenente punti 3D filtrati, colori opzionali e valori di confidenza opzionali | DA3_POINT_CLOUD |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToPointCloud/it.md)

---
**Source fingerprint (SHA-256):** `3cf5bdbb8afdfcfc02f9832a8cbc5a3df49da755dea6df01792aa6ef9e5d7287`

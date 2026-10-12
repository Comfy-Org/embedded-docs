# DA3Render

Questo nodo genera una visualizzazione dai dati di geometria di Depth Anything 3. Può restituire mappe di profondità, mappe di confidenza o maschere del cielo a seconda della modalità di output selezionata.

## Input

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `da3_geometry` | Il pacchetto di dati di geometria di Depth Anything 3 contenente profondità e, opzionalmente, tensori sky e confidence | DA3_GEOMETRY | Sì | - |
| `output` | Il tipo di visualizzazione da generare.<br>- depth: immagine di profondità in scala di grigi normalizzata.<br>- depth_colored: profondità mappata attraverso la colormap Turbo.<br>- sky_mask: probabilità del cielo in [0, 1] (solo per modelli Mono/Metric).<br>- confidence: confidenza di profondità normalizzata (solo per modelli Small/Base). | COMBO | Sì | "depth"<br>"depth_colored"<br>"sky_mask"<br>"confidence" |

### Sottoparametri per le opzioni di `output`

Quando `output` è impostato su `"depth"` o `"depth_colored"`:

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `normalization` | Metodo di normalizzazione della profondità.<br>- v2_style: normalizzazione media/deviazione standard per risultati percettivamente bilanciati (predefinito).<br>- min_max: estende l'intero intervallo di profondità a [0, 1] per il massimo contrasto.<br>- raw: nessun ridimensionamento, preserva le unità metriche per il modello Metric. | COMBO | Sì | "v2_style"<br>"min_max"<br>"raw" |
| `apply_sky_clip` | Ritaglia la profondità della regione sky al 99° percentile della profondità in primo piano prima della normalizzazione. Richiede una chiave sky nell'input da3_geometry (solo per modelli Mono/Metric). Predefinito: False | BOOLEAN | Sì | True<br>False |

Quando `output` è impostato su `"sky_mask"`:

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `colored` | Applica la colormap Turbo alla maschera del cielo. Predefinito: False | BOOLEAN | Sì | True<br>False |

Quando `output` è impostato su `"confidence"`:

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `colored` | Applica la colormap Turbo alla mappa di confidenza. Predefinito: False | BOOLEAN | Sì | True<br>False |

### Vincoli dei parametri

- Quando `apply_sky_clip` è impostato su True, l'input `da3_geometry` deve contenere un tensore sky. Questo è disponibile solo quando si utilizzano modelli Mono o Metric. Se il tensore sky è mancante, il nodo genererà un errore.
- L'opzione di output `sky_mask` richiede un tensore sky nell'input `da3_geometry`. Questo è disponibile solo con modelli Mono o Metric.
- L'opzione di output `confidence` richiede un tensore di confidenza nell'input `da3_geometry`. Questo è disponibile solo con modelli Small o Base.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `IMAGE` | La visualizzazione renderizzata come tensore immagine. Per gli output depth, restituisce una mappa di profondità in scala di grigi o colorata. Per sky_mask e confidence, restituisce una visualizzazione in scala di grigi o colorata a seconda del parametro colored. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3Render/it.md)

---
**Source fingerprint (SHA-256):** `54d4cde95a916cac26c8a2e19c5623e794d46c0d7652f1c8204f9f2a0deabe0c`

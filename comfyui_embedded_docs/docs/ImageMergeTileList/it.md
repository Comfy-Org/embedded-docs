# Unisci elenco di tile in immagine

Questo nodo prende un elenco di tile di immagine e li unisce di nuovo in un'unica immagine più grande. È progettato per ricostruire un'immagine che era stata precedentemente suddivisa in una griglia di tile sovrapposti, utilizzando una tecnica di fusione ponderata per creare un risultato finale senza giunture.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image_list` | Un elenco di tile di immagine da unire. Il primo tile dell'elenco viene utilizzato per determinare le dimensioni dei tile e il tipo di dato per l'intero processo. | IMAGE | Sì | N/A |
| `final_width` | La larghezza dell'immagine finale unita in pixel (predefinito: 1024). | INT | Sì | 64 - 32768 |
| `final_height` | L'altezza dell'immagine finale unita in pixel (predefinito: 1024). | INT | Sì | 64 - 32768 |
| `overlap` | La quantità di sovrapposizione tra tile adiacenti in pixel. Un valore maggiore di 0 abilita un effetto di fusione morbida sulle giunture dei tile (predefinito: 128). | INT | Sì | 0 - 4096 |

**Nota:** `image_list` è un elenco di input dinamico. Il nodo elaborerà i tile nell'ordine in cui sono forniti, fino al numero necessario per riempire la griglia definita da `final_width`, `final_height` e dalle dimensioni del primo tile. Se l'elenco contiene più tile del necessario, quelli in eccesso vengono ignorati.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'immagine finale unita, ricostruita a partire dai tile di input. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageMergeTileList/it.md)

---
**Source fingerprint (SHA-256):** `41b570bf758093f3693c015e7976b946b9d93ca56db2bf66617149f259ae8c06`

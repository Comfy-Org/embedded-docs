# Flux Cancella Immagine

Rimuove l'oggetto mascherato da un'immagine e ricostruisce lo sfondo. Dipingi la maschera su ciò che desideri cancellare e il nodo riempie l'area con un contenuto di sfondo plausibile.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da elaborare | IMAGE | Sì | - |
| `mask` | Le aree bianche vengono rimosse; le aree nere vengono conservate | MASK | Sì | - |
| `dilate_pixels` | Espande i confini della maschera per garantire una copertura pulita dei bordi dell'oggetto (predefinito: 10) | INT | Sì | 0 a 25 |
| `seed` | Il seme casuale utilizzato per creare il rumore (predefinito: 0) | INT | No | 0 a 2147483647 |

**Nota:** L'immagine di input deve essere di almeno 256x256 pixel in entrambe le dimensioni. La maschera viene ridimensionata automaticamente per corrispondere alle dimensioni dell'immagine e il canale alpha dell'immagine viene rimosso prima dell'elaborazione.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine risultante con l'oggetto mascherato rimosso e lo sfondo ricostruito | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxEraseNode/it.md)

---
**Source fingerprint (SHA-256):** `124be59b9829aa9f865d7ec76cd68f7978e2010cd3a84f25742a1c17f2d70b76`

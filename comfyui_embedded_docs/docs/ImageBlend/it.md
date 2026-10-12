# ImageBlend

Il nodo `ImageBlend` è progettato per fondere due immagini in base a una modalità di fusione e a un fattore di fusione specificati. Supporta varie modalità di fusione come normal, multiply, screen, overlay, soft light e difference, consentendo tecniche versatili di manipolazione e compositing delle immagini. Questo nodo è essenziale per creare immagini composite regolando l'interazione visiva tra due livelli immagine.

## Input

| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image1` | La prima immagine da fondere. Funge da livello di base per l'operazione di fusione. | `IMAGE` |
| `image2` | La seconda immagine da fondere. A seconda della modalità di fusione, modifica l'aspetto della prima immagine. | `IMAGE` |
| `blend_factor` | Determina il peso della seconda immagine nella fusione. Un fattore di fusione più alto dà maggiore rilievo alla seconda immagine nella fusione risultante. | `FLOAT` |
| `blend_mode` | Specifica il metodo di fusione delle due immagini. Supporta modalità come normal, multiply, screen, overlay, soft light e difference, ciascuna delle quali produce un effetto visivo unico. | COMBO[STRING] |

## Output

| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'immagine risultante dopo aver fuso le due immagini di input in base alla modalità di fusione e al fattore specificati. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlend/it.md)

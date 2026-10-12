# Sfoca Immagine

Il nodo `ImageBlur` applica una sfocatura gaussiana a un'immagine, consentendo l'ammorbidimento dei bordi e la riduzione dei dettagli e del rumore. Offre il controllo su intensità e diffusione della sfocatura tramite parametri.

## Input

| Campo | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine di input da sfocare. È il target principale dell'effetto di sfocatura. | `IMAGE` |
| `blur_radius` | Determina il raggio dell'effetto di sfocatura. Un raggio maggiore produce una sfocatura più pronunciata. | `INT` |
| `sigma` | Controlla la diffusione della sfocatura. Un valore sigma più alto indica che la sfocatura influenzerà un'area più ampia attorno a ciascun pixel. | `FLOAT` |

## Output

| Campo | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'output è la versione sfocata dell'immagine di input, con il grado di sfocatura determinato dai parametri di input. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlur/it.md)

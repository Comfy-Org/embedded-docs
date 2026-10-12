# EmptyHiDreamO1LatentImage

Questo nodo crea un'immagine latente vuota nello spazio dei pixel per il modello HiDream-O1-Image. Genera un tensore vuoto di zeri che funge da punto di partenza per la generazione dell'immagine, con dimensioni definite dagli input width, height e batch_size.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `width` | La larghezza dell'immagine latente in pixel. Predefinito: 2048. Il valore deve essere un multiplo di 32. Il modello è stato addestrato a circa 4 megapixel; risoluzioni inferiori possono ridurre visibilmente la qualità. | INT | Sì | 64 a 4096 (passo: 32) |
| `height` | L'altezza dell'immagine latente in pixel. Predefinito: 2048. Il valore deve essere un multiplo di 32. Il modello è stato addestrato a circa 4 megapixel; risoluzioni inferiori possono ridurre visibilmente la qualità. | INT | Sì | 64 a 4096 (passo: 32) |
| `batch_size` | Il numero di immagini latenti da generare in un singolo batch. Predefinito: 1. | INT | Sì | 1 a 64 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples` | Un tensore riempito di zeri che rappresenta l'immagine latente vuota, con forma (batch_size, 3, height, width). | LATENT |

## Note

- Il modello HiDream-O1-Image è stato addestrato a circa 4 megapixel. L'uso di risoluzioni significativamente inferiori può comportare una riduzione visibile della qualità dell'immagine.
- Le risoluzioni di addestramento includono: 2048x2048, 2304x1728, 1728x2304, 2560x1440, 1440x2560, 2496x1664, 1664x2496, 3104x1312, 1312x3104, 2304x1792, 1792x2304.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHiDreamO1LatentImage/it.md)

---
**Source fingerprint (SHA-256):** `7412639e261512d9174e60009143c8c06c354e2a20ada7271837d72053426be5`

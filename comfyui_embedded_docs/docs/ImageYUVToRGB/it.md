# Immagine da YUV a RGB

Il nodo ImageYUVToRGB converte le immagini dallo spazio colore YUV allo spazio colore RGB. Prende tre immagini di input separate che rappresentano le componenti Y (luma), U (proiezione blu) e V (proiezione rossa) e le combina in un'unica immagine RGB.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `Y` | L'immagine di input della componente Y (luminanza). Se l'immagine ha più di tre canali, vengono usati solo i primi tre e ne viene calcolata la media in un unico canale. | IMAGE | Sì | - |
| `U` | L'immagine di input della componente U (proiezione blu). Se l'immagine ha più di tre canali, vengono usati solo i primi tre e ne viene calcolata la media in un unico canale. | IMAGE | Sì | - |
| `V` | L'immagine di input della componente V (proiezione rossa). Se l'immagine ha più di tre canali, vengono usati solo i primi tre e ne viene calcolata la media in un unico canale. | IMAGE | Sì | - |

**Nota:** Tutte e tre le immagini di input (Y, U e V) devono essere fornite insieme e devono avere dimensioni compatibili (altezza, larghezza e dimensione del batch corrispondenti) affinché la conversione riesca.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | L'immagine RGB convertita | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/it.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`

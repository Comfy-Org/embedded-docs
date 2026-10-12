# ImageRGBToYUV

Il nodo ImageRGBToYUV converte un'immagine RGB in componenti di colore in stile YUV usando una conversione di colore da RGB a YCbCr. Suddivide il risultato in tre immagini separate — Y (luminanza, o luminosità), U (crominanza della differenza blu) e V (crominanza della differenza rossa) — e restituisce ciascuna componente con la stessa larghezza e altezza dell'input.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | L'immagine RGB di input da convertire in componenti Y, U e V. Se l'immagine contiene un canale alfa, vengono usati solo i primi tre canali (RGB). | IMAGE | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `Y` | La componente di luminanza (luminosità) dello spazio colore YUV, restituita come immagine a tre canali | IMAGE |
| `U` | La componente di crominanza della differenza blu dello spazio colore YUV, restituita come immagine a tre canali | IMAGE |
| `V` | La componente di crominanza della differenza rossa dello spazio colore YUV, restituita come immagine a tre canali | IMAGE |

Ogni output ha la stessa larghezza e altezza dell'immagine di input. La corrispondente componente Y, U o V viene ripetuta su tutti e tre i canali, in modo che ogni output venga restituito come immagine standard a tre canali.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/it.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`

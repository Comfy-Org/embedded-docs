# Post-Elaborazione Output SeedVR2

Questo nodo allinea l'immagine generata con l'immagine originale ridimensionata e applica una correzione del colore opzionale. Prende l'output di un processo di upscaling SeedVR2 e lo adatta per corrispondere ai colori e alle dimensioni dell'immagine di riferimento originale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `images` | L'immagine generata da elaborare. | IMAGE | Sì | - |
| `original_resized_images` | L'immagine originale ridimensionata prima della pre-elaborazione, usata come riferimento. | IMAGE | Sì | - |
| `color_correction_method` | Metodo per far corrispondere i colori dell'immagine generata a quelli dell'immagine originale. lab: trasferisce il colore nello spazio CIELAB, preservando i dettagli (più fedele). wavelet: trasferisce il colore a bassa frequenza, mantenendo i dettagli ad alta frequenza dell'immagine upscalata. adain: abbina media/deviazione standard per canale (più veloce, tinta globale). none: salta il trasferimento del colore (solo allineamento geometrico). (predefinito: "lab") | COMBO | Sì | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Nota:** Entrambi gli input possono essere tensori 4-D (batch, altezza, larghezza, canali) o 5-D (batch, fotogrammi, altezza, larghezza, canali). Il nodo ritaglia entrambi al valore più piccolo di batch, numero di fotogrammi, altezza e larghezza, quindi non devono corrispondere esattamente. Quando viene usato un metodo di correzione del colore diverso da `none`, l'immagine di riferimento viene prima ridimensionata alle dimensioni dell'output. La correzione del colore viene elaborata in blocchi che tengono conto della memoria, passando a una dimensione di blocco inferiore se la memoria si esaurisce. L'altezza e la larghezza dell'output vengono arrotondate per difetto a numeri pari. Se l'immagine di riferimento ha un canale alfa (4 canali), quel canale alfa viene preservato e applicato all'output.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `images` | L'immagine allineata e con correzione del colore. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/it.md)

---
**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`

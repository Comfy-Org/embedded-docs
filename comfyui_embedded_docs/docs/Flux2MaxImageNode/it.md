# Flux.2 [max] Immagine

Genera un'immagine con Flux.2 [max] tramite l'API BFL a partire da un prompt e dimensioni di output esplicite, opzionalmente guidata da immagini di riferimento. Espone gli stessi input di Flux.2 [pro] Image.

**Nota:** questo nodo è contrassegnato come deprecato nel codice sorgente.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt per la generazione o la modifica dell'immagine. | STRING | Sì | - |
| `larghezza` | Larghezza dell'immagine generata in pixel (predefinito: 1024). | INT | Sì | 256 a 2048 (passo: 32) |
| `altezza` | Altezza dell'immagine generata in pixel (predefinito: 768). | INT | Sì | 256 a 2048 (passo: 32) |
| `seed` | Il seed casuale utilizzato per creare il rumore (predefinito: 0). | INT | Sì | 0 a 18446744073709551615 |
| `upsampling del prompt` | Indica se eseguire l'upsampling sul prompt. Se attivo, il prompt viene modificato automaticamente per una generazione più creativa (predefinito: `True`). Questa è un'impostazione avanzata. | BOOLEAN | Sì | True / False |
| `immagini` | Immagini di riferimento opzionali per la generazione image-to-image. Ogni immagine viene ridimensionata verso il basso a un massimo di 2048x2048 pixel prima del caricamento. | IMAGE | No | 0 a 9 immagini |

**Vincoli:**

* Connettere più di 9 immagini di riferimento genera un errore.
* La dimensione dell'output viene addebitata per megapixel, quindi valori maggiori di `width` e `height` costano di più.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine generata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2MaxImageNode/it.md)

---
**Source fingerprint (SHA-256):** `cd540606835e7808861d9a96584731100b1bf9c996f18586fed39e8a2d32a29f`

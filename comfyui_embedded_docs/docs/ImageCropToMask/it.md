# Ritaglia immagine in base alla maschera

Ritaglia un'immagine al bounding box della sua maschera, producendo un soggetto centrato su un colore di sfondo solido. Il nodo compone l'immagine mascherata sopra lo sfondo scelto e ridimensiona il risultato alle dimensioni di output specificate, rendendolo adatto a pipeline 3D che richiedono un soggetto centrato, privo di sfondo, a una risoluzione fissa.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `images` | L'immagine o il batch di immagini di input da ritagliare. | IMAGE | Sì | — |
| `masks` | La maschera o il batch di maschere che definisce l'area del soggetto. Una singola maschera viene applicata a tutte le immagini; in caso contrario, la dimensione del batch delle maschere deve corrispondere a quella del batch delle immagini. Se la risoluzione della maschera differisce da quella dell'immagine, la maschera viene automaticamente ridimensionata per corrispondere. | MASK | Sì | — |
| `width` | Larghezza di output in pixel. (predefinito: 1024) | INT | Sì | 64 a 4096 (passo 8) |
| `height` | Altezza di output in pixel. (predefinito: 1024) | INT | Sì | 64 a 4096 (passo 8) |
| `pad_factor` | Margine extra attorno al bounding box della maschera come moltiplicatore. (predefinito: 1.0) | FLOAT | Sì | 1.0 a 2.0 (passo 0.01) |
| `grow_mask` | Espande o riduce la maschera di questo numero di pixel prima del ritaglio. I valori positivi espandono la maschera, quelli negativi la riducono. (predefinito: 0) | INT | Sì | -32 a 32 (passo 1) |
| `background` | Colore di sfondo dietro il soggetto mascherato. (predefinito: #000000) | COLOR | Sì | — |

Nota: La regione di ritaglio è centrata sul bounding box della maschera e il suo rapporto d'aspetto corrisponde a `width` / `height`. Il nodo rileva e corregge automaticamente una maschera invertita (pixel in primo piano lungo il bordo, sfondo al centro). Se la maschera non contiene pixel in primo piano, il nodo prova la maschera invertita; se anche questa è vuota, registra un avviso e ritaglia l'intera immagine. Viene generato un errore quando la dimensione del batch delle maschere non corrisponde a quella del batch delle immagini e non si tratta di una singola maschera.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `images` | Le immagini composite ritagliate (soggetto mascherato sopra il colore di sfondo scelto), ridimensionate a `width` x `height`. La dimensione del batch corrisponde a quella del batch delle immagini di input. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropToMask/it.md)

---
**Source fingerprint (SHA-256):** `fcc14b5db7318699526dd544d404f78f9d1ab362b73769276f113f2b1062b214`

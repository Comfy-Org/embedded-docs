# Selettore di Risoluzione

Il nodo Resolution Selector calcola la larghezza e l'altezza in pixel in base a un rapporto d'aspetto scelto e a una risoluzione totale target in megapixel. È utile per generare dimensioni coerenti per altri nodi, come il nodo Empty Latent Image.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `aspect_ratio` | Il rapporto d'aspetto per le dimensioni di output (predefinito: `"1:1 (Square)"`). | COMBO | Sì | `"1:1 (Square)"`<br>`"2:3 (Portrait Photo)"`<br>`"3:2 (Photo)"`<br>`"3:4 (Portrait Standard)"`<br>`"4:3 (Standard)"`<br>`"9:16 (Portrait Widescreen)"`<br>`"16:9 (Widescreen)"`<br>`"21:9 (Ultrawide)"` |
| `megapixels` | Megapixel totali target. 1.0 MP ≈ 1024x1024 per un'immagine quadrata (predefinito: 1.0). | FLOAT | Sì | 0.1 - 16.0 (passo: 0.1) |
| `preview` | Anteprima in tempo reale della risoluzione di output calcolata. Questo widget di sola lettura si aggiorna automaticamente e non accetta input dell'utente. | RESOLUTION_PREVIEW | No | N/A |
| `multiple` | Il multiplo più vicino del risultato a cui impostare la risoluzione selezionata (predefinito: 8). | INT | No | 8 - 128 (passo: 4) |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `width` | Larghezza calcolata in pixel moltiplicata per il multiplo selezionato. | INT |
| `height` | Altezza calcolata in pixel moltiplicata per il multiplo selezionato. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/it.md)

---
**Source fingerprint (SHA-256):** `dd4c7f977ed69a873a48da4b01c5c8f0b6563cfd743740235fc0ad5762579697`

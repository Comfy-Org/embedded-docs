# Pad Image

Aggiunge un riempimento a un'immagine con un colore pieno o una copia speculare dei suoi bordi. Il riempimento può essere impostato come pixel esatti su ciascun lato, come moltiplicatore di dimensione, oppure come la quantità minima che rende larghezza e altezza divisibili per un numero, il che è utile prima del salvataggio o della tassellatura. L'immagine originale mantiene la sua posizione: i riempimenti `left` e `top` vengono aggiunti prima di essa, `right` e `bottom` dopo.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine a cui aggiungere il riempimento. | IMAGE | Sì | - |
| `padding_type` | Quanto riempimento aggiungere: `"pad dimensions"` per quantità esatte per lato, `"pad by multiplier"` per una dimensione di output relativa all'input, oppure `"pad to multiple"` per raggiungere il multiplo successivo. Selezionando un'opzione vengono mostrati i relativi parametri. | DYNAMIC_COMBO | Sì | `"pad dimensions"`<br>`"pad by multiplier"`<br>`"pad to multiple"` |
| `left` | Pixel da aggiungere a sinistra. Disponibile quando `padding_type` è `"pad dimensions"` (predefinito: 0). | INT | Sì | 0 a 16384 |
| `top` | Pixel da aggiungere in alto. Disponibile quando `padding_type` è `"pad dimensions"` (predefinito: 0). | INT | Sì | 0 a 16384 |
| `right` | Pixel da aggiungere a destra. Disponibile quando `padding_type` è `"pad dimensions"` (predefinito: 0). | INT | Sì | 0 a 16384 |
| `bottom` | Pixel da aggiungere in basso. Disponibile quando `padding_type` è `"pad dimensions"` (predefinito: 0). | INT | Sì | 0 a 16384 |
| `multiplier` | Dimensione di output relativa all'input; ad esempio 1.5 aggiunge il 25% su ciascun lato. Il riempimento viene suddiviso equamente tra i lati opposti. Disponibile quando `padding_type` è `"pad by multiplier"` (predefinito: 1.0). | FLOAT | Sì | 1.0 a 8.0 (passo 0.01) |
| `multiple` | Aggiunge riempimento in modo che larghezza e altezza siano divisibili per questo numero. Il riempimento viene suddiviso equamente tra i lati opposti, con il pixel in più assegnato a destra e in basso. Disponibile quando `padding_type` è `"pad to multiple"` (predefinito: 32). | INT | Sì | 1 a 16384 |
| `padding_style` | Cosa utilizzare per riempire l'area aggiunta: `"color"` o `"mirror image"`. Selezionando un'opzione vengono mostrati i relativi parametri. | DYNAMIC_COMBO | Sì | `"color"`<br>`"mirror image"` |
| `color` | Colore di riempimento per l'area aggiunta; il canale alfa viene ignorato. Disponibile quando `padding_style` è `"color"` (predefinito: `"#000000"`). | COLOR | Sì | - |
| `feathering` | Sfuma questo numero di pixel del bordo dell'immagine nel colore di riempimento sui lati riempiti. 0 lascia un bordo netto. Disponibile quando `padding_style` è `"color"` (predefinito: 0). | INT | Sì | 0 a 16384 |

`"mirror image"` riflette i bordi dell'immagine invece di riempirli con un colore. Il pixel di bordo non viene ripetuto e, quando il riempimento è più largo o più alto dell'immagine stessa, l'immagine speculare si ripete per coprire il resto. Quando ogni quantità di riempimento risulta 0, l'immagine di input viene restituita invariata.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'immagine con riempimento, con la dimensione batch e il numero di canali dell'input. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PadImageNode/it.md)

---
**Source fingerprint (SHA-256):** `9373cd6aa287befba74374b9b2a6c38b20344b5715e9aaa4cf49282ae930c91d`

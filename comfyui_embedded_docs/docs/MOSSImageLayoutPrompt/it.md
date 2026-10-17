# MOSS-Image Layout Prompt

Costruisce il prompt di layout che MOSS-Image legge. Prende gli elementi disegnati nel nodo Create Bounding Boxes e genera un layout JSON con una voce per ogni riquadro: la sua etichetta, la sua didascalia e il suo rettangolo nello spazio in pixel della tela di destinazione. Imposta `width` e `height` sulla dimensione dell'immagine che intendi generare, quindi collega l'output all'input prompt del codificatore di testo. Se non è connesso alcun elemento, il testo del prompt viene restituito invariato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `prompt` | Descrizione dell'intera immagine. Diventa la didascalia del layout. | STRING | Sì | - |
| `element` | Gli elementi da posizionare, presi dal nodo Create Bounding Boxes. Ogni riquadro contribuisce con la propria didascalia; i riquadri di testo contribuiscono anche con il loro testo, e i riquadri che contengono una palette di colori la mantengono. | ARRAY | Sì | - |
| `width` | Larghezza dell'immagine generata in pixel. I riquadri vengono convertiti in questa griglia di pixel, quindi usa la dimensione dell'immagine che intendi generare (predefinito: 1024). | INT | Sì | da 16 a 16384 (passo 16) |
| `height` | Altezza dell'immagine generata in pixel. I riquadri vengono convertiti in questa griglia di pixel, quindi usa la dimensione dell'immagine che intendi generare (predefinito: 1024). | INT | Sì | da 16 a 16384 (passo 16) |
| `character_boxes` | Numeri dei riquadri da etichettare come personaggi anziché come oggetti, come contrassegnati nell'anteprima di Create Bounding Boxes, ad esempio "1, 3". Ogni numero nella stringa viene letto, quindi qualsiasi separatore funziona (predefinito: vuoto). | STRING | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `prompt` | Il prompt di layout: un oggetto JSON che contiene la didascalia, una voce per ogni riquadro e il formato delle coordinate dei riquadri. Il testo di input viene passato così com'è quando non è connesso alcun elemento. | STRING |

## Note

I rettangoli dei riquadri arrivano da Create Bounding Boxes come coordinate normalizzate tra 0 e 1000 e vengono scritti nel layout in pixel relativi al centro della tela, nell'ordine `yxyx`. I valori `width` e `height` devono quindi corrispondere all'immagine generata, altrimenti i riquadri finiscono nel posto sbagliato.

Un riquadro che contiene testo viene sempre etichettato come testo, un riquadro il cui numero è elencato in `character_boxes` viene etichettato come personaggio, e ogni altro riquadro viene etichettato come oggetto.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MOSSImageLayoutPrompt/it.md)

---
**Source fingerprint (SHA-256):** `da012a8d0dceaf6391110c90bd677d7929920d60fe961c00e5011b037206aa9a`

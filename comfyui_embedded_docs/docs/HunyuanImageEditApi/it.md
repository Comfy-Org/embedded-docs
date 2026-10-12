# HunyuanImageEditApi

Il nodo Tencent HY Image: Edit modifica o combina immagini di riferimento a partire da un'istruzione testuale con il modello Hunyuan Image di Tencent. Collega da una a cinque immagini, descrivi la modifica nel prompt e fai riferimento alle immagini come `@Image1`, `@Image2` e così via. Il nodo carica le immagini di riferimento, invia la richiesta all'API e restituisce il risultato modificato.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello usato per la modifica. Il modello selezionato determina quali input aggiuntivi vengono mostrati. | DYNAMIC_COMBO | Sì | `"hy-image-3.5-preview"` |

### Input di hy-image-3.5-preview

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Le istruzioni di modifica. Supporta riferimenti in stile `@Image1` alle immagini collegate. Non deve essere vuoto (predefinito: vuoto). | STRING | Sì | Qualsiasi testo |
| `aspect_ratio` | Proporzioni dell'output. `"auto"` segue le proporzioni della prima immagine di riferimento e non è disponibile a 4K. Ignorato quando `resolution` è `"custom"`. | COMBO | Sì | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"` (predefinito: `"auto"`) |
| `resolution` | Area in pixel dell'output: 1K corrisponde a circa 1024x1024, 2K a circa 2048x2048 e 4K a circa 4096x4096. Qualsiasi valore superiore a 2K viene renderizzato a 2K e ingrandito dal modello. Imposta su `"custom"` per usare `width` e `height` invece di un'area predefinita. | COMBO | Sì | `"1K"`<br>`"2K"`<br>`"4K"`<br>`"custom"` (predefinito: `"2K"`) |
| `width` | Larghezza dell'output in pixel. Usata solo quando `resolution` è `"custom"`. | INT | Sì | 256-8192, passo di 16 (predefinito: 2048) |
| `height` | Altezza dell'output in pixel. Usata solo quando `resolution` è `"custom"`. | INT | Sì | 256-8192, passo di 16 (predefinito: 2048) |
| `seed` | Seme usato per la generazione. I risultati variano comunque tra esecuzioni con lo stesso seme. | INT | Sì | 0-2147483647 (predefinito: 42) |
| `reference_detail` | Quanto dettaglio delle immagini di riferimento vede il modello: `"standard"` consente fino a 1024x1024 pixel per immagine, `"high"` fino a 2048x2048 e preserva meglio testi piccoli e dettagli fini, ma richiede più tempo. Questo è un parametro avanzato. | COMBO | No | `"standard"`<br>`"high"` (predefinito: `"standard"`) |
| `watermark` | Se aggiungere una filigrana generata dall'IA al risultato. Questo è un parametro avanzato. | BOOLEAN | No | true<br>false (predefinito: false) |

### Input di riferimento

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `images` | Le immagini di riferimento da modificare o combinare. Slot espandibile: collega da 1 a 5 immagini (`image_1` fino a `image_5`). Fai riferimento a esse nel prompt come `@Image1` ... `@Image5`, numerate nell'ordine di input; un input in batch conta una volta per immagine. | IMAGE | Sì | 1-5 immagini |

`prompt` non deve essere vuoto, e un riferimento nel prompt come `@Image3` genera un errore quando sono collegate solo 1 o 2 immagini. Si possono usare al massimo 5 immagini di riferimento in totale, contando separatamente ogni immagine di un batch. Con la risoluzione `"custom"`, `width` e `height` devono entrambi essere multipli di 16 e il loro prodotto non deve superare il limite di area di 4096 x 4096 pixel (circa 16,7 megapixel); qualsiasi proporzione va bene, anche se oltre circa 6:1 il modello inizia a ripetere il soggetto. La proporzione `"auto"` funziona solo entro il limite di area 2K, quindi a 4K scegli una proporzione esplicita oppure usa `"custom"`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine modificata prodotta dalle immagini di riferimento e dal prompt. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageEditApi/it.md)

---
**Source fingerprint (SHA-256):** `46c112347b51a2983521f87bbeb047289515f4073c48ba5d909fd3bae4597633`

# HunyuanImageTextToImageApi

Il nodo Tencent HY Image: Text to Image genera un'immagine da una descrizione testuale con il modello Hunyuan Image di Tencent. Il prompt viene inviato all'API, che lo riscrive e lo espande prima del rendering, e l'immagine finale viene restituita come batch di immagini.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello utilizzato per la generazione. Il modello selezionato determina quali input aggiuntivi vengono mostrati. | DYNAMIC_COMBO | Sì | `"hy-image-3.5-preview"` |

### Input di hy-image-3.5-preview

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrive l'immagine da generare. Il modello lo riscrive e lo espande prima del rendering. Non deve essere vuoto (predefinito: vuoto). | STRING | Sì | Qualsiasi testo |
| `aspect_ratio` | Rapporto d'aspetto dell'output. `"auto"` lascia che il modello scelga il rapporto dal prompt e non è disponibile a 4K. Ignorato quando `resolution` è `"custom"`. | COMBO | Sì | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"` (predefinito: `"auto"`) |
| `resolution` | Area in pixel dell'immagine: 1K è circa 1024x1024, 2K circa 2048x2048 e 4K circa 4096x4096. Qualsiasi valore superiore a 2K viene renderizzato a 2K e ingrandito dal modello. Impostare su `"custom"` per usare `width` e `height` invece di un'area preimpostata. | COMBO | Sì | `"1K"`<br>`"2K"`<br>`"4K"`<br>`"custom"` (predefinito: `"2K"`) |
| `width` | Larghezza dell'immagine in pixel. Usata solo quando `resolution` è `"custom"`. | INT | Sì | 256-8192, incrementi di 16 (predefinito: 2048) |
| `height` | Altezza dell'immagine in pixel. Usata solo quando `resolution` è `"custom"`. | INT | Sì | 256-8192, incrementi di 16 (predefinito: 2048) |
| `seed` | Seed utilizzato per la generazione. I risultati variano comunque tra esecuzioni con lo stesso seed. | INT | Sì | 0-2147483647 (predefinito: 42) |
| `watermark` | Indica se aggiungere una filigrana generata dall'IA al risultato. Questo è un parametro avanzato. | BOOLEAN | No | true<br>false (predefinito: false) |

`prompt` non deve essere vuoto. Con la risoluzione `"custom"`, `width` e `height` devono entrambi essere multipli di 16 e il loro prodotto non deve superare il limite di area di 4096 x 4096 pixel (circa 16,7 megapixel); qualsiasi rapporto d'aspetto va bene, anche se oltre circa 6:1 il modello inizia a ripetere il soggetto. Il rapporto d'aspetto `"auto"` richiede che il modello scelga una dimensione, quindi funziona solo entro il limite di area 2K: a 4K, scegli un rapporto d'aspetto esplicito o usa `"custom"`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `IMAGE` | L'immagine generata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageTextToImageApi/it.md)

---
**Source fingerprint (SHA-256):** `1d4e70d688c5aa4e79b81447da559e201078454077da34769f2a4f544fbba63f`

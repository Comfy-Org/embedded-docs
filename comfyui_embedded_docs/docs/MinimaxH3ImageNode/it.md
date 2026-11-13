# MiniMax H3 Image

Genera immagini da testo con MiniMax H3 Image oppure modifica e combina fino a 16 immagini di riferimento. Il prompt fa riferimento alle immagini tramite l'ordine di connessione: `@Image1`, `@Image2` e così via.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | `MiniMax-H3-Image` oppure `MiniMax-H3-Image-Highspeed` per esecuzioni più rapide. Predefinito: `"MiniMax-H3-Image"`. | COMBO | Sì | `"MiniMax-H3-Image"`<br>`"MiniMax-H3-Image-Highspeed"` |
| `prompt` | Cosa generare o come modificare le immagini di riferimento. Con immagini di riferimento collegate, può contenere al massimo 8.000 caratteri. Predefinito: vuoto. | STRING | Sì | 1 a 8000 caratteri |
| `size` | `2K` e `4K` derivano la dimensione da un rapporto d'aspetto; `custom` imposta larghezza e altezza esatte. Predefinito: `"2K"`. | DYNAMIC_COMBO | Sì | `"2K"`<br>`"4K"`<br>`"custom"` |
| `enhance_prompt` | MiniMax riscrive il prompt in una descrizione dettagliata della scena prima di generare. Le modifiche alle immagini vengono sempre migliorate. Quando è disattivato, scegli un rapporto d'aspetto fisso o una dimensione personalizzata. Predefinito: true. | BOOLEAN | No | true<br>false |
| `seed` | Controlla se il nodo viene rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | No | 0 a 2147483647 |
| `images` | Immagini di riferimento da modificare o combinare, a cui si fa riferimento nel prompt come `@Image1` fino a `@Image16` nell'ordine di connessione. | AUTOGROW | No | Fino a 16 immagini |

### Input per le dimensioni "2K" e "4K"

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Con `auto`, MiniMax sceglie il rapporto dal prompt oppure segue l'immagine di riferimento quando ne è collegata una. La generazione da testo a immagine con `enhance_prompt` disattivato richiede un rapporto fisso. Predefinito: `"auto"`. | COMBO | Sì | Più opzioni disponibili |

### Input per la dimensione "custom"

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `width` | Larghezza di output in pixel. Predefinito: 2048. | INT | Sì | 512 a 7680 (passo 16) |
| `height` | Altezza di output in pixel. Predefinito: 2048. | INT | Sì | 512 a 7680 (passo 16) |

Nota: per una dimensione personalizzata, il prodotto tra larghezza e altezza deve essere compreso tra 655.360 e 20.000.000 pixel, con un rapporto d'aspetto massimo di 3:1.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine generata o modificata, in formato PNG. | IMAGE |
| `revised_prompt` | Il prompt riscritto utilizzato da MiniMax, quando il miglioramento del prompt era attivo. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxH3ImageNode/it.md)

---
**Source fingerprint (SHA-256):** `723eb4c2d3b303ece041f98bd5b773c669affb9a7b3da0c08ffcac4ee89f8e11`

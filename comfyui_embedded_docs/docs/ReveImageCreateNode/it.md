# ReveImageCreateNode

Il nodo Reve Image Create genera immagini da una descrizione testuale utilizzando il modello Reve AI. Invia il prompt all'API di Reve e restituisce l'immagine risultante, con post-elaborazione opzionale per l'upscaling e la rimozione dello sfondo. Questo nodo è deprecato.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Versione del modello da utilizzare per la generazione. | DYNAMIC_COMBO | Sì | `"reve-create@20250915"` |
| `prompt` | Descrizione testuale dell'immagine desiderata. Massimo 2560 caratteri. Predefinito: "" (vuoto). | STRING | Sì | Da 1 a 2560 caratteri |
| `upscale` | Esegue l'upscaling dell'immagine generata. Può comportare un costo aggiuntivo. Predefinito: "disabled". | DYNAMIC_COMBO | No | `"disabled"`<br>`"enabled"` |
| `remove_background` | Rimuove lo sfondo dall'immagine generata. Può comportare un costo aggiuntivo. Predefinito: False. | BOOLEAN | No | N/D |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 0. | INT | No | Da 0 a 2147483647 |

### Input di reve-create@20250915

Opzioni disponibili quando `model` è impostato su `"reve-create@20250915"`:

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Rapporto d'aspetto dell'immagine di output. | COMBO | Sì | `"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Valori più alti producono immagini migliori ma costano più crediti. Predefinito: 1. Opzione avanzata. | INT | No | Da 1 a 5 |

### Input di upscaling

Opzioni disponibili quando `upscale` è impostato su `"enabled"`:

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `upscale_factor` | Fattore di upscaling (2x, 3x o 4x). Predefinito: 2. | INT | No | Da 2 a 4 |

**Nota:** Il parametro `prompt` deve contenere tra 1 e 2560 caratteri. L'input `upscale_factor` compare solo quando `upscale` è impostato su `"enabled"`. Il parametro `seed` non garantisce output deterministici — i risultati non sono deterministici indipendentemente dal valore del seed. Sia `upscale` che `remove_background` possono comportare un costo aggiuntivo.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine generata dal modello Reve in base al prompt di input. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/it.md)

---
**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`

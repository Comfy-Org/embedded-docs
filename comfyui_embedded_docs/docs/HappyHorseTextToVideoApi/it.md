# HappyHorse Testo in Video

Genera un video basato su un prompt testuale utilizzando il modello HappyHorse. Questo nodo invia il prompt e le impostazioni all'API HappyHorse, attende che il video venga generato e quindi scarica il risultato.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello HappyHorse utilizzato per la generazione, insieme ai relativi sotto-parametri. La selezione di un modello determina quali sotto-parametri sono disponibili (vedere le sezioni dei modelli di seguito). | DYNAMIC_COMBO | Sì | "happyhorse-1.1-t2v"<br>"happyhorse-1.0-t2v" |
| `seed` | Seed da utilizzare per la generazione. Utilizzando lo stesso seed con gli stessi input si otterrà lo stesso risultato. (predefinito: 0). | INT | Sì | 0 a 2147483647 |
| `watermark` | Indica se aggiungere una filigrana generata dall'IA al risultato. (predefinito: False). | BOOLEAN | Sì | True / False |

### Input di happyhorse-1.1-t2v

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt che descrive gli elementi e le caratteristiche visive. Supporta l'inglese e il cinese. (predefinito: ""). | STRING | Sì | - |
| `resolution` | La risoluzione del video di output. | COMBO | Sì | "720P"<br>"1080P" |
| `ratio` | Il rapporto d'aspetto del video di output. | COMBO | Sì | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9"<br>"9:21"<br>"5:4"<br>"4:5" |
| `duration` | La durata del video in secondi. (predefinito: 5, min: 3, max: 15, passo: 1). | INT | Sì | 3 a 15 |

### Input di happyhorse-1.0-t2v

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt che descrive gli elementi e le caratteristiche visive. Supporta l'inglese e il cinese. (predefinito: ""). | STRING | Sì | - |
| `resolution` | La risoluzione del video di output. | COMBO | Sì | "720P"<br>"1080P" |
| `ratio` | Il rapporto d'aspetto del video di output. | COMBO | Sì | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | La durata del video in secondi. (predefinito: 5, min: 3, max: 15, passo: 1). | INT | Sì | 3 a 15 |

Nota: il prompt non deve essere vuoto; viene generato un errore se non viene fornito alcun prompt. Entrambi i modelli supportano durate video da 3 a 15 secondi. Il modello `happyhorse-1.1-t2v` offre rapporti d'aspetto aggiuntivi (`21:9`, `9:21`, `5:4`, `4:5`) non disponibili con `happyhorse-1.0-t2v`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `VIDEO` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/it.md)

---
**Source fingerprint (SHA-256):** `b60cfc3ce4935d7eb36bb28f9bd268446c4df5b437e06278b7e6d91d349d0238`

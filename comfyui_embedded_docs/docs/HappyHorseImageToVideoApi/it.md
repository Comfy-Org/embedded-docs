# HappyHorseImageToVideoApi

Questo nodo genera un breve video a partire da una singola immagine iniziale utilizzando il modello HappyHorse. Si fornisce un'immagine del primo fotogramma e un prompt testuale che descrive il movimento e la scena desiderati; il nodo crea un video che continua da quell'immagine.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello HappyHorse da utilizzare per la generazione del video. | DYNAMIC_COMBO | Sì | `"happyhorse-1.1-i2v"`<br>`"happyhorse-1.0-i2v"` |
| `first_frame` | Immagine del primo fotogramma. Il rapporto d'aspetto dell'output viene derivato da questa immagine. | IMAGE | Sì | min 300×300 px; da 1:2.5 a 2.5:1 |
| `seed` | Seed da utilizzare per la generazione. (predefinito: 0) | INT | Sì | da 0 a 2147483647 |
| `watermark` | Indica se aggiungere una filigrana generata dall'IA al risultato. (opzione avanzata; predefinito: False) | BOOLEAN | Sì | True / False |

### Input di happyhorse-1.1-i2v e happyhorse-1.0-i2v

Entrambe le versioni del modello condividono lo stesso insieme di parametri.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt che descrive gli elementi e le caratteristiche visive. Supporta l'inglese e il cinese. (predefinito: "") | STRING | No | N/D |
| `resolution` | La risoluzione del video di output. (predefinito: `"720P"`) | COMBO | Sì | `"720P"`<br>`"1080P"` |
| `duration` | La durata del video generato in secondi. (predefinito: 5) | INT | Sì | da 3 a 15 |

Nota: l'immagine `first_frame` deve essere di almeno 300x300 pixel e il suo rapporto d'aspetto deve essere compreso tra 1:2.5 e 2.5:1.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/it.md)

---
**Source fingerprint (SHA-256):** `4bf6eece0d1b4104ce2d84e29b2c918a0a6ba782da1dd801b66cbfa1666d150b`

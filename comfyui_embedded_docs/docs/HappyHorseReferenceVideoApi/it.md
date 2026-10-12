# HappyHorse Riferimento in Video

Questo nodo genera un video che ritrae una persona o un oggetto a partire da immagini di riferimento utilizzando il modello HappyHorse. Supporta performance con un singolo personaggio e interazioni tra più personaggi. Le immagini di riferimento vengono caricate e utilizzate per rappresentare i personaggi nel video generato.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello HappyHorse reference-to-video da utilizzare per la generazione. | DYNAMIC_COMBO | Sì | `"happyhorse-1.1-r2v"`<br>`"happyhorse-1.0-r2v"` |
| `seed` | Seed da utilizzare per la generazione (predefinito: 0). Può essere impostato per cambiare automaticamente dopo ogni generazione. | INT | Sì | 0 a 2147483647 |
| `watermark` | Indica se aggiungere una filigrana generata dall'IA al risultato (predefinito: False). | BOOLEAN | Sì | True o False |

### Input di HappyHorse 1.1 (happyhorse-1.1-r2v)

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt che descrive il video. Usa identificatori come 'character1' e 'character2' per fare riferimento ai personaggi di riferimento. | STRING | Sì | N/A |
| `resolution` | La risoluzione del video generato. | COMBO | Sì | `"720P"`<br>`"1080P"` |
| `ratio` | Il rapporto d'aspetto del video generato. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"`<br>`"5:4"`<br>`"4:5"` |
| `duration` | La durata del video generato in secondi (predefinito: 5). | INT | Sì | 3 a 15 |

### Input di HappyHorse 1.0 (happyhorse-1.0-r2v)

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt che descrive il video. Usa identificatori come 'character1' e 'character2' per fare riferimento ai personaggi di riferimento. | STRING | Sì | N/A |
| `resolution` | La risoluzione del video generato. | COMBO | Sì | `"720P"`<br>`"1080P"` |
| `ratio` | Il rapporto d'aspetto del video generato. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | La durata del video generato in secondi (predefinito: 5). | INT | Sì | 3 a 15 |

### Input di riferimento

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot espandibile: collega da 1 a 9 immagini di riferimento della persona o dell'oggetto da inserire nel video. È necessario fornire almeno un'immagine di riferimento. | IMAGE | Sì | 1 a 9 (per modello) |

Nota: è necessario fornire almeno un'immagine di riferimento, altrimenti il nodo genera un errore. Ogni immagine di riferimento deve essere di almeno 400 x 400 pixel e avere un rapporto d'aspetto compreso tra 1:2.5 e 2.5:1. Il prompt non deve essere vuoto.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `VIDEO` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/it.md)

---
**Source fingerprint (SHA-256):** `252c918afc4cf38be9c7d09b7112075b9adb23490ec9fed1717a8548519d2554`

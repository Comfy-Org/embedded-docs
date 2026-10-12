# GrokVideoReferenceNode

Il nodo Grok Reference-to-Video genera un video da un prompt testuale, utilizzando fino a sette immagini di riferimento per guidare lo stile e il contenuto dell'output. Con il modello `grok-imagine-video-1.5`, puoi anche allegare fino a tre riferimenti vocali preimpostati e fare riferimento a immagini e voci direttamente nel prompt usando i tag `@ImageN` e `@AudioN`. Il nodo invia la richiesta a un'API esterna, attende il completamento della generazione e scarica il video risultante.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello da usare per la generazione del video. | DYNAMIC_COMBO | Sì | `"grok-imagine-video-1.5"`<br>`"grok-imagine-video"` |
| `prompt` | Descrizione testuale del video desiderato. Deve essere una stringa non vuota. | STRING | Sì | N/A |
| `seed` | Seme per determinare se il nodo deve essere rieseguito; i risultati effettivi sono non deterministici indipendentemente dal seme (predefinito: 0). | INT | Sì | da 0 a 2147483647 |

### Input di Grok Imagine Video 1.5

Disponibili quando `model` è impostato su `grok-imagine-video-1.5`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `voice_1` | Riferimento vocale preimpostato opzionale; fai riferimento ad esso nel prompt come @Audio1. L'API supporta solo queste voci preimpostate, non audio personalizzato (predefinito: none). | COMBO | No | Opzioni vocali preimpostate, che includono `"none"` |
| `voice_2` | Secondo riferimento vocale opzionale; @Audio2 nel prompt (predefinito: none). | COMBO | No | Opzioni vocali preimpostate, che includono `"none"` |
| `voice_3` | Terzo riferimento vocale opzionale; @Audio3 nel prompt (predefinito: none). | COMBO | No | Opzioni vocali preimpostate, che includono `"none"` |
| `resolution` | La risoluzione del video di output. | COMBO | Sì | `"480p"`<br>`"720p"` |
| `aspect_ratio` | Il rapporto d'aspetto del video di output. | COMBO | Sì | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | La durata del video di output in secondi (predefinito: 6). | INT | Sì | da 1 a 15 |

### Input di Grok Imagine Video

Disponibili quando `model` è impostato su `grok-imagine-video`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `resolution` | La risoluzione del video di output. | COMBO | Sì | `"480p"`<br>`"720p"` |
| `aspect_ratio` | Il rapporto d'aspetto del video di output. | COMBO | Sì | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | La durata del video di output in secondi (predefinito: 6). | INT | Sì | da 2 a 10 |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reference_images` | Slot espandibile: collega da 1 a 7 immagini di riferimento per guidare la generazione del video. Con `grok-imagine-video-1.5`, fai riferimento ad esse nel prompt come @Image1 ... @Image7, numerate nell'ordine di input; un input in batch conta una volta per immagine. | IMAGE | Sì | da 1 a 7 immagini |

**Nota:** I sotto-parametri mostrati dipendono dal `model` selezionato; `grok-imagine-video-1.5` aggiunge gli input `voice_1`, `voice_2` e `voice_3`. È richiesta almeno un'immagine di riferimento, e il totale è limitato a 7 (un input in batch conta una volta per immagine). Con `grok-imagine-video-1.5`, il prompt può fare riferimento alle immagini collegate come `@Image1` ... `@Image7` e agli slot vocali come `@Audio1`, `@Audio2`, `@Audio3`; un `@image` o `@audio` non numerato fa riferimento al primo. `@AudioN` fa riferimento al widget `voice_N`, non all'ordine delle voci abilitate. Fare riferimento a un'immagine non collegata o a uno slot vocale impostato su `none` causa un errore. L'API supporta solo voci preimpostate, non audio personalizzato.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/it.md)

---
**Source fingerprint (SHA-256):** `e584c450563eaa7fcb7751d2325f9ef847fa34a4342df01f2bd9ce2e4ff8f2c3`

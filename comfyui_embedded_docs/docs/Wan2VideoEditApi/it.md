# Wan 2.7 Modifica Video

Il nodo Wan 2.7 Video Edit modifica un video utilizzando istruzioni testuali, immagini di riferimento o trasferimento di stile. Invia il video di input (più eventuali immagini di riferimento) al servizio di modifica video Wan 2.7 e restituisce un video appena generato in base alle impostazioni scelte di risoluzione, rapporto d'aspetto e durata.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello da utilizzare per la modifica video. Ogni opzione espone il proprio insieme di sottoparametri. | DYNAMIC_COMBO | Sì | `"wan2.7-videoedit"` |
| `video` | Il video da modificare. | VIDEO | Sì | - |
| `seed` | Seed da utilizzare per la generazione. (predefinito: 0) | INT | Sì | da 0 a 2147483647 |
| `audio_setting` | 'auto': il modello decide se rigenerare l'audio in base al prompt. 'origin': conserva l'audio originale dal video di input. (predefinito: "auto") | COMBO | Sì | `"auto"`<br>`"origin"` |
| `watermark` | Indica se aggiungere una filigrana generata dall'IA al risultato. (predefinito: False) | BOOLEAN | Sì | - |

### Input di wan2.7-videoedit

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Istruzioni di modifica o requisiti di trasferimento di stile. (predefinito: stringa vuota) | STRING | Sì | - |
| `resolution` | La risoluzione del video di output. | COMBO | Sì | `"720P"`<br>`"1080P"` |
| `ratio` | Rapporto d'aspetto. Se non viene modificato, approssima il rapporto d'aspetto del video di input. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Durata di output in secondi. 'auto' corrisponde alla durata del video di input. Un valore specifico tronca dall'inizio del video. (predefinito: "auto") | COMBO | Sì | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reference_images` | Slot espandibile: collega da 0 a 4 immagini (`image1`...`image4`) per guidare la modifica. Il numero massimo è 4 per il modello wan2.7-videoedit. | IMAGE | No | da 0 a 4 elementi |

**Vincoli:**
*   `audio_setting` e `watermark` sono opzioni avanzate.
*   Il `prompt` deve contenere almeno 1 carattere.
*   Il `video` di input deve avere una durata compresa tra 2 e 10 secondi.
*   Lo slot espandibile `reference_images` accetta un massimo di 4 immagini.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il video modificato generato dal modello. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/it.md)

---
**Source fingerprint (SHA-256):** `27283273ee56c90903db103a3e9bc17dc4df0914676c9aedd2a115b07937dc10`

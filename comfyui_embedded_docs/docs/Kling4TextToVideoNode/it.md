# Kling 4.0 da testo a video

Genera un video da un prompt testuale con il modello Kling 4.0, inclusi i contenuti audio. Questo nodo invia il prompt e le impostazioni di generazione all'API Kling, attende il completamento dell'attività e restituisce il video finito. Usalo quando è necessario creare una clip solo da una descrizione, senza media di riferimento.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Selettore del modello. `"kling-4.0"` supporta fino a 4K HDR e 30 secondi; `"kling-4.0-flash"` è limitato a 720p e 20 secondi. Selezionando un modello vengono mostrati i relativi input di seguito. | DYNAMIC_COMBO | Sì | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Input di kling-4.0

Questi input vengono visualizzati quando `model` è impostato su `"kling-4.0"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrizione testuale del video da generare. Deve essere compresa tra 1 e 26000 caratteri. | STRING | Sì | 1 a 26000 caratteri |
| `resolution` | Risoluzione del video in output; un'opzione con `HDR` nel nome restituisce un video HDR. Predefinito: `"720p"`. | COMBO | Sì | `"720p"`<br>`"1080p"`<br>`"4k"`<br>`"1080p HDR"`<br>`"4k HDR"` |
| `aspect_ratio` | Proporzioni del video in output. Predefinito: `"16:9"`. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Durata del video generato in secondi. Predefinito: 5. | INT | Sì | 3 a 30 |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

### Input di kling-4.0-flash

Questi input vengono visualizzati quando `model` è impostato su `"kling-4.0-flash"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrizione testuale del video da generare. Deve essere compresa tra 1 e 26000 caratteri. | STRING | Sì | 1 a 26000 caratteri |
| `resolution` | Risoluzione del video in output. Flash esegue il rendering solo a 720p. Predefinito: `"720p"`. | COMBO | Sì | `"720p"` |
| `aspect_ratio` | Proporzioni del video in output. Predefinito: `"16:9"`. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Durata del video generato in secondi. Predefinito: 5. | INT | Sì | 3 a 20 |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `video` | Il video generato, scaricato dal provider una volta completata l'attività. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4TextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `7a5d99aa6f5fdb923ce9e2c89f64e92d46fad14d28002a033ddedc24c7d27894`

# Kling 4.0 da testo a video

Genera un video da un prompt testuale con il modello Kling 4.0, includendo l'audio. Questo nodo invia il prompt e le impostazioni di generazione all'API Kling, attende il completamento dell'attività e restituisce il video finito. Usalo quando occorre creare una clip solo da una descrizione, senza contenuti multimediali di riferimento.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `modello` | Selettore del modello. `"kling-4.0"` supporta fino a 1080p e 30 secondi; `"kling-4.0-flash"` è limitato a 720p e 20 secondi. La selezione di un modello mostra i relativi input di seguito. | DYNAMIC_COMBO | Sì | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Input di kling-4.0

Questi input compaiono quando `model` è impostato su `"kling-4.0"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Descrizione testuale del video da generare. Deve contenere da 1 a 26000 caratteri. | STRING | Sì | Da 1 a 26000 caratteri |
| `resolution` | Risoluzione del video di output. Predefinito: `"720p"`. | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Rapporto d'aspetto del video di output. Predefinito: `"16:9"`. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Durata del video generato in secondi. Predefinito: 5. | INT | Sì | Da 3 a 30 |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | Da 0 a 2147483647 |

### Input di kling-4.0-flash

Questi input compaiono quando `model` è impostato su `"kling-4.0-flash"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Descrizione testuale del video da generare. Deve contenere da 1 a 26000 caratteri. | STRING | Sì | Da 1 a 26000 caratteri |
| `resolution` | Risoluzione del video di output. Flash esegue il rendering solo a 720p. Predefinito: `"720p"`. | COMBO | Sì | `"720p"` |
| `aspect_ratio` | Rapporto d'aspetto del video di output. Predefinito: `"16:9"`. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Durata del video generato in secondi. Predefinito: 5. | INT | Sì | Da 3 a 20 |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | Da 0 a 2147483647 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video generato, scaricato dal provider al completamento dell'attività. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4TextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `3e37f976f48488c3accb4efb0d876d12c316796023eb9c28b9209cb2188249e2`

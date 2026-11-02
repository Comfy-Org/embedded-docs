# Kling 4.0 Text to Video

Genera un video da un prompt testuale con il modello Kling 4.0, inclusi i contenuti audio. Questo nodo invia il prompt e le impostazioni di generazione all'API Kling, attende il completamento dell'attività e restituisce il video finito. Usalo quando è necessario creare una clip solo da una descrizione, senza media di riferimento.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Selettore del modello. È disponibile solo `"kling-4.0"`; selezionandolo vengono mostrati gli input seguenti. | DYNAMIC_COMBO | Sì | `"kling-4.0"` |

### Input di kling-4.0

Questi input vengono visualizzati quando `model` è impostato su `"kling-4.0"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Descrizione testuale del video da generare. Deve contenere da 1 a 26000 caratteri. | STRING | Sì | da 1 a 26000 caratteri |
| `resolution` | Risoluzione del video in output. Predefinito: `"720p"`. | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Proporzioni del video in output. Predefinito: `"16:9"`. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Durata del video generato in secondi. Predefinito: 5. | INT | Sì | da 3 a 30 |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | da 0 a 2147483647 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video generato, scaricato dal provider una volta completata l'attività. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4TextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `3835dcb7d83d843ea7f6c5dc691b48759d9c3e7a7baeead3d0f92817e73d6079`

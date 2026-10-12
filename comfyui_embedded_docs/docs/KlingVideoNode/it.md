# Kling 3.0 Video

Questo nodo genera video con il modello Kling V3. Supporta la generazione da testo a video (text-to-video), in cui un video viene creato da una descrizione testuale, e da immagine a video (image-to-video), in cui un'immagine esistente viene animata. Può anche creare video multi-segmento utilizzando prompt storyboard e, opzionalmente, generare audio.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `multi_shot` | Genera una serie di segmenti video con prompt e durate individuali. Quando è impostato su un'opzione storyboard, compaiono input aggiuntivi per il prompt e la durata di ciascuno storyboard. | DYNAMIC_COMBO | Sì | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Quando è abilitato, il nodo genera l'audio per il video. Nota: `"kling-3.0-turbo"` genera sempre audio nativo, quindi l'interruttore audio viene ignorato per quel modello. Il valore predefinito è True. | BOOLEAN | Sì | True<br>False |
| `model` | Modello e impostazioni di generazione. Selezionando un modello vengono rivelati i relativi sotto-parametri di risoluzione e rapporto d'aspetto. | DYNAMIC_COMBO | Sì | `"kling-v3"`<br>`"kling-3.0-turbo"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Il valore predefinito è 0. | INT | Sì | da 0 a 2147483647 |
| `start_frame` | Immagine del frame iniziale opzionale. Quando è collegata, passa alla modalità da immagine a video. | IMAGE | No | - |

### Input di kling-v3

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model.resolution` | La risoluzione per il video generato. Il valore predefinito è `"1080p"`. | COMBO | Sì | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `model.aspect_ratio` | Il rapporto d'aspetto per il video generato. Ignorato in modalità da immagine a video. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Input di kling-3.0-turbo

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model.resolution` | La risoluzione per il video generato. Il valore predefinito è `"720p"`. | COMBO | Sì | `"1080p"`<br>`"720p"` |
| `model.aspect_ratio` | Il rapporto d'aspetto per il video generato. Ignorato in modalità da immagine a video. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Input multi-shot

**Quando `multi_shot` è impostato su `"disabled"`:**

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | La descrizione testuale principale per il video. Deve essere compresa tra 1 e 2500 caratteri. | STRING | Sì | da 1 a 2500 caratteri |
| `negative_prompt` | Testo che descrive ciò che non deve apparire nel video. Può essere lasciato vuoto. | STRING | No | - |
| `duration` | La durata del video in secondi. Il valore predefinito è 5. | INT | Sì | da 3 a 15 |

**Quando `multi_shot` è impostato su un'opzione storyboard (ad es. `"3 storyboards"`):**

Per ogni segmento storyboard N (da 1 fino al numero di storyboard selezionato), compaiono i seguenti input:

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `storyboard_N_prompt` | Prompt per il segmento storyboard N. Massimo 512 caratteri. | STRING | Sì | da 1 a 512 caratteri |
| `storyboard_N_duration` | Durata per il segmento storyboard N in secondi. Il valore predefinito è 4. | INT | Sì | da 1 a 15 |

**Vincoli e comportamento:**

- La modalità da testo a video viene utilizzata quando `start_frame` non è collegato; la modalità da immagine a video viene utilizzata quando `start_frame` è collegato. In modalità da immagine a video, `model.aspect_ratio` viene ignorato e l'immagine di input deve essere di almeno 300x300 pixel con un rapporto d'aspetto compreso tra 1:2.5 e 2.5:1.
- In modalità storyboard, il `prompt` principale e `negative_prompt` non vengono utilizzati. La somma totale di tutte le durate degli storyboard deve essere compresa tra 3 e 15 secondi.
- `negative_prompt` viene utilizzato solo con `kling-v3`; viene ignorato quando è selezionato `kling-3.0-turbo`.
- Per `kling-v3`, ogni storyboard viene inviato all'API come segmento separato. Per `kling-3.0-turbo`, i prompt e le durate degli storyboard vengono combinati in un singolo prompt multi-shot.
- Per `kling-3.0-turbo`, `generate_audio` viene ignorato perché questo modello genera sempre audio nativo.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `video` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `2863d7a971a1978b6009e5321ed2112a9c04809281acd5f65d85ab72c4b49f08`

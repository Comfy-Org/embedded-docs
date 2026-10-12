# Vidu3ImageToVideoNode

Il nodo Vidu Q3 Image-to-Video Generation crea una sequenza video partendo da un'immagine di input. Utilizza un modello Vidu Q3 per animare l'immagine, facoltativamente guidata da un prompt testuale, e restituisce in output un file video.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modello da utilizzare per la generazione del video. | DYNAMIC_COMBO | Sì | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `image` | Un'immagine da utilizzare come fotogramma iniziale del video generato. | IMAGE | Sì | - |
| `prompt` | Un prompt testuale facoltativo per la generazione del video (max 2000 caratteri) (predefinito: vuoto). | STRING | Sì | - |
| `seed` | Il valore seed utilizzato per controllare la casualità della generazione (predefinito: 1). | INT | Sì | da 0 a 2147483647 |

### Input di viduq3-pro

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Risoluzione del video in output. | COMBO | Sì | `"720p"`<br>`"1080p"`<br>`"2K"` |
| `duration` | Durata del video in output in secondi (predefinito: 5). | INT | Sì | da 1 a 16 |
| `audio` | Se abilitato, produce video con audio (inclusi dialoghi ed effetti sonori) (predefinito: False). | BOOLEAN | Sì | `True`<br>`False` |

### Input di viduq3-turbo

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Risoluzione del video in output. | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `duration` | Durata del video in output in secondi (predefinito: 5). | INT | Sì | da 1 a 16 |
| `audio` | Se abilitato, produce video con audio (inclusi dialoghi ed effetti sonori) (predefinito: False). | BOOLEAN | Sì | `True`<br>`False` |

**Nota:** Il parametro `image` deve avere un rapporto d'aspetto compreso tra 1:4 e 4:1 (da verticale a orizzontale). Il `prompt` è facoltativo ma non può superare i 2000 caratteri. Le opzioni `resolution` disponibili dipendono dal modello selezionato: `"viduq3-pro"` supporta `"720p"`, `"1080p"` e `"2K"`; `"viduq3-turbo"` supporta `"720p"` e `"1080p"`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3ImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `77500d1e19928128decc010540670e311cd8ec4fcad913412517f47f0e27e15f`

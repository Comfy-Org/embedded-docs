# PixverseImageToVideoNode

Genera un video da un'immagine fissa e un prompt testuale utilizzando PixVerse. Il nodo carica l'immagine di input, applica le impostazioni di qualità, durata e movimento selezionate, quindi restituisce il video risultante una volta completata la generazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | Immagine di input da trasformare in video | IMAGE | Sì | - |
| `prompt` | Prompt per la generazione del video (predefinito: stringa vuota) | STRING | Sì | - |
| `quality` | Impostazione della qualità video (predefinito: res_540p) | COMBO | Sì | `res_540p`<br>`res_1080p` |
| `duration_seconds` | Durata del video generato in secondi | COMBO | Sì | `dur_2`<br>`dur_5`<br>`dur_10` |
| `motion_mode` | Stile di movimento applicato alla generazione del video | COMBO | Sì | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` |
| `seed` | Seed per la generazione del video (predefinito: 0) | INT | Sì | 0-2147483647 |
| `negative_prompt` | Descrizione testuale opzionale di elementi indesiderati in un'immagine (predefinito: stringa vuota) | STRING | No | - |
| `pixverse_template` | Template opzionale per influenzare lo stile di generazione, creato dal nodo PixVerse Template | CUSTOM | No | - |

**Nota:** Quando si utilizza la qualità 1080p, la modalità di movimento viene automaticamente impostata su normal e la durata è limitata a 5 secondi. Per durate diverse da 5 secondi, anche la modalità di movimento viene automaticamente impostata su normal.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `output` | Video generato in base all'immagine di input e ai parametri | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `93ea662a27159f55bf12e49ea230f0005813614ad07f5189d1fd61e7b937fd4b`

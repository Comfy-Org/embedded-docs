# LtxApi25ImageToVideo

Questo nodo genera un video di qualità professionale a partire da un'immagine iniziale utilizzando un modello LTX 2.5. Descrivi il contenuto del video con un prompt testuale, selezioni una variante del modello e regoli durata, risoluzione, frequenza dei fotogrammi e generazione audio. È possibile fornire un fotogramma finale opzionale per definire la fine del video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | Fotogramma iniziale da utilizzare per il video. | IMAGE | Sì | Esattamente un'immagine |
| `model` | Gruppo di impostazioni del modello. Seleziona la variante del modello LTX 2.5 da utilizzare. | COMBO | Sì | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `model.duration` | Durata del video generato in secondi. | INT | Sì | Intero |
| `model.resolution` | Risoluzione del video generato. Le opzioni disponibili possono dipendere dal modello selezionato. | COMBO | Sì | "1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840" |
| `model.fps` | Frequenza dei fotogrammi del video generato. | INT | Sì | Intero (predefinito: 25) |
| `model.generate_audio` | Indica se generare l'audio per il video. | BOOLEAN | Sì | True<br>False (predefinito: True) |
| `prompt` | Descrizione testuale del contenuto video da generare. Deve contenere da 1 a 10000 caratteri. | STRING | Sì | Da 1 a 10000 caratteri |
| `seed` | Valore di seed per una generazione riproducibile. Usare lo stesso seed con le stesse impostazioni produce lo stesso risultato. | INT | Sì | Intero (predefinito: 42) |
| `last_frame` | Fotogramma finale da utilizzare per il video. | IMAGE | No | Esattamente un'immagine |

**Nota:** Per `image` è supportata una sola immagine. Se viene fornito `last_frame`, deve contenere anch'esso esattamente un'immagine. Le opzioni disponibili per `model.resolution` possono variare in base alla variante di `model` selezionata. Il costo di un'esecuzione dipende da `model`, `model.duration` e `model.resolution` selezionati.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Il video generato in base all'immagine iniziale fornita e alle impostazioni di generazione. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25ImageToVideo/it.md)

---
**Source fingerprint (SHA-256):** `13db42e5e0d4237424b30b960ec12f5dd16808d21b85e100e5861c095b351c79`

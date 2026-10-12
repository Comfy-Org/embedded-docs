# KlingOmniProEditVideoNode

Il nodo Kling Omni Edit Video (Pro) utilizza un modello di IA per modificare un video esistente basandosi su una descrizione testuale. Fornisci un video sorgente e un prompt, e il nodo genera un nuovo video della stessa durata con le modifiche richieste. Può facoltativamente utilizzare immagini di riferimento per guidare lo stile e mantenere l'audio originale dal video sorgente.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_name` | Il modello di IA da utilizzare per la modifica video (predefinito: `"kling-v3-omni"`). | COMBO | Sì | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Un prompt testuale che descrive il contenuto del video. Può includere sia descrizioni positive che negative. | STRING | Sì |  |
| `video` | Video da modificare. La durata del video di output sarà la stessa. | VIDEO | Sì |  |
| `keep_original_sound` | Determina se l'audio originale del video di input viene mantenuto nell'output (predefinito: True). | BOOLEAN | Sì |  |
| `reference_images` | Fino a 4 immagini di riferimento aggiuntive. | IMAGE | No |  |
| `resolution` | La risoluzione per il video di output (predefinito: `"1080p"`). | COMBO | No | `"1080p"`<br>`"720p"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed (predefinito: 0). | INT | No | da 0 a 2147483647 |

**Vincoli e limitazioni:**

* Il `prompt` deve essere lungo tra 1 e 2500 caratteri.
* Il `video` di input deve avere una durata compresa tra 3,0 e 10,05 secondi.
* Le dimensioni del `video` di input devono essere comprese tra 720x720 e 2160x2160 pixel.
* È possibile fornire un massimo di 4 `reference_images` quando viene utilizzato un video.
* Ogni `reference_image` deve essere di almeno 300x300 pixel.
* Ogni `reference_image` deve avere un rapporto d'aspetto compreso tra 1:2,5 e 2,5:1.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video modificato generato dal modello di IA. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProEditVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `4aa7779a30183c80f025e15ae693ba23021013c68d247753e7e9a4c3a64762da`

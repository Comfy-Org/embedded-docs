# Vidu4ReferenceVideoNode

Genera un video da immagini di riferimento, audio di riferimento opzionale e un prompt con un modello Vidu Q4. Questa è la variante reference-to-video dei nodi di generazione Vidu Q4.

Selezionando un `model` vengono rivelati i parametri specifici di quel modello.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare per la generazione video. Selezionando un modello vengono rivelati i parametri specifici: `reference_images`, `reference_audios`, `prompt`, `aspect_ratio`, `resolution`, `duration`, `audio` e `seed`. | DYNAMIC_COMBO | Sì | `"Vidu Q4 Preview"` |
| `reference_images` | Slot espandibile: collega una o più immagini di riferimento (`image_1`, `image_2`, ...) per il video generato; ogni immagine di un batch conta ai fini del totale. Riferisciti a esse nel prompt in ordine: immagine 1, immagine 2, e così via. | IMAGE | Sì | Fino a 15 immagini |
| `reference_audios` | Slot espandibile: collega riferimenti vocali opzionali (`audio_1`, `audio_2`, `audio_3`), da 3 a 12 secondi ciascuno. Viene utilizzata solo la voce, non le parole: scrivi il dialogo nel prompt e assegna una voce in ordine, ad esempio `image 1 says "Hello!" in the voice from audio 1`. Richiede che `audio` sia abilitato. | AUDIO | No | Fino a 3 clip |
| `prompt` | Una descrizione testuale per la generazione video, fino a 5000 caratteri. Necessaria per descrivere i riferimenti che si desidera utilizzare. | STRING | Sì | Qualsiasi testo |
| `aspect_ratio` | Le proporzioni del video in output. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"3:4"`<br>`"4:3"` |
| `resolution` | Risoluzione del video in output (predefinito: `"720p"`). | COMBO | Sì | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` |
| `duration` | Durata del video in output in secondi (predefinito: 5). | INT | Sì | 3 to 16 |
| `audio` | Se abilitato, produce un video con audio, inclusi dialoghi ed effetti sonori (predefinito: True). | BOOLEAN | Sì | `True`<br>`False` |
| `seed` | Il seed controlla se il nodo deve rieseguire; i risultati non sono deterministici indipendentemente dal seed. Questo parametro ha la funzionalità "control after generate" (predefinito: 42). | INT | Sì | 1 to 2147483647 |

**Nota:** Al massimo possono essere utilizzate 15 immagini di riferimento in totale, contando ogni immagine di un batch. Ogni immagine deve essere di almeno 128x128 pixel con un rapporto d'aspetto compreso tra 1:5 e 5:1. L'audio di riferimento richiede che `audio` sia abilitato e genera un errore in caso contrario.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `VIDEO` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu4ReferenceVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `f37ceec93a6140d69332415b8fd748d55e6a608177430975b4b42ab33e593489`

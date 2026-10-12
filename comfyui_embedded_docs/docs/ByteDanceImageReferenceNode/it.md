# ByteDanceImageReferenceNode

Il nodo ByteDance Image Reference genera video utilizzando un prompt testuale e da una a quattro immagini di riferimento. Invia le immagini e il prompt a un servizio API esterno che crea un video corrispondente alla tua descrizione, incorporando allo stesso tempo lo stile visivo e il contenuto delle immagini di riferimento. Il nodo fornisce vari controlli per la risoluzione video, il rapporto d'aspetto, la durata e altri parametri di generazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello AI da utilizzare per la generazione del video (predefinito: `"seedance-1-0-lite-i2v-250428"`). | STRING | Sì | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"` |
| `prompt` | Il prompt testuale utilizzato per generare il video. | STRING | Sì | - |
| `images` | Da una a quattro immagini. Ogni immagine deve essere compresa tra 300x300 e 6000x6000 pixel, con un rapporto d'aspetto compreso tra 0.4 e 2.5. | IMAGE | Sì | - |
| `resolution` | La risoluzione del video di output. | STRING | Sì | `"480p"`<br>`"720p"` |
| `aspect_ratio` | Il rapporto d'aspetto del video di output (predefinito: `"adaptive"`). | STRING | Sì | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | La durata del video di output in secondi (predefinito: 5). | INT | Sì | 3 - 12 |
| `seed` | Seed da utilizzare per la generazione (predefinito: 0). | INT | No | 0 - 2147483647 |
| `watermark` | Indica se aggiungere una filigrana "AI generated" al video (predefinito: False). | BOOLEAN | No | - |

**Nota:** Il testo del prompt non deve contenere le seguenti stringhe di parametro: `--resolution`, `--ratio`, `--duration`, `--seed` o `--watermark`. Questi valori sono controllati esclusivamente tramite i relativi widget di input dedicati.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il file video generato in base al prompt di input e alle immagini di riferimento. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/it.md)

---
**Source fingerprint (SHA-256):** `77a0f9aee920d07a1374eaec8489eed494a4505369246c16007765d67e52ef99`

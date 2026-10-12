# Vidu2TextToVideoNode

Il nodo Vidu2 Text-to-Video Generation crea un video da una descrizione testuale. Si connette a un'API esterna per generare contenuti video basati sul prompt, consentendo di controllare la lunghezza, lo stile visivo e il formato del video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello AI da usare per la generazione video. Attualmente è disponibile un solo modello. | COMBO | Sì | `"viduq2"` |
| `prompt` | Una descrizione testuale per la generazione video, con una lunghezza massima di 2000 caratteri. | STRING | Sì | - |
| `duration` | La durata del video generato in secondi. Il valore può essere regolato tramite un cursore (predefinito: 5). | INT | No | da 1 a 10 |
| `seed` | Un numero usato per controllare la casualità della generazione, consentendo risultati riproducibili. Può essere controllato dopo la generazione (predefinito: 1). | INT | No | da 0 a 2147483647 |
| `aspect_ratio` | Il rapporto proporzionale tra larghezza e altezza del video. | COMBO | No | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `resolution` | Le dimensioni in pixel del video generato. Questo è un parametro avanzato. | COMBO | No | `"720p"`<br>`"1080p"` |
| `background_music` | Indica se aggiungere musica di sottofondo al video generato (predefinito: False). Questo è un parametro avanzato. | BOOLEAN | No | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2TextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `27b7c05ae1b3b23d07e775f67474ecef1ffc0bd8240f4aa2219e15949d854f27`

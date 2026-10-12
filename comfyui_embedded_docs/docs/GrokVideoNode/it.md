# Grok Video

Il nodo Grok Video genera un breve video a partire da una descrizione testuale. Può creare un video da zero utilizzando un prompt oppure generare un video da una singola immagine di input. Il nodo invia la richiesta a un'API esterna e restituisce il video generato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello da utilizzare per la generazione video (predefinito: `"grok-imagine-video-1.5-lite"`). | COMBO | Sì | `"grok-imagine-video"`<br>`"grok-imagine-video-1.5"`<br>`"grok-imagine-video-1.5-lite"` |
| `prompt` | Descrizione testuale del video desiderato. Opzionale per i modelli `grok-imagine-video-1.5` quando viene fornita un'immagine di input. | STRING | Sì | - |
| `resolution` | La risoluzione del video di output. `1080p` non è disponibile per `grok-imagine-video`. | COMBO | Sì | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | Le proporzioni del video di output. Ignorato quando viene fornita un'immagine di input; il video segue le proporzioni dell'immagine. | COMBO | Sì | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | La durata del video di output in secondi (predefinito: 6). | INT | Sì | da 1 a 15 |
| `seed` | Seme per determinare se il nodo deve essere rieseguito; i risultati effettivi sono non deterministici indipendentemente dal seme (predefinito: 0). | INT | Sì | da 0 a 2147483647 |
| `image` | Immagine iniziale opzionale. Se omessa, il video viene generato solo dal prompt testuale. | IMAGE | No | - |

**Nota:** Quando viene fornita un'`image`, è supportata una sola immagine di input; fornire più immagini causerà un errore. Il `prompt` deve essere non vuoto dopo la rimozione degli spazi quando non viene fornita alcuna immagine, oppure quando si utilizza `grok-imagine-video` anche con un'immagine. Per i modelli `grok-imagine-video-1.5`, il `prompt` è opzionale solo quando viene fornita un'immagine di input. La risoluzione `1080p` non è disponibile per `grok-imagine-video`. Quando `aspect_ratio` è impostato su `"auto"`, le proporzioni vengono scelte automaticamente dal servizio; quando viene fornita un'immagine di input, `aspect_ratio` viene ignorato e il video segue le proporzioni dell'immagine.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `output` | Il video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `ed5a1c39598a319d5b350b19f39a352dedd1150471695d25f7637fc0f8735d02`

# PixVerse Video di Transizione

Genera un video di transizione tra due immagini di input utilizzando l'API PixVerse. Fornisci un'immagine iniziale e un'immagine finale, e il nodo crea un video fluido che passa da una all'altra, guidato dal tuo prompt testuale e dalle impostazioni scelte.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `first_frame` | L'immagine iniziale per la transizione video | IMAGE | Sì | - |
| `last_frame` | L'immagine finale per la transizione video | IMAGE | Sì | - |
| `prompt` | Prompt per la generazione del video (predefinito: stringa vuota) | STRING | Sì | - |
| `quality` | Impostazione della qualità video (predefinito: `"540p"`) | COMBO | Sì | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `duration_seconds` | Durata del video in secondi | COMBO | Sì | `5`<br>`8` |
| `motion_mode` | Stile di movimento per la transizione (predefinito: `"normal"`) | COMBO | Sì | `"normal"`<br>`"fast"` |
| `seed` | Seed per la generazione del video (predefinito: 0) | INT | Sì | 0 to 2147483647 |
| `negative_prompt` | Una descrizione testuale opzionale degli elementi indesiderati in un'immagine (predefinito: stringa vuota) | STRING | No | - |

**Nota sui vincoli dei parametri:** Quando si utilizza la qualità 1080p, la modalità di movimento viene impostata automaticamente su `"normal"` e la durata è limitata a 5 secondi. Per qualsiasi durata diversa da 5 secondi, anche la modalità di movimento viene impostata automaticamente su `"normal"`.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Il video di transizione generato | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `9774f15ae93377d4768cee9f51ce004a791ecaad3cadd0a2467d354c4dbc6f23`

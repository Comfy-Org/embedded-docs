# Creatify Aurora 2.0 Avatar

Creatify Aurora 2.0 Avatar trasforma una foto, insieme a un clip vocale o a un brano musicale, in un video in cui la persona parla o canta. Il video ha la stessa durata dell'audio collegato e mantiene tale audio invariato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | Foto della persona da animare. Almeno 256 pixel per lato e un rapporto d'aspetto compreso tra 1:4 e 4:1; il video mantiene il rapporto d'aspetto della foto. | IMAGE | Sì | - |
| `audio` | Parlato o brano musicale che guida il movimento della bocca e la durata del video. Fino a 60 secondi, oppure 14 secondi con `"2k"`; addebitato per secondo iniziato. | AUDIO | Sì | Fino a 60 secondi |
| `resolution` | Risoluzione del video di output (predefinito: `"720p"`). | COMBO | Sì | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"2k"` |
| `text_prompt` | Scena, camera, illuminazione, espressione o movimento per l'inquadratura. Se vuoto, mantiene la foto così com'è (predefinito: stringa vuota). | STRING | Sì | Qualsiasi testo |
| `seed` | Il seed controlla se il nodo viene rieseguito. I risultati non sono deterministici indipendentemente dal seed (predefinito: 42). | INT | Sì | 0 a 2147483647 |

**Vincoli:** una foto più piccola di 256 pixel per lato, o con un rapporto d'aspetto al di fuori dell'intervallo da 1:4 a 4:1, genera un errore. Un audio più lungo del limite per la risoluzione scelta viene rifiutato: 60 secondi normalmente e 14 secondi con `"2k"`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `VIDEO` | Il video in cui la persona parla o canta, con l'audio collegato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyAurora2AvatarNode/it.md)

---
**Source fingerprint (SHA-256):** `29c83246ebed4bc7a9f3daf3612cd6f34bf2d5a2f1fde7612614a2da6a5010be`

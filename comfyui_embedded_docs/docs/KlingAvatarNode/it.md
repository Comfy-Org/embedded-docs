# Kling Avatar 2.0

Il nodo Kling Avatar 2.0 genera video di umani digitali in stile broadcast a partire da una singola foto di riferimento e da un file audio. Crea un video di un avatar parlante con un prompt testuale opzionale per definire azioni, emozioni e movimenti di camera dell'avatar.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | Immagine di riferimento dell'avatar. Larghezza e altezza devono essere almeno 300px. Il rapporto d'aspetto deve essere compreso tra 1:2.5 e 2.5:1. | IMAGE | Sì | - |
| `sound_file` | Input audio. La durata deve essere compresa tra 2 e 300 secondi. | AUDIO | Sì | - |
| `mode` | La modalità di generazione da utilizzare. | COMBO | Sì | `"std"`<br>`"pro"` |
| `prompt` | Prompt opzionale per definire azioni, emozioni e movimenti di camera dell'avatar. (predefinito: stringa vuota) | STRING | No | - |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 0) | INT | Sì | da 0 a 2147483647 |

**Nota:** Gli input `image` e `sound_file` hanno requisiti di validazione specifici. L'immagine deve essere di almeno 300x300 pixel con un rapporto d'aspetto compreso tra 1:2.5 e 2.5:1. Il file audio deve avere una durata compresa tra 2 e 300 secondi.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Il video dell'umano digitale generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingAvatarNode/it.md)

---
**Source fingerprint (SHA-256):** `34f64d168d6c407d9ab474e2637513c172090a0f0c219675d32f8e70ff84f2ae`

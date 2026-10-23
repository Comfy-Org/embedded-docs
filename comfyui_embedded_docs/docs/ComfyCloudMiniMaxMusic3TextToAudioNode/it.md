# Comfy Cloud MiniMax Music 3 da testo ad audio [BETA]

Esegue il workflow MiniMax Music 3 su una GPU di Comfy Cloud e restituisce un brano generato. Il prompt definisce stile, strumentazione e atmosfera; i testi vengono cantati anziché descritti e un testo vuoto rende il brano strumentale. Questo è un nodo beta e viene addebitato al secondo di GPU.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Descrizione del brano: stile, strumentazione e atmosfera. Gli spazi bianchi iniziali e finali vengono rimossi prima dell'invio. | STRING | Sì | Da 1 a 4096 caratteri |
| `lyrics` | Parole da cantare. Lasciare vuoto per un brano strumentale. | STRING | No | Da 0 a 4096 caratteri |
| `seed` | Seme casuale che controlla il risultato generato (predefinito: 42). | INT | Sì | 0 a 9223372036854775807 |
| `max_duration` | Durata massima del brano, in secondi (predefinito: 120.0). Il modello può terminare il brano prima. | FLOAT | Sì | Da 0.04 a 360.0 (passo 0.04) |
| `audio_quality` | Bitrate di output. `"V0"` è variabile ed è la qualità più alta delle tre (predefinito: `"V0"`). | COMBO | Sì | `"V0"`<br>`"128k"`<br>`"320k"` |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `AUDIO` | Il brano generato. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxMusic3TextToAudioNode/it.md)

---
**Source fingerprint (SHA-256):** `defc8d97071f2eaef4b00c6df721f4d10756e4867fefa22c1db7b8c3aafb6b7b`

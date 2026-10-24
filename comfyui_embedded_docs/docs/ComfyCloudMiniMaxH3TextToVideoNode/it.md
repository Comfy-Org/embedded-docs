# Comfy Cloud MiniMax H3 da testo a video [BETA]

Esegue il workflow text-to-video MiniMax H3 su una GPU di Comfy Cloud e restituisce un video con una colonna sonora corrispondente. Immagine e audio vengono prodotti nello stesso passaggio, invece di essere aggiunti successivamente tramite doppiaggio. Questo è un nodo beta e viene fatturato per secondo GPU.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | La descrizione testuale del video, inclusi i suoni che l'inquadratura dovrebbe contenere. Gli spazi bianchi iniziali e finali vengono rimossi prima dell'invio. | STRING | Sì | da 1 a 4096 caratteri |
| `seed` | Seme casuale che controlla il risultato generato (predefinito: 42). | INT | Sì | da 0 a 18446744073709551615 |
| `aspect_ratio` | Proporzioni del video generato (predefinito: `"16:9"`). | COMBO | Sì | `"1:1"`<br>`"3:4"`<br>`"2:3"`<br>`"3:2"`<br>`"4:3"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"` |
| `resolution` | Budget della dimensione del fotogramma (predefinito: `"480p"`). 720p costa all'incirca il doppio dei secondi GPU rispetto a 480p. | COMBO | Sì | `"480p"`<br>`"720p"` |
| `duration_seconds` | Durata in secondi (predefinito: 5). La pipeline quantizza in passi di 17 fotogrammi a 24 fps, quindi la clip si colloca entro circa due terzi di secondo da questo valore. | INT | Sì | da 5 a 15 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `VIDEO` | Il video generato con la relativa colonna sonora. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3TextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `bd1cbc80baa3b77ba48b529119495052252570b949676742b4c77cfe86b70ee2`

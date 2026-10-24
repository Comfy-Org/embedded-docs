# Comfy Cloud MiniMax H3 da immagine a video [BETA]

Esegue il workflow image-to-video di MiniMax H3 su una GPU di Comfy Cloud e restituisce un video con una colonna sonora abbinata. L'immagine statica diventa il primo fotogramma. Reimmettendo il fotogramma finale di una clip si continua la sequenza, quindi concatenando più esecuzioni si costruisce un'inquadratura più lunga. Questo è un nodo beta e l'addebito avviene per secondo GPU.

## Ingressi

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | L'immagine da cui inizia il video. Viene caricata a un massimo di 2048x2048 pixel prima dell'esecuzione del workflow. | IMAGE | Sì | - |
| `prompt` | La descrizione testuale del movimento e dei suoni che l'inquadratura deve contenere. Gli spazi iniziali e finali vengono rimossi prima dell'invio. | STRING | Sì | da 1 a 4096 caratteri |
| `seed` | Seme casuale che controlla il risultato generato (predefinito: 42). | INT | Sì | da 0 a 18446744073709551615 |
| `aspect_ratio` | Proporzioni del video generato (predefinito: `"1:1"`). | COMBO | Sì | `"1:1"`<br>`"3:4"`<br>`"2:3"`<br>`"3:2"`<br>`"4:3"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"` |
| `resolution` | Budget della dimensione del fotogramma (predefinito: `"480p"`). Il 720p costa all'incirca il doppio dei secondi GPU del 480p. | COMBO | Sì | `"480p"`<br>`"720p"` |
| `duration_seconds` | Durata in secondi (predefinito: 5). La pipeline quantizza in passi di 17 fotogrammi a 24 fps, quindi la clip si attesta entro circa due terzi di secondo da questo valore. | INT | Sì | da 5 a 15 |

## Uscite

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `VIDEO` | Il video generato con la sua colonna sonora. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3ImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `d3657e266f2b9f789414a106ef66b6c64ec314d27c3b6a99c3a6a9b8584abf61`

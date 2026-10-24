# Comfy Cloud MiniMax H3 Da primo-ultimo fotogramma a video [BETA]

Esegue il workflow first-last frame di MiniMax H3 su una GPU di Comfy Cloud e restituisce il movimento tra due fotogrammi chiave con una colonna sonora corrispondente. Fornisci i fotogrammi di apertura e chiusura e il modello riempie l'inquadratura tra di essi. L'ultimo fotogramma è facoltativo: se lo ometti, il movimento si sviluppa invece a partire dal primo fotogramma. Questo è un nodo beta e la fatturazione avviene al secondo di GPU.

## Ingressi

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | L'immagine da cui inizia il video. Viene caricata a una risoluzione massima di 2048x2048 pixel prima dell'esecuzione del workflow. | IMAGE | Sì | - |
| `last_frame` | Fotogramma di chiusura facoltativo. Se collegato, il movimento generato termina su questa immagine; senza di esso il movimento si sviluppa a partire da `first_frame`. | IMAGE | No | - |
| `prompt` | Descrizione testuale del movimento e dei suoni che l'inquadratura deve contenere. Gli spazi iniziali e finali vengono rimossi prima dell'invio. | STRING | Sì | da 1 a 4096 caratteri |
| `seed` | Seme casuale che controlla il risultato generato (predefinito: 42). | INT | Sì | da 0 a 18446744073709551615 |
| `aspect_ratio` | Proporzioni del video generato (predefinito: `"1:1"`). | COMBO | Sì | `"1:1"`<br>`"3:4"`<br>`"2:3"`<br>`"3:2"`<br>`"4:3"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"` |
| `resolution` | Budget della dimensione del fotogramma (predefinito: `"480p"`). 720p costa all'incirca il doppio in secondi GPU rispetto a 480p. | COMBO | Sì | `"480p"`<br>`"720p"` |
| `duration_seconds` | Durata in secondi (predefinito: 5). La pipeline quantizza in passi di 17 fotogrammi a 24 fps, quindi la clip risulta entro circa due terzi di secondo da questo valore. | INT | Sì | da 5 a 15 |

## Uscite

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `VIDEO` | Il video generato con la relativa colonna sonora. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3FirstLastFrameToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `5b9d1a2155951fb953e94726f0c6ca7720a805ab5d3015adaa5cc496acaa0de3`

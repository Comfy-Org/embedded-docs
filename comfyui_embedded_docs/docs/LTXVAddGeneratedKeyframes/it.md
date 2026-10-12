# LTXVAddGeneratedKeyframes

Il nodo LTXV Add Generated Keyframes aggiunge keyframe di dettaglio a un latente video. Ogni keyframe è un frame latente di token posizionato su un singolo frame pixel; viene sottoposto a denoising insieme al video e non fa parte dell'output decodificato. Il posizionamento è uno slot ogni `interval_frames` pixel, saltando i frame I2V, le guide esistenti e i keyframe generati già presenti nel conditioning; estraili di nuovo con LTXV Separate Generated Keyframes. È richiesto un checkpoint addestrato per i keyframe generati (uno che contiene `keyframes_abs_pos_embedding`).

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `positive` | Conditioning positivo a cui vengono agganciati i keyframe. | CONDITIONING | Sì | N/A |
| `negative` | Conditioning negativo a cui vengono agganciati i keyframe. | CONDITIONING | Sì | N/A |
| `vae` | Usato solo per leggere i fattori di scala del latente. | VAE | Sì | N/A |
| `latent` | Latente video 5D semplice a cui generare i keyframe insieme. Aggiungili prima di Concat AV Latent. | LATENT | Sì | N/A |
| `interval_frames` | Passo in frame pixel per il posizionamento automatico. Il valore predefinito 24 corrisponde a circa un keyframe al secondo a 24 fps. I pixel occupati vengono saltati. Ignorato quando `frame_indices` è impostato. (predefinito: 24) | INT | No | 1-1024 |
| `keyframes` | Contenuto opzionale con cui inizializzare i nuovi keyframe. Collega i keyframe da un Separate precedente (stessa dimensione spaziale), o un latente video semplice per copiare il frame più vicino a ogni nuovo slot (ad es. dopo un upscale temporale). Questi vengono comunque sottoposti a denoising, non bloccati come guide. Gli indici registrati su un latente keyframes vengono ignorati a meno che `frame_indices` non sia impostato. Ha effetto solo quando il campionamento inizia sotto sigma 1. | LATENT | No | N/A |
| `frame_indices` | Indici di frame pixel opzionali. Lascia vuoto per posizionare da `interval_frames` sulla canvas corrente. Quando impostato, questa lista è il posizionamento (i keyframe collegati vengono abbinati in ordine). L'ultimo frame è consentito; il frame 0 no (è già un token autonomo). (predefinito: stringa vuota) | STRING | No | Interi separati da virgola; da 1 all'ultimo frame pixel (frame 0 escluso) |

**Nota:** Il `latent` deve essere un latente video 5D semplice con i keyframe generati aggiunti prima di Concat AV Latent. Quando `frame_indices` è impostato, ogni frame pixel elencato deve essere univoco e non può già contenere un keyframe immagine, una guida o un keyframe generato. Se `frame_indices` è vuoto, i pixel occupati vengono saltati automaticamente; se non esiste uno slot di dettaglio libero, il nodo genera un errore. Quando si aggiungono keyframe generati esistenti, il latente deve ancora avere gli stessi token per frame e il blocco esistente deve terminare all'ultimo frame latente.

## Output

| Nome Output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `positive` | Conditioning positivo con attenzione ai keyframe generati allegata. | CONDITIONING |
| `negative` | Conditioning negativo con attenzione ai keyframe generati allegata. | CONDITIONING |
| `latent` | Latente video con keyframe generati aggiunti su T. | LATENT |

## Note

- Il parametro `interval_frames` imposta la spaziatura dei keyframe posizionati automaticamente. Un valore più alto comporta meno keyframe e spaziatura più ampia; un valore più basso produce più keyframe.
- L'input `keyframes` consente di inizializzare i nuovi keyframe con keyframe esistenti o un latente video. Se viene fornito un latente video semplice più lungo, il frame video più vicino viene copiato a ogni nuovo slot. Questi keyframe vengono comunque sottoposti a denoising e non sono bloccati come guide.
- Il parametro `frame_indices` consente di specificare indici esatti di frame pixel in cui posizionare i keyframe. Quando fornito, `interval_frames` viene ignorato. La lista deve contenere interi univoci all'interno dell'intervallo di pixel valido, e il frame 0 non è consentito.
- Gli output `positive` e `negative` contengono il conditioning con l'attenzione ai keyframe generati allegata.
- L'output `latent` contiene il latente video con i keyframe generati aggiunti su T.
- È richiesto un checkpoint addestrato per i keyframe generati (uno che contiene `keyframes_abs_pos_embedding`).
- Estrai i keyframe generati con LTXV Separate Generated Keyframes.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGeneratedKeyframes/it.md)

---
**Source fingerprint (SHA-256):** `43053d15eceb61f37223c46dd46417c71f0503ef3a412ee50a3b2f764f310a64`

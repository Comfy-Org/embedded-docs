# Concatena AV Latent

Questo nodo unisce un latent video e un latent audio in un unico latent audio-video (AV) congiunto, pronto per modelli AV come LTXV o MiniMax H3. Se l'input video è già un latent AV, il suo stream video viene mantenuto e solo lo stream audio viene sostituito con il latent audio fornito.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video_latent` | La rappresentazione latent dei dati video. Quando contiene già sia stream video sia stream audio, il nodo mantiene il suo stream video e sostituisce l'audio con quello di `audio_latent`. | LATENT | Sì |  |
| `audio_latent` | La rappresentazione latent dei dati audio. La sua lunghezza viene regolata per adattarsi allo stream video: l'audio più lungo viene tagliato, quello più corto viene riempito con zeri. | LATENT | Sì |  |

**Nota:** I campioni di entrambi gli input vengono combinati come una coppia di stream video e audio in un tensore annidato. Se uno dei due input contiene un `noise_mask`, l'output ne include uno combinato; una maschera mancante viene sostituita con una maschera composta interamente da 1 corrispondente alla forma dei suoi campioni. Quando l'audio più corto viene riempito, la regione riempita viene lasciata non mascherata, così il modello può generarla. Il nodo solleva un errore se il latent audio non può essere adattato al latent video, per esempio quando i due latent differiscono in più di una dimensione o quando differiscono nelle dimensioni batch o dei canali.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | Un latent che contiene i campioni video e audio impacchettati insieme come due stream, più un `noise_mask` combinato quando almeno un input ne fornisce uno. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/it.md)

---
**Source fingerprint (SHA-256):** `0231f9db2ce73132d8555fbb33f295b68aa68a0c1c54e4a0c5d2e1f67b5611cb`

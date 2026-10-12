# LTXVSeparateAVLatent

Il nodo LTXVSeparateAVLatent divide un latent audiovisivo combinato in due latent separati: uno contenente i dati video e uno contenente i dati audio. Funziona con qualsiasi modello audiovisivo, come LTXV o MiniMax H3. Il tensore `samples` viene diviso lungo la sua prima dimensione, con il primo elemento che diventa il latent video e il secondo elemento che diventa il latent audio; se è presente una maschera di rumore, viene divisa allo stesso modo.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `av_latent` | La rappresentazione latent audiovisiva combinata da dividere in latent video e audio. | LATENT | Sì | N/A |

**Nota:** Si prevede che il tensore `samples` del latent di input abbia almeno due elementi lungo la prima dimensione (dimensione batch). Il primo elemento viene utilizzato per il latent video e il secondo elemento viene utilizzato per il latent audio. Se è presente un `noise_mask`, viene diviso allo stesso modo.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `video_latent` | La rappresentazione latent contenente i dati video separati. | LATENT |
| `audio_latent` | La rappresentazione latent contenente i dati audio separati. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/it.md)

---
**Source fingerprint (SHA-256):** `22ed38bbc1b5716cee380c35c50455810f79c273f51bbe6a535c9ae33192afe6`

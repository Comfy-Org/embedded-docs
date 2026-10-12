# Audio latent LTXV vuoto

Il nodo LTXV Empty Latent Audio crea un batch di tensori latenti audio vuoti (riempiti di zeri). Legge la configurazione di un modello Audio VAE collegato per determinare le dimensioni latenti corrette, come il numero di canali e i bin di frequenza, e calcola quanti latenti audio sono necessari dal conteggio dei frame e dal frame rate. Il latente vuoto risultante può essere utilizzato come punto di partenza per flussi di lavoro di generazione o manipolazione audio.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `frames_number` | Numero di frame. Il valore predefinito è 97. | INT | Sì | 1 a 1000 |
| `frame_rate` | Numero di frame al secondo. Il valore predefinito è 25.0. Questo input accetta valori FLOAT o INT. | FLOAT | Sì | 1.0 a 1000.0 |
| `batch_size` | Il numero di campioni audio latenti nel batch. Il valore predefinito è 1. | INT | Sì | 1 a 4096 |
| `audio_vae` | Il modello Audio VAE da cui ottenere la configurazione. Visualizzato come "Audio VAE". | VAE | Sì | N/A |

**Nota:** L'input `audio_vae` è obbligatorio. Il nodo genera un errore se non viene fornito.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `Latent` | Un tensore latente audio vuoto con forma (batch_size, z_channels, num_audio_latents, audio_freq), dove il numero di canali e i bin di frequenza provengono dall'Audio VAE e il numero di latenti audio deriva da `frames_number` e `frame_rate`. L'output include anche un campo `type` impostato su "audio". | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/it.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`

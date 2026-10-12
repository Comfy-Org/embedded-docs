# LTXVSeparateGeneratedKeyframes

## Panoramica

Il nodo LTXV Separate Generated Keyframes estrae nuovamente i keyframe generati aggiunti da LTXV Add Generated Keyframes da un latent campionato e li rimuove dal conditioning. Usalo prima di eseguire l'upscaling spaziale del latent video. Non eseguire prima LTXV Crop Guides — tratta i keyframe generati come guide usa e getta e li elimina.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `positive` | Conditioning positivo che contiene i metadati dei keyframe generati. I metadati vengono rimossi da esso in output. | CONDITIONING | Sì | N/A |
| `negative` | Conditioning negativo che contiene i metadati dei keyframe generati. I metadati vengono rimossi da esso in output. | CONDITIONING | Sì | N/A |
| `latent` | Latent video che contiene i keyframe generati. I keyframe vengono rimossi da esso in output. | LATENT | Sì | N/A |
| `keyframes_to_batch` | Restituisce i keyframe come batch di latent a singolo frame. Lascia disattivato per ottenerli come un unico latent multi-frame, che è ciò che si aspettano l'upsampler del latent e un successivo Add Generated Keyframes. | BOOLEAN | No | default: False |

### Note sugli input

- `positive` deve contenere i metadati dei keyframe generati, altrimenti il nodo genera un errore che indica di aggiungerli prima con LTXV Add Generated Keyframes.
- `latent` deve essere un normale latent video (un tensore 5D). Se i latent video e audio sono ancora combinati, separali prima con Separate AV Latent.
- Il numero di token per frame latent registrato quando sono stati aggiunti i keyframe deve corrispondere ai token per frame del `latent` fornito. Se il latent è stato ridescalato dopo l'aggiunta dei keyframe, non saranno più allineati e il nodo genera un errore — separali prima di eseguire l'upscaling del latent.
- L'intervallo di frame dei keyframe registrato deve rientrare nel `latent` fornito, altrimenti il nodo genera un errore che indica che i keyframe sono stati registrati rispetto a un latent diverso.
- L'indice della voce di guide attention registrato deve esistere ancora nel conditioning. Se il conditioning è stato ricostruito dopo l'aggiunta dei keyframe, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `positive` | Conditioning positivo con i metadati dei keyframe generati rimossi. | CONDITIONING |
| `negative` | Conditioning negativo con i metadati dei keyframe generati rimossi. | CONDITIONING |
| `latent` | Latent video con i keyframe generati rimossi. | LATENT |
| `keyframes` | I keyframe estratti, etichettati con generated_keyframe_indices e generated_keyframe_num_frames. Passali a un successivo Add Generated Keyframes per inizializzare nuovi slot, oppure a Generated Keyframes To Guides per fissarli come guide immagine fisse (gli indici vengono rimappati se la lunghezza della canvas è cambiata). | LATENT |

## Note

- Il parametro `keyframes_to_batch` determina se i keyframe vengono restituiti come batch di latent a singolo frame o come un unico latent multi-frame.
- Il nodo garantisce che i keyframe generati vengano rimossi dal conditioning e dal latent prima di qualsiasi ulteriore elaborazione.
- L'output `keyframes` può essere utilizzato per inizializzare nuovi slot per i keyframe generati o per fissarli come guide immagine fisse.
- Il nodo genera un `ValueError` se il latent non contiene keyframe generati o se i keyframe non corrispondono al formato previsto.
- Il nodo presuppone che i keyframe generati siano stati aggiunti usando il nodo LTXV Add Generated Keyframes e che siano compatibili con il latent corrente.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/it.md)

---
**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`

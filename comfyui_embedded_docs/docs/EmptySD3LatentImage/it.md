# Immagine Latent Vuota SD3

EmptySD3LatentImage crea un'immagine latente vuota (tutta a zero) nel layout che i modelli Stable Diffusion 3 si aspettano. Poiché il latente è vuoto, viene normalmente utilizzato come punto di partenza che un flusso di generazione riempie con un'immagine. La larghezza e l'altezza scelte determinano la dimensione dell'immagine finale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `width` | La larghezza dell'immagine latente in pixel (predefinito: 1024). I valori sono incrementati a passi di 16. | INT | Sì | da 16 a MAX_RESOLUTION (passo: 16) |
| `height` | L'altezza dell'immagine latente in pixel (predefinito: 1024). I valori sono incrementati a passi di 16. | INT | Sì | da 16 a MAX_RESOLUTION (passo: 16) |
| `batch_size` | Il numero di immagini latenti da generare nel batch (predefinito: 1). | INT | Sì | da 1 a 4096 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `LATENT` | Un tensore latente contenente campioni vuoti (tutti a zero) nel formato compatibile con SD3. Il tensore ha 16 canali, è ridotto di un fattore 8 rispetto a `width` e `height`, e presenta un rapporto di riduzione spaziale di 8. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/it.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`

# EmptyChromaRadianceLatentImage

Il nodo EmptyChromaRadianceLatentImage crea un'immagine latente vuota con le dimensioni specificate, per l'uso in flussi di lavoro chroma radiance. Produce un tensore riempito di zeri che funge da punto di partenza per le operazioni nello spazio latente, consentendo di definire larghezza, altezza e dimensione del batch dell'immagine latente vuota.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `width` | La larghezza dell'immagine latente in pixel (predefinito: 1024) | INT | Sì | 16 a MAX_RESOLUTION |
| `height` | L'altezza dell'immagine latente in pixel (predefinito: 1024) | INT | Sì | 16 a MAX_RESOLUTION |
| `batch_size` | Il numero di immagini latenti da generare in un batch (predefinito: 1) | INT | Sì | 1 a 4096 |

Nota: `width` e `height` sono definiti con un passo di 16, quindi i valori vengono adeguati a multipli di 16.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples` | Il tensore dell'immagine latente vuota generato, riempito di zeri, con forma batch_size x 3 x height x width | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/it.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`

# Upscaling latent Hunyuan Video 1.5 con modello

Il nodo Hunyuan Video 15 Latent Upscale With Model aumenta la risoluzione di una rappresentazione latente dell'immagine. Dapprima esegue l'upscale dei campioni latenti a una dimensione specificata utilizzando un metodo di interpolazione scelto, quindi affina il risultato sottoposto a upscale utilizzando un modello di upscale specializzato Hunyuan Video 1.5 per migliorare la qualità.

## Input
| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di upscale latente Hunyuan Video 1.5 utilizzato per affinare i campioni sottoposti a upscale. | LATENT_UPSCALE_MODEL | Sì | N/A |
| `samples` | La rappresentazione latente dell'immagine da sottoporre a upscale. | LATENT | Sì | N/A |
| `upscale_method` | L'algoritmo di interpolazione utilizzato per il passaggio iniziale di upscale (predefinito: `"bilinear"`). | COMBO | Sì | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `width` | La larghezza di destinazione per il latente sottoposto a upscale, in pixel. Un valore di 0 calcolerà automaticamente la larghezza in base all'altezza di destinazione e alle proporzioni originali. La larghezza finale del risultato sarà un multiplo di 16 (predefinito: 1280). | INT | Sì | 0 to 16384 (step: 8) |
| `height` | L'altezza di destinazione per il latente sottoposto a upscale, in pixel. Un valore di 0 calcolerà automaticamente l'altezza in base alla larghezza di destinazione e alle proporzioni originali. L'altezza finale del risultato sarà un multiplo di 16 (predefinito: 720). | INT | Sì | 0 to 16384 (step: 8) |
| `crop` | Determina come il latente sottoposto a upscale viene ritagliato per adattarsi alle dimensioni di destinazione. | COMBO | Sì | `"disabled"`<br>`"center"` |

**Nota sulle dimensioni:** Se sia `width` sia `height` sono impostati a 0, il nodo restituisce l'input `samples` invariato. Se solo una dimensione è impostata a 0, l'altra dimensione viene calcolata per preservare le proporzioni originali. Entrambi i valori vengono limitati a un minimo di 64, e la destinazione di upscale passata al passaggio di interpolazione è `width // 16` per `height // 16`, quindi le dimensioni richieste vengono effettivamente arrotondate per difetto a multipli di 16.

## Output
| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `LATENT` | La rappresentazione latente dell'immagine sottoposta a upscale e affinata dal modello, restituita come tensore float sulla CPU. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/it.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`

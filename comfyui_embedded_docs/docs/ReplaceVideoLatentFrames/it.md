# Sostituisci Frame Latent Video

ReplaceVideoLatentFrames sostituisce un intervallo di fotogrammi in un video latente di destinazione con fotogrammi da un video latente sorgente, a partire da un indice di fotogramma specificato. Se non viene fornito alcun latente sorgente, il latente di destinazione viene restituito invariato. Il nodo supporta indici negativi e registra un avviso quando i fotogrammi sorgente non rientrano nella destinazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `destination` | Il latente di destinazione in cui verranno sostituiti i fotogrammi. | LATENT | Sì | - |
| `source` | Il latente sorgente che fornisce i fotogrammi da inserire nel latente di destinazione. Se non fornito, il latente di destinazione viene restituito invariato. | LATENT | No | - |
| `index` | L'indice del fotogramma latente iniziale nel latente di destinazione in cui verranno posizionati i fotogrammi del latente sorgente. I valori negativi contano dalla fine (predefinito: 0; passo: 1). | INT | Sì | -MAX_RESOLUTION to MAX_RESOLUTION |

**Vincoli:**

* Un `index` negativo viene corretto aggiungendolo al numero di fotogrammi della destinazione, quindi conta all'indietro dalla fine del latente di destinazione.
* Se `index` punta oltre il numero di fotogrammi della destinazione, o se i fotogrammi sorgente non rientrano nella destinazione a partire da `index`, viene registrato un avviso e il latente di destinazione viene restituito invariato.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Il video latente risultante dopo l'operazione di sostituzione dei fotogrammi. Se la sostituzione non può essere eseguita, il latente di destinazione viene restituito invariato. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/it.md)

---
**Source fingerprint (SHA-256):** `5b98d875bdeaec63521bff19fecbc5510036c8b4f90322d8296b216688b557bf`

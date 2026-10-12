# HiDreamO1ReferenceImages

Questo nodo collega le immagini di riferimento sia al conditioning positivo sia a quello negativo, in modo che i nodi a valle possano utilizzarle per guidare la generazione. Le immagini di riferimento vengono applicate nell'ordine numerico dei rispettivi socket di input. Se non è collegata alcuna immagine di riferimento, il conditioning positivo e quello negativo passano invariati.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Il conditioning positivo a cui collegare le immagini di riferimento. | CONDITIONING | Sì | - |
| `negative` | Il conditioning negativo a cui collegare le immagini di riferimento. | CONDITIONING | Sì | - |
| `images` | Le immagini di riferimento vengono usate nell'ordine numerico dei socket. Quando vengono fornite immagini, queste vengono collegate sia al conditioning positivo sia a quello negativo. | IMAGE | No | Da 0 a 100 immagini (`image_1` a `image_100`) |

**Nota sul parametro `images`:** Questo è un input autogrow che fornisce socket numerati da `image_1` a `image_100`. Le immagini vengono usate nell'ordine numerico dei socket. L'input è opzionale: se non è collegata alcuna immagine di riferimento, il nodo restituisce il conditioning `positive` e `negative` invariati. Quando le immagini sono collegate, lo stesso insieme di immagini di riferimento viene collegato a entrambi gli output, e il conditioning negativo viene anche contrassegnato come negativo prima che le immagini vengano collegate.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Il conditioning positivo con le immagini di riferimento collegate. | CONDITIONING |
| `negative` | Il conditioning negativo con le immagini di riferimento collegate. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/it.md)

---
**Source fingerprint (SHA-256):** `07f9f0ea19957523e95d04b9086dc994807bb0cd5262fe798dc784c1ecb4920d`

# SDPoseKeypointExtractor

Il nodo SDPoseKeypointExtractor rileva i keypoint della posa umana dalle immagini di input usando il modello SDPose. Può elaborare immagini complete o regioni specifiche definite da bounding box e restituisce in output i keypoint rilevati nel formato OpenPose, che include le coordinate per ogni persona e un punteggio di confidenza per ciascun keypoint.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello SDPose utilizzato per il rilevamento dei keypoint. Deve essere un modello con un attributo `heatmap_head`, specificamente dal repository SDPose. | MODEL | Sì | - |
| `vae` | Il modello VAE utilizzato per codificare le immagini di input nello spazio latente per l'elaborazione. | VAE | Sì | - |
| `image` | L'immagine di input o il batch di immagini da cui estrarre i keypoint di posa. | IMAGE | Sì | - |
| `batch_size` | Il numero di immagini da elaborare contemporaneamente quando si opera in modalità immagine completa (ovvero, quando `bboxes` non è fornito). Questo può velocizzare l'elaborazione. (predefinito: 16) | INT | No | 1 to 10000 |
| `bboxes` | Bounding box opzionali per rilevamenti più accurati. Necessari per il rilevamento multi-persona. Se forniti, il nodo estrarrà i keypoint da ciascuna regione specificata. | BOUNDINGBOX | No | - |

**Vincoli dei parametri:**
*   L'input `model` deve essere un modello SDPose specifico. Se il modello fornito non ha un attributo `heatmap_head`, il nodo genererà un errore.
*   Il nodo opera in due modalità distinte in base all'input `bboxes`:
    1.  **Modalità Bounding Box:** Quando `bboxes` è fornito, elabora ciascuna regione specificata individualmente. Questa modalità è necessaria per rilevare più persone in una singola immagine.
    2.  **Modalità Immagine Completa:** Quando `bboxes` non è fornito, elabora l'intera immagine come batch. Il parametro `batch_size` si applica solo in questa modalità.
*   Quando `bboxes` è fornito, deve essere un elenco di bounding box. Se ci sono meno elenchi di bounding box rispetto alle immagini, l'ultimo elenco viene riutilizzato per le immagini rimanenti.
*   Le bounding box con larghezza o altezza pari a zero (ad es., `x2 <= x1` o `y2 <= y1`) vengono saltate.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `keypoints` | Keypoint nel formato frame OpenPose (canvas_width, canvas_height, people). L'output contiene le persone rilevate, ciascuna con un array di coordinate dei keypoint (x, y) e i relativi punteggi di confidenza. | POSE_KEYPOINT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseKeypointExtractor/it.md)

---
**Source fingerprint (SHA-256):** `5e199e9d08a46d934c6d1f4b1a411f0ca95eb5e7f85ec39f59a058c9be598e9f`

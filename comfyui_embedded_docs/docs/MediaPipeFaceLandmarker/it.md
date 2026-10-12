# MediaPipeFaceLandmarker

## Panoramica

Rileva volti in un'immagine e identifica 468 punti di riferimento facciali (punti chiave) su ciascun volto utilizzando i modelli BlazeFace e FaceMesh di MediaPipe. Calcola inoltre i coefficienti blendshape ARKit-52 per l'analisi delle espressioni facciali. Il nodo può elaborare più immagini in un batch e restituisce sia i dati dei punti di riferimento sia i bounding box per ciascun volto rilevato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `face_detection_model` | Il modello di rilevamento volti MediaPipe da utilizzare per il rilevamento dei punti di riferimento. | FACE_DETECTION_MODEL | Sì |  |
| `image` | L'immagine di input o il batch di immagini in cui rilevare i volti. | IMAGE | Sì |  |
| `detector_variant` | Portata del rilevatore di volti. `"short"` è ottimizzato per volti in primo piano (entro circa 2 m dalla fotocamera); `"full"` copre volti più lontani/piccoli (fino a circa 5 m) ma è più lento. `"both"` esegue entrambi i rilevatori e mantiene quello che ha trovato più volti per frame (costo di rilevamento circa 2x). Predefinito: `"short"`. | COMBO | Sì | `"short"`<br>`"full"`<br>`"both"` |
| `num_faces` | Numero massimo di volti da restituire per frame. 0 significa nessun limite (restituisce tutti quelli rilevati). Predefinito: 1. | INT | Sì | 0 a 16 |
| `min_confidence` | Soglia del punteggio BlazeFace. Valori più bassi aiutano a rilevare volti piccoli o occlusi. Predefinito: 0.5. | FLOAT | No | 0.00 a 1.00 |
| `missing_frame_fallback` | Comportamento per frame quando il rilevamento fallisce in un batch. `"empty"` lascia il frame senza volto. `"previous"` copia il rilevamento riuscito più recente. `"interpolate"` interpola linearmente (lerp) landmark/bbox/blendshape tra i frame riusciti che delimitano l'intervallo. Multi-volto: accoppia i volti tra i frame tramite il vicino più prossimo greedy basato sul centro del bbox. Predefinito: `"empty"`. | COMBO | No | `"empty"`<br>`"previous"`<br>`"interpolate"` |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `face_landmarks` | Un output strutturato contenente i risultati del rilevamento dei volti per frame, inclusi 468 punti di riferimento facciali, coefficienti blendshape ARKit-52, matrici di trasformazione e set di connessioni per la visualizzazione della mesh. | FACE_LANDMARKS |
| `bboxes` | Un elenco di bounding box per ciascun volto rilevato, con coordinate (x, y, larghezza, altezza), etichetta "face" e punteggio di confidenza. Un elenco per ogni frame di input. | BOUNDING_BOX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceLandmarker/it.md)

---
**Source fingerprint (SHA-256):** `f60ed6201288a59d65d62cc98c12f227a353870c36decea8da81a063cfdf2bba`

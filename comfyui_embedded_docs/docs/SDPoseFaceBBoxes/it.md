# SDPoseFaceBBoxes

Il nodo SDPoseFaceBBoxes elabora i dati dei keypoint di posa per rilevare e generare bounding box attorno ai volti umani. Analizza i keypoint 2D del volto per ogni persona in un frame, calcola una bounding box basata su quei punti e può regolare dimensione e forma della box. Le bounding box risultanti sono formattate per essere compatibili con altri nodi del flusso di lavoro SDPose, come SDPoseKeypointExtractor.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `keypoints` | I dati dei keypoint di posa contenenti informazioni sulle persone rilevate e sui relativi landmark del corpo/volto per frame. | POSE_KEYPOINT | Sì | - |
| `scale` | Moltiplicatore per l'area della bounding box attorno a ciascun volto rilevato. Un valore più grande crea una box più grande. (predefinito: 1.5) | FLOAT | No | 1.0 - 10.0 |
| `force_square` | Espande l'asse più corto della bbox in modo che la regione di ritaglio sia sempre quadrata. (predefinito: True) | BOOLEAN | No | - |

**Nota:** L'input `keypoints` deve essere nel formato specifico prodotto da nodi come SDPoseKeypointExtractor, contenente i dati `canvas_height`, `canvas_width` e `people` con `face_keypoints_2d` per ciascuna persona.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `bboxes` | Un elenco di bounding box del volto per ciascun frame. Ogni bounding box è definita dalle coordinate del suo angolo in alto a sinistra (`x`, `y`), `width` e `height`. Questo output è compatibile con l'input `bboxes` del nodo SDPoseKeypointExtractor. | BOUNDINGBOX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseFaceBBoxes/it.md)

---
**Source fingerprint (SHA-256):** `dc68640f46afcba4c10a907fd9467671d508cd5bac7670b35a038d159f9d8f50`

# SDPose Disegna Keypoints

Il nodo SDPoseDrawKeypoints riceve in input dati di stima della posa (keypoint) e li disegna come uno scheletro visivo su una tela vuota. Consente di disegnare selettivamente diverse parti della posa, come corpo, testa, mani, viso e piedi, con larghezze delle linee e dimensioni dei punti personalizzabili. L'immagine risultante può essere utilizzata per la visualizzazione o come input per altri nodi che richiedono un'immagine della posa.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `keypoints` | I dati dei keypoint della posa da disegnare. Questi dati provengono tipicamente da un nodo di rilevamento della posa e possono contenere uno o più fotogrammi. | POSE_KEYPOINT | Sì | - |
| `draw_body` | Controlla se viene disegnato lo scheletro del corpo principale (predefinito: True). | BOOLEAN | No | - |
| `draw_hands` | Controlla se vengono disegnati i keypoint delle mani (predefinito: True). | BOOLEAN | No | - |
| `draw_face` | Controlla se vengono disegnati i keypoint del viso (predefinito: True). | BOOLEAN | No | - |
| `draw_feet` | Controlla se vengono disegnati i keypoint dei piedi (predefinito: False). | BOOLEAN | No | - |
| `stick_width` | La larghezza delle linee usate per disegnare lo scheletro del corpo e della testa (predefinito: 4). | INT | No | da 1 a 10 |
| `face_point_size` | La dimensione dei punti usati per disegnare i keypoint del viso (predefinito: 3). | INT | No | da 1 a 10 |
| `score_threshold` | Il punteggio di confidenza minimo che un keypoint deve avere per essere disegnato. I keypoint con punteggi inferiori a questo valore vengono ignorati (predefinito: 0.3). | FLOAT | No | da 0.0 a 1.0 |
| `draw_head` | Controlla se vengono disegnati i keypoint della testa (naso, occhi, orecchie) (predefinito: True). | BOOLEAN | No | - |

**Nota:** Se l'input `keypoints` è vuoto o `None`, il nodo restituirà un'immagine 64x64 vuota.

**Nota:** `draw_body` e `draw_head` funzionano in modo indipendente. Quando `draw_head` è disabilitato, i keypoint della testa non vengono disegnati anche se `draw_body` è abilitato. Quando `draw_body` è disabilitato ma `draw_head` è abilitato, vengono disegnati solo i keypoint della testa e il punto del collo. Se entrambi sono disabilitati, non viene disegnato alcun keypoint del corpo o della testa.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | Un'immagine con i keypoint della posa disegnati. Le dimensioni dell'immagine corrispondono a `canvas_height` e `canvas_width` specificati nei dati dei keypoint di input. Quando l'input contiene più fotogrammi, viene restituito un batch di immagini. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/it.md)

---
**Source fingerprint (SHA-256):** `2b2b9530b55c56e278666bd5d139bb6a1bb503b75b948a89266b9982b5a295e4`

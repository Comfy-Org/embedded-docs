# Pixal3DMultiViewConditioning

Il nodo Pixal3D Multi-View Conditioning costruisce dati di condizionamento da un rig di camere con orbita fissa: viste frontale, sinistra, posteriore e destra posizionate a 90 gradi l'una dall'altra, utilizzate esattamente come inquadrate. Collega almeno una vista quadrata dell'oggetto e prepara dati di condizionamento positivo e negativo corrispondenti per i modelli Pixal3D.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision con pesi NAF inclusi. | CLIP_VISION | Sì | N/A |
| `fov` | FOV orizzontale in gradi delle viste come inquadrate: 20 per render del rig e per la maggior parte dei generatori multi-view, oppure MoGeGeometryToFOV su una delle viste per le foto. Predefinito: 20.0. | FLOAT | Sì | 1.0 - 170.0 |
| `front` | Vista quadrata del lato frontale dell'oggetto, con alpha o su sfondo nero, inquadrata come nel rig: l'oggetto occupa circa 1/1.1 della cornice nella sua larghezza massima, alla stessa scala in ogni vista. La prima vista collegata (ordine front, left, back, right) è la vista frontale a cui viene orientata la mesh. | IMAGE | No | N/A |
| `left` | Vista quadrata del lato sinistro dell'oggetto, con alpha o su sfondo nero, inquadrata come nel rig: l'oggetto occupa circa 1/1.1 della cornice nella sua larghezza massima, alla stessa scala in ogni vista. La prima vista collegata (ordine front, left, back, right) è la vista frontale a cui viene orientata la mesh. | IMAGE | No | N/A |
| `back` | Vista quadrata del lato posteriore dell'oggetto, con alpha o su sfondo nero, inquadrata come nel rig: l'oggetto occupa circa 1/1.1 della cornice nella sua larghezza massima, alla stessa scala in ogni vista. La prima vista collegata (ordine front, left, back, right) è la vista frontale a cui viene orientata la mesh. | IMAGE | No | N/A |
| `right` | Vista quadrata del lato destro dell'oggetto, con alpha o su sfondo nero, inquadrata come nel rig: l'oggetto occupa circa 1/1.1 della cornice nella sua larghezza massima, alla stessa scala in ogni vista. La prima vista collegata (ordine front, left, back, right) è la vista frontale a cui viene orientata la mesh. | IMAGE | No | N/A |

### Note

- Almeno una vista deve essere collegata; il nodo genera un errore se tutti e quattro gli input vista sono vuoti.
- La prima vista collegata, nell'ordine front, left, back, right, viene considerata la vista frontale, e la mesh viene orientata verso quella vista. Se la prima vista collegata non è `front`, viene registrato un avviso che indica che la mesh verrà orientata con quella vista come vista frontale.
- Le viste vengono lette nell'ordine front, left, back, right e posizionate sull'orbita ai loro azimuth fissi rispetto alla prima vista collegata.
- Le viste di input con un canale alpha hanno l'alpha applicato su sfondo nero. Le viste che non sono 1024 x 1024 vengono ridimensionate a 1024 x 1024.
- La dimensione del batch viene presa dalla prima vista collegata. Se le viste collegate hanno dimensioni del batch diverse, quelle più piccole vengono ripetute ciclicamente per allinearsi.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `positive` | L'output di condizionamento positivo, costruito dalle viste codificate e dalle relative feature proiettate. | CONDITIONING |
| `negative` | L'output di condizionamento negativo, costruito da embedding azzerati con le stesse feature proiettate. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DMultiViewConditioning/it.md)

---
**Source fingerprint (SHA-256):** `e6319ebd1a557dbb48269bab8a667e78e48f446d87fffbd9df4c4ebfb62b0fac`

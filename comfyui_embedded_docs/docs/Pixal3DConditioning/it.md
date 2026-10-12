# Pixal3DConditioning

Il nodo Pixal3DConditioning prepara il condizionamento delle immagini per la pipeline di generazione 3D Trellis2. Utilizza un modello di visione DINOv3 per estrarre feature visive dall'immagine di input a due risoluzioni (512 e 1024), quindi le organizza in mappe di feature per ogni stadio che possono essere opzionalmente potenziate da un modello NAF. Le informazioni sulla fotocamera sono derivate dal campo visivo orizzontale per costruire la matrice di trasformazione di proiezione, e il nodo restituisce una coppia di condizionamento positiva (feature derivate dall'immagine più dati di proiezione) e una coppia di condizionamento negativa (tensori di feature azzerati) per la guida senza classificatore.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision. | CLIP_VISION | Sì | — |
| `image` | Immagine preprocessata da ImageCropToMask (pad_factor=1.1 per Pixal3D). | IMAGE | Sì | — |
| `camera_angle_x` | FOV orizzontale in gradi (visualizzato come `fov`). Collega un MoGeGeometryToFOV (axis='horizontal', unit='degrees') per un FoV per immagine (corrisponde al default upstream). Predefinito: 49.13. | FLOAT | Sì | 1.0 – 170.0 (step 0.01) |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `positive` | L'output di condizionamento positivo contenente le mappe di feature derivate dall'immagine e i dati di proiezione per la generazione Trellis2. | CONDITIONING |
| `negative` | L'output di condizionamento negativo con tensori di feature azzerati, utilizzato per la guida senza classificatore. | CONDITIONING |

Nota: il valore `camera_angle_x` viene convertito internamente da gradi a radianti, e la distanza della fotocamera viene calcolata da esso per costruire la matrice di trasformazione di proiezione. Quando il modello di visione fornito include un componente NAF, il nodo produce anche mappe di feature ad alta risoluzione per gli stadi di forma e texture.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/it.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`

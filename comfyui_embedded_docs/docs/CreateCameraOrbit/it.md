# Create Camera Orbit

Costruisce un rig di camere attorno al target della prima camera: per impostazione predefinita una piattaforma girevole, una scansione inclinata quando `pitch` è impostato e, facoltativamente, viste direttamente dall'alto e dal basso. Render Mesh esegue il rendering di un'immagine per ciascuna camera e Bake Texture From Views le riproietta sulla mesh.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `camera_info` | Prima camera dell'orbita. Se viene fornito un elenco di camere, viene creata un'orbita per ciascuna camera in esso contenuta. | LOAD3D_CAMERA | Sì | - |
| `count` | Camere distribuite uniformemente lungo la scansione. Predefinito: 4. | INT | Sì | 1 a 64 |
| `yaw` | Rotazione totale attorno al target, nella direzione yaw di Create Camera Info. I giri completi si fermano un passo prima della prima camera; le altre scansioni terminano sull'ultima camera. Predefinito: 360.0. | FLOAT | Sì | -720.0 a 720.0 (passo 1.0) |
| `pitch` | Inclinazione totale rispetto al target; i valori positivi salgono come il pitch di Create Camera Info; oltre 90 le camere passano sopra la sommità. I giri completi si ripetono come `yaw`. Predefinito: 0.0. | FLOAT | Sì | -720.0 a 720.0 (passo 1.0) |
| `poles` | Viste direttamente dall'alto e/o dal basso rivolte al target, aggiunte dopo l'orbita. La parte superiore delle loro immagini punta in direzione opposta alla prima camera. Predefinito: `"none"`. | COMBO | Sì | `"none"`<br>`"top"`<br>`"bottom"`<br>`"top and bottom"` |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `camera_info` | L'elenco delle camere del rig, nell'ordine dell'orbita seguito dalle viste polari. | LOAD3D_CAMERA |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateCameraOrbit/it.md)

---
**Source fingerprint (SHA-256):** `b251efc969f8db7cf03527594be3bbd2af037f1ebb56bdf508bf264ddd9f8c08`

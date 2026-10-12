# WanCameraEmbedding

Questo nodo genera un embedding della traiettoria della camera utilizzando gli embedding di Plücker per il percorso della camera scelto. Costruisce una sequenza di pose della camera simulando movimenti come panoramica, zoom o rotazione, e le converte in un tensore di embedding che può essere utilizzato nelle pipeline di generazione video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `camera_pose` | Il tipo di movimento della camera da simulare (predefinito: "Static") | COMBO | Sì | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" |
| `width` | La larghezza dell'output in pixel (predefinito: 832, passo: 16) | INT | Sì | da 16 a MAX_RESOLUTION |
| `height` | L'altezza dell'output in pixel (predefinito: 480, passo: 16) | INT | Sì | da 16 a MAX_RESOLUTION |
| `length` | La lunghezza della sequenza della traiettoria della camera (predefinito: 81, passo: 4) | INT | Sì | da 1 a MAX_RESOLUTION |
| `speed` | La velocità del movimento della camera (predefinito: 1.0, passo: 0.1) | FLOAT | No | da 0.0 a 10.0 |
| `fx` | Il parametro di lunghezza focale x (predefinito: 0.5, passo: 0.000000001) | FLOAT | No | da 0.0 a 1.0 |
| `fy` | Il parametro di lunghezza focale y (predefinito: 0.5, passo: 0.000000001) | FLOAT | No | da 0.0 a 1.0 |
| `cx` | La coordinata x del punto principale (predefinito: 0.5, passo: 0.01) | FLOAT | No | da 0.0 a 1.0 |
| `cy` | La coordinata y del punto principale (predefinito: 0.5, passo: 0.01) | FLOAT | No | da 0.0 a 1.0 |

Nota: `fx`, `fy`, `cx` e `cy` sono parametri intrinseci avanzati della camera. Il parametro `speed` scala l'angolo di rotazione e la distanza di traslazione del movimento della camera selezionato.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `camera_embedding` | Il tensore di embedding della camera generato contenente la sequenza della traiettoria | TENSOR |
| `width` | Il valore di larghezza utilizzato per l'elaborazione | INT |
| `height` | Il valore di altezza utilizzato per l'elaborazione | INT |
| `length` | Il valore di lunghezza utilizzato per l'elaborazione | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/it.md)

---
**Source fingerprint (SHA-256):** `1a2f98d83d18033581823dee61b5a3686d560c749c55223f81febca89654a29f`

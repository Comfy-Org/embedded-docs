# MiniMax H3 Max Camera Control

Questo nodo genera un video che parte da un'immagine statica e sposta la camera verso un nuovo angolo e una nuova distanza attorno al soggetto. Azimut, elevazione e distanza descrivono dove termina la camera; il primo fotogramma rimane esattamente come fornito. Quando non viene fornito alcun prompt, la scena resta congelata e si muove solo la camera.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello da utilizzare per la generazione video. | DYNAMIC_COMBO | Sì | "MiniMax H3 Max" |

### Input di MiniMax H3 Max

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | Primo fotogramma del video, almeno 256x256 pixel. Le proporzioni devono essere comprese tra 0.4 e 2.5. | IMAGE | Sì | Immagine singola |
| `camera_info` | Camera finale opzionale, ad esempio da Create Camera Info o Compose Camera Angle Prompt, con l'immagine come vista frontale. Quando è collegata, imposta l'azimut e l'elevazione. | LOAD3D_CAMERA | No | Info camera |
| `prompt` | Opzionale. Se vuoto, la scena resta congelata e si muove solo la camera. | STRING | Sì | da 0 a 50000 caratteri |
| `azimuth` | Orbita orizzontale attorno al soggetto alla fine del video, in gradi rispetto all'immagine (predefinito: 90). I valori positivi spostano la camera verso destra, quindi il soggetto ruota verso il lato sinistro dell'inquadratura. È un valore target: un'orbita di 90 gradi spesso si attesta tra 30 e 90 gradi. Ignorato quando `camera_info` è collegato. | INT | Sì | da -360 a 360 |
| `elevation` | Angolo verticale della camera alla fine del video, in gradi (predefinito: 0). I valori positivi inquadrano dall'alto verso il basso, i valori negativi inquadrano dal basso verso l'alto. Ignorato quando `camera_info` è collegato. | INT | Sì | da -90 a 90 |
| `distance` | Distanza della camera alla fine del video rispetto all'immagine: 1 la mantiene, un valore inferiore a 1 avvicina, un valore superiore a 1 allontana (predefinito: 1.0). | FLOAT | Sì | da 0.1 a 10.0 |
| `duration` | Durata del video in output in secondi (predefinito: 5). | INT | Sì | da 1 a 15 |
| `resolution` | Risoluzione del video in output (predefinito: "768P"). | COMBO | Sì | "480P"<br>"768P"<br>"1080P" |
| `prompt_expansion_mode` | Quanto impegno viene dedicato alla riscrittura del prompt prima della generazione (predefinito: "balanced"). | COMBO | Sì | "disabled"<br>"balanced"<br>"quality" |
| `seed` | Seme casuale. La stessa richiesta con lo stesso seed produce risultati simili, ma non necessariamente identici (predefinito: 42). | INT | Sì | da 0 a 4294967295 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `video` | Il video generato con il movimento della camera applicato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxCameraControlNode/it.md)

---
**Source fingerprint (SHA-256):** `d9eed1a3ae91891b974bea39ea00101c0577cf5b204d4c701b13b232e0604153`

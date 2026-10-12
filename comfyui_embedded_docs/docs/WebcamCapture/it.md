# WebcamCapture

Il nodo WebcamCapture acquisisce immagini da un dispositivo webcam e le converte in un formato utilizzabile all'interno dei flussi di lavoro ComfyUI. Eredita dal nodo LoadImage e fornisce opzioni per controllare le dimensioni e la tempistica di acquisizione. Quando è abilitato, il nodo può acquisire nuove immagini ogni volta che la coda del flusso di lavoro viene elaborata.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | La sorgente di input webcam da cui acquisire le immagini | WEBCAM | Sì | - |
| `width` | La larghezza desiderata per l'immagine acquisita (predefinito: 0, usa la risoluzione nativa della webcam) | INT | Sì | 0 a MAX_RESOLUTION |
| `height` | L'altezza desiderata per l'immagine acquisita (predefinito: 0, usa la risoluzione nativa della webcam) | INT | Sì | 0 a MAX_RESOLUTION |
| `capture_on_queue` | Se abilitato, acquisisce una nuova immagine ogni volta che la coda del flusso di lavoro viene elaborata (predefinito: True) | BOOLEAN | Sì | - |

**Nota:** Quando sia `width` sia `height` sono impostati a 0, il nodo usa la risoluzione nativa della webcam. Impostare una delle due dimensioni su un valore diverso da zero ridimensionerà l'immagine acquisita di conseguenza.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `IMAGE` | L'immagine webcam acquisita convertita nel formato immagine di ComfyUI | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WebcamCapture/it.md)

---
**Source fingerprint (SHA-256):** `551368150fc293309f917eabaa066f223b1fa1a016ffd3643b57b80c83f812cc`

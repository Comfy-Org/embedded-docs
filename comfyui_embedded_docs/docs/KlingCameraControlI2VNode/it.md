# KlingCameraControlI2VNode

Il nodo Kling Image to Video Camera Control trasforma immagini fisse in video cinematografici con movimenti di camera professionali. Questo nodo specializzato image-to-video consente di controllare azioni virtuali della camera, tra cui zoom, rotazione, pan, tilt e visuale in prima persona, mantenendo al contempo il focus sull'immagine originale. Il controllo della camera è attualmente supportato solo in modalità pro con il modello kling-v1-5 a una durata di 5 secondi.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `start_frame` | Immagine di riferimento - URL o stringa codificata Base64, non può superare 10MB, risoluzione non inferiore a 300x300px, proporzioni tra 1:2.5 e 2.5:1. Base64 non deve includere il prefisso data:image. | IMAGE | Sì | - |
| `prompt` | Prompt testuale positivo che descrive il contenuto video desiderato. La lunghezza massima è di 500 caratteri. | STRING | Sì | - |
| `negative_prompt` | Prompt testuale negativo che descrive ciò che va evitato nel video generato. La lunghezza massima è di 500 caratteri. | STRING | Sì | - |
| `cfg_scale` | Controlla la forza della guida testuale. Valori più alti fanno sì che l'output segua più fedelmente il prompt (default: 0.75) | FLOAT | No | 0.0 to 1.0 |
| `aspect_ratio` | Le proporzioni del video generato (default: "16:9") | COMBO | No | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `camera_control` | Può essere creato utilizzando il nodo Kling Camera Controls. Controlla il movimento della camera e il movimento durante la generazione del video. | CAMERA_CONTROL | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | L'output video generato | VIDEO |
| `video_id` | Identificatore univoco per il video generato | STRING |
| `duration` | Durata del video generato | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/it.md)

---
**Source fingerprint (SHA-256):** `65b1e4a46c2de1558c8f27ebe031f1736e84d532908170c91fb70121c350347e`

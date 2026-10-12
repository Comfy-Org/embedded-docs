# KlingCameraControlT2VNode

Il nodo Kling Text to Video Camera Control trasforma il testo in video cinematografici con movimenti di camera professionali che simulano la cinematografia del mondo reale. Questo nodo supporta il controllo di azioni di camera virtuale tra cui zoom, rotazione, pan, tilt e visuale in prima persona, mantenendo l'attenzione sul testo originale. La durata, la modalità e il nome del modello sono codificati in modo fisso perché il controllo della camera è supportato solo in modalità pro con il modello kling-v1-5 a una durata di 5 secondi.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale positivo | STRING | Sì | - |
| `negative_prompt` | Prompt testuale negativo | STRING | Sì | - |
| `cfg_scale` | Controlla quanto fedelmente l'output segue il prompt (predefinito: 0.75) | FLOAT | No | 0.0-1.0 |
| `aspect_ratio` | Il rapporto d'aspetto del video generato (predefinito: "16:9") | COMBO | No | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"3:4"<br>"4:3" |
| `camera_control` | Può essere creato utilizzando il nodo Kling Camera Controls. Controlla il movimento e la dinamica della camera durante la generazione del video. | CAMERA_CONTROL | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il video generato con effetti di controllo della camera | VIDEO |
| `video_id` | L'identificatore univoco del video generato | STRING |
| `duration` | La durata del video generato | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlT2VNode/it.md)

---
**Source fingerprint (SHA-256):** `7975d97c4f9242a9ae3c17be03696d174a2495bd53fb9fc4405f86c44167fa21`

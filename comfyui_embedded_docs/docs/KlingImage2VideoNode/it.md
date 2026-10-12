# Kling Immagine (Primo Frame) in Video

Il nodo Kling Image to Video genera un breve video utilizzando un'immagine iniziale come primo fotogramma. Combina l'immagine con prompt testuali e impostazioni di generazione, quindi restituisce il video risultante insieme al suo ID e alla sua durata.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `start_frame` | L'immagine di riferimento utilizzata per generare il video. L'immagine deve essere di almeno 300x300 pixel e avere un rapporto d'aspetto compreso tra 1:2.5 e 2.5:1. | IMAGE | Sì | - |
| `prompt` | Prompt testuale positivo. Non deve essere vuoto. Massimo 500 caratteri. | STRING | Sì | - |
| `negative_prompt` | Prompt testuale negativo. Massimo 500 caratteri. Lasciare vuoto se non utilizzato. | STRING | Sì | - |
| `model_name` | Il modello utilizzato per la generazione del video. | COMBO | Sì | `"kling-v2-5-turbo"` |
| `cfg_scale` | Controlla quanto fedelmente il video segue il prompt. Valori più alti indicano un'aderenza maggiore (predefinito: 0.8). | FLOAT | Sì | 0.0 a 1.0 |
| `mode` | La modalità di generazione. | COMBO | Sì | `"pro"` |
| `aspect_ratio` | Il rapporto d'aspetto del video generato (predefinito: `"16:9"`). | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La durata del video generato in secondi (predefinito: `"5"`). | COMBO | Sì | `"5"`<br>`"10"` |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | L'output video generato. | VIDEO |
| `video_id` | Identificatore univoco del video generato. | STRING |
| `duration` | Informazioni sulla durata del video generato. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/it.md)

---
**Source fingerprint (SHA-256):** `f4a461819bc05f92d867bddcc78a66ad7beaa10707ef8cae3e7eb9e6f72c890a`

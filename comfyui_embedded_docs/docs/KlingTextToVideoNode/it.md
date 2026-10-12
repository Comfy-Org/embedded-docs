# Kling Da Testo a Video

Il nodo Kling Text to Video genera video a partire da descrizioni testuali usando l'API di generazione video Kling. Invia il prompt e le impostazioni (proporzioni, modalità di generazione e scala CFG) all'API, attende il completamento dell'attività di generazione e restituisce il video risultante insieme al relativo ID e alla durata.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale positivo | STRING | Sì | Massimo 2500 caratteri |
| `negative_prompt` | Prompt testuale negativo | STRING | No | Massimo 2500 caratteri |
| `cfg_scale` | Valore di scala di configurazione che controlla quanto fedelmente il video segue il prompt (predefinito: 1.0) | FLOAT | No | da 0.0 a 1.0 |
| `aspect_ratio` | Impostazione delle proporzioni del video (predefinito: "16:9") | COMBO | No | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | La configurazione da utilizzare per la generazione del video secondo il formato: mode / duration / model_name (predefinito: "pro mode / 5s duration / kling-v2-5-turbo") | COMBO | No | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

Nota: il parametro `prompt` è obbligatorio e non deve essere vuoto. Sia `prompt` che `negative_prompt` sono limitati a un massimo di 2500 caratteri. L'opzione `mode` da 10 secondi costa più di quella da 5 secondi.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il video generato | VIDEO |
| `video_id` | Identificatore univoco del video generato | STRING |
| `duration` | Informazioni sulla durata del video generato | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`

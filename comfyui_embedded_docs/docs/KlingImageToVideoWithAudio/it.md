# Kling 2.6 Immagine (Primo Frame) in Video con Audio

Il nodo Kling Image(First Frame) to Video with Audio utilizza il modello Kling AI per generare un breve video a partire da una singola immagine di partenza e da un prompt testuale. Crea una sequenza video che inizia con l'immagine fornita e può includere facoltativamente audio generato dall'IA per accompagnare la parte visiva.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model_name` | La versione specifica del modello Kling AI da utilizzare per la generazione video. | COMBO | Sì | `"kling-v2-6"` |
| `start_frame` | L'immagine che fungerà da primo fotogramma del video generato. L'immagine deve avere almeno 300x300 pixel e un rapporto d'aspetto compreso tra 1:2.5 e 2.5:1. | IMAGE | Sì | - |
| `prompt` | Prompt testuale positivo. Descrive il contenuto video che si desidera generare. Il prompt deve contenere da 1 a 2500 caratteri. | STRING | Sì | - |
| `mode` | La modalità operativa per la generazione video. | COMBO | Sì | `"pro"` |
| `duration` | La durata del video da generare, in secondi. | COMBO | Sì | `5`<br>`10` |
| `generate_audio` | Se abilitato, il nodo genererà audio per accompagnare il video. Se disabilitato, il video sarà silenzioso. (predefinito: True) | BOOLEAN | No | - |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `video` | Il file video generato, che può includere audio a seconda dell'input `generate_audio`. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/it.md)

---
**Source fingerprint (SHA-256):** `e0b834a297f7afd72cfb779a92557f0dc680eacd4d0e18bab0e7c59ae8624965`

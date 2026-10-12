# KlingTextToVideoWithAudio

Il nodo Kling Text to Video with Audio genera un breve video da una descrizione testuale. Invia una richiesta al servizio Kling AI, che elabora il prompt e restituisce un file video. Il nodo può anche generare l'audio di accompagnamento per il video in base al testo.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model_name` | Il modello AI specifico da utilizzare per la generazione del video. | COMBO | Sì | `"kling-v2-6"` |
| `prompt` | Prompt testuale positivo. La descrizione utilizzata per generare il video. Deve contenere tra 1 e 2500 caratteri. | STRING | Sì | - |
| `mode` | La modalità operativa per la generazione del video. | COMBO | Sì | `"pro"` |
| `aspect_ratio` | Il rapporto larghezza-altezza desiderato per il video generato. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La durata del video in secondi. | COMBO | Sì | `5`<br>`10` |
| `generate_audio` | Controlla se viene generato l'audio per il video. Quando è abilitato, l'IA creerà l'audio in base al prompt (predefinito: `True`). | BOOLEAN | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/it.md)

---
**Source fingerprint (SHA-256):** `ddd2f3c1799abac067a05f3f5d6442ad4fe023d2f4f9afbde2894ca66854977e`

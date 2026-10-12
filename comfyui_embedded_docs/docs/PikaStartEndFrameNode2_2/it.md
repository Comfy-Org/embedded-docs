# PikaStartEndFrameNode2_2

Il nodo PikaFrames v2.2 genera un video combinando il frame iniziale e quello finale. Carichi due immagini per definire i punti di inizio e fine, e l'IA crea una transizione fluida tra di esse per produrre un video completo.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image_start` | La prima immagine da combinare. | IMAGE | Sì | - |
| `image_end` | L'ultima immagine da combinare. | IMAGE | Sì | - |
| `prompt_text` | Prompt testuale che descrive il contenuto video desiderato. | STRING | Sì | - |
| `negative_prompt` | Testo che descrive cosa evitare nel video. | STRING | Sì | - |
| `seed` | Valore seed casuale per la coerenza della generazione. | INT | Sì | - |
| `resolution` | Risoluzione del video in output. | STRING | Sì | - |
| `duration` | Durata del video generato. | INT | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Il video generato che combina i frame iniziale e finale con transizioni IA. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/it.md)

---
**Source fingerprint (SHA-256):** `0a26f6db754c61d1f35e3fd9faceb631a8103ce9ff38190a5dd637991914e238`

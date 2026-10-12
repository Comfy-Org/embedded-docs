# Concatena video

Concatena più segmenti video in un unico video, preservando l'ordine in cui sono collegati. Gli input codificati compatibili vengono combinati senza essere decodificati, e una traccia audio separata opzionale può essere fornita per sostituire l'audio originale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `videos` | Segmenti video da concatenare nell'ordine di input. Collega da 1 a 100 video; ogni video appare come uno slot di input separato etichettato `video_1`, `video_2`, ecc. | VIDEO | Sì | da 1 a 100 segmenti |
| `codec` | Codec utilizzato per codificare i tensori video. L'opzione auto usa H.264; i video già codificati rimangono invariati. Predefinito: "auto" | COMBO | Sì | `"auto"`<br>Altre opzioni sono definite dai tipi di codec video disponibili. |
| `complete_audio` | Traccia audio completa opzionale per il video concatenato. Sostituisce l'audio dei video di input. | AUDIO | No | N/A |

**Nota:** L'input `videos` accetta da 1 a 100 segmenti video. Se viene fornito `complete_audio`, sostituisce l'audio di tutti i video di input. Quando `codec` è impostato su "auto", gli input codificati compatibili vengono concatenati senza decodifica.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `VIDEO` | Il video concatenato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConcatenateVideo/it.md)

---
**Source fingerprint (SHA-256):** `f591aecb83754127e1c86ed0488548f9e7d99f3559c95a1c86c55fa5d430713d`

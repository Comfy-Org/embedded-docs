# Luma Ray 3.2 Da Immagine a Video

Genera un video da un frame iniziale e/o finale utilizzando il modello Ray 3.2 di Luma. Le generazioni ancorate a immagini hanno sempre una durata di 5 secondi.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per la generazione del video. | STRING | Sì | 1 a 6000 caratteri |
| `resolution` | La risoluzione di output del video generato (predefinita: "720p"). | COMBO | Sì | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `loop` | Fa sì che il video si ripeta senza interruzioni. Non disponibile quando è impostato un `end_frame`. | BOOLEAN | Sì | True<br>False |
| `seed` | Valore di seed per una generazione riproducibile. | INT | Sì | 0 a 2147483647 |
| `start_frame` | Primo frame del video generato. | IMAGE | No | - |
| `end_frame` | Ultimo frame del video generato. | IMAGE | No | - |

**Nota:** È necessario fornire almeno uno tra `start_frame` o `end_frame`. Se vengono forniti entrambi, il video generato eseguirà una transizione dal frame iniziale al frame finale. L'opzione `loop` non può essere abilitata quando è impostato un `end_frame`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | L'output video generato. | VIDEO |
| `generation_id` | L'identificatore univoco per la richiesta di generazione. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `ff479c196f10153ffa09af6acfb4e286d1934aa28a5e9b413613097a2cfb5f2a`

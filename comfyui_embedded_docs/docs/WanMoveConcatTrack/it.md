# WanMoveConcatTrack

Il nodo WanMoveConcatTrack combina due insiemi di dati di tracciamento del movimento in un'unica sequenza più lunga. Funziona unendo i percorsi delle tracce e le maschere di visibilità dagli input di traccia lungo le rispettive dimensioni. Se viene fornito un solo input di traccia, passa semplicemente quei dati invariati.

## Input
| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `tracks_1` | Il primo insieme di dati di tracciamento del movimento da concatenare. | TRACKS | Sì |  |
| `tracks_2` | Un secondo insieme opzionale di dati di tracciamento del movimento. Se non fornito, `tracks_1` viene passato direttamente all'output. | TRACKS | No |  |

## Output
| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `tracks` | I dati di tracciamento del movimento concatenati, contenenti `track_path` e `track_visibility` combinati dagli input. Restituisce `tracks_1` invariato quando `tracks_2` non è collegato. | TRACKS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/it.md)

---
**Source fingerprint (SHA-256):** `0507c42dce5d481fe5dc5aa1116c9df279f236419f548ea3eff5d824d0d22653`

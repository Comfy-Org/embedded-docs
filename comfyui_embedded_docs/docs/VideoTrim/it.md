# Taglia video (avanzato)

Questo nodo ritaglia un video in una finestra temporale scelta impostando un tempo di inizio e una durata. Offre anche una modalità rigorosa che genera un errore quando la durata richiesta non può essere raggiunta.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Il video da ritagliare. | VIDEO | Sì | — |
| `trim` | Finestra di ritaglio usando i frame di inizio/fine. La finestra viene convertita in un tempo di inizio (in secondi dall'inizio del video) e in una durata (in secondi). Quando sia il tempo di inizio sia la durata sono 0, il video viene restituito senza alcun ritaglio. | VIDEO_EDIT | Sì | start_time: >= 0, default 0<br>duration: >= 0, default 0 |
| `strict_duration` | Se True, quando la durata specificata non è possibile, viene generato un errore. (predefinito: False) | BOOLEAN | No | true<br>false |

Nota: La durata del ritaglio deve essere >= 0; i valori negativi generano un errore. La finestra di ritaglio richiesta deve rientrare nel video sorgente. Se il ritaglio non può essere applicato, viene generato un errore che riporta la durata del video sorgente, il tempo di inizio e la durata target.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Il video ritagliato. Quando la finestra di ritaglio è vuota (tempo di inizio e durata entrambi 0), il video originale viene restituito invariato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTrim/it.md)

---
**Source fingerprint (SHA-256):** `ba8f8ccbae7e8aebda553810b81ccaa427d45523142bd00746c4e2f4e5b41a1b`

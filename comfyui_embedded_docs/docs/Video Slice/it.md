# Taglia Video

Il nodo Video Slice consente di estrarre un segmento specifico da un video. È possibile definire un tempo di inizio e una durata per ritagliare il video, oppure saltare semplicemente i fotogrammi iniziali. Se la durata richiesta è maggiore del video rimanente, il nodo può restituire la parte disponibile oppure generare un errore.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video` | Il video di input da ritagliare. | VIDEO | Sì | - |
| `start_time` | Tempo di inizio in secondi (predefinito: 0.0). | FLOAT | Sì | da -1e5 a 1e5 |
| `duration` | Durata in secondi, oppure 0 per durata illimitata (predefinito: 0.0). | FLOAT | Sì | 0.0 e oltre |
| `strict_duration` | Se True, quando la durata specificata non è possibile, viene generato un errore (predefinito: False). | BOOLEAN | Sì | - |

**Nota:** Se il video non può essere ritagliato con i valori specificati di `start_time` e `duration`, il nodo genera un errore. Quando `strict_duration` è False, il nodo restituisce la porzione disponibile del video se la durata richiesta supera la lunghezza rimanente; quando è True, genera invece un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `video` | Il segmento video ritagliato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/it.md)

---
**Source fingerprint (SHA-256):** `439b76528742c1fbe230eee9502e945847ae99a58a9bd81a7a7dc3b20e15d450`

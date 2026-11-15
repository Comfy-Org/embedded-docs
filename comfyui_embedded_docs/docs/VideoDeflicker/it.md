# Video Deflicker

Rimuove lo sfarfallio temporale da un video elaborato, in modo che ogni fotogramma mantenga i propri dettagli seguendo il movimento dei fotogrammi vicini. È pensato per filmati che pulsano dopo essere stati ingranditi o elaborati fotogramma per fotogramma: collega il modello di flusso ottico e i fotogrammi con sfarfallio e, facoltativamente, una copia stabile della sorgente come guida.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `optical_flow` | Modello di flusso ottico dal nodo Load Optical Flow Model (torchvision RAFT-large). | OPTICAL_FLOW | Sì | - |
| `images` | Fotogrammi con sfarfallio da stabilizzare, ad esempio un video che è stato ingrandito o elaborato fotogramma per fotogramma. | IMAGE | Sì | - |
| `guide` | Fotogrammi sorgente stabili di cui seguire il movimento, a qualsiasi risoluzione. Il valore predefinito è `images`, che rimuove meno sfarfallio. | IMAGE | No | - |
| `strength` | Quanto fortemente ogni fotogramma segue i propri vicini (predefinito: 1.0). Valori più alti rimuovono più sfarfallio e ammorbidiscono maggiormente i dettagli fini; 0 restituisce i fotogrammi invariati. | FLOAT | Sì | 0.0 a 100.0 (passo: 0.1) |
| `direction` | Direzione della passata. `bidirectional` calcola la media di una passata in avanti e una all'indietro, il che evita di rimanere in ritardo rispetto al movimento; `forward` esegue una singola passata. (predefinito: `bidirectional`) | COMBO | Sì | `"bidirectional"`<br>`"forward"` |
| `threshold` | Le modifiche superiori a questa soglia tra un fotogramma e il suo vicino compensato dal movimento vengono considerate reali e levigate meno (predefinito: 0.1). 0 leviga allo stesso modo ogni cambiamento. | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `IMAGE` | Fotogrammi senza sfarfallio, con la stessa dimensione e lo stesso numero di fotogrammi di `images`. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoDeflicker/it.md)

---
**Source fingerprint (SHA-256):** `d9937a67b0ac33ef3b326017e7d7990474705917902f1097cfeb06d9f83322a1`

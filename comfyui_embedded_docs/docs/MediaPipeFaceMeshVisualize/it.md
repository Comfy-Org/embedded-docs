# Visualizza Punti di Riferimento del Viso (MediaPipe)

## Panoramica

Disegna i punti di riferimento del volto e le linee di connessione (una mesh facciale) sopra un'immagine di input. Questo nodo utilizza i dati dei landmark prodotti da un nodo di rilevamento del volto per visualizzare le caratteristiche facciali rilevate, come occhi, naso, bocca e contorno del volto.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `face_landmarks` | I dati dei landmark del volto provenienti da un nodo di rilevamento. | FACE_LANDMARKS | Sì |  |
| `image` | L'immagine su cui disegnare la mesh. Se non è collegata, verrà utilizzata una tela nera della stessa dimensione del risultato di rilevamento. | IMAGE | No |  |
| `connections` | Determina quali parti della mesh facciale disegnare. `"all"` disegna la mesh completa (ovale, occhi, sopracciglia, labbra, iridi, naso). `"fill"` disegna un poligono pieno dell'ovale del volto (maschera silhouette). `"custom"` consente di attivare o disattivare ogni caratteristica singolarmente. (predefinito: `"all"`) | COMBO | Sì | `"all"`<br>`"fill"`<br>`"custom"` |
| `color` | Il colore delle linee e dei punti della mesh. (predefinito: `#00ff00`) | COLOR | Sì |  |
| `thickness` | Lo spessore in pixel delle linee della mesh. Impostandolo a 0 si disabilita il disegno delle linee. (predefinito: 1) | INT | Sì | 0 to 8 |
| `point_size` | Il raggio in pixel dei punti dei landmark. Impostandolo a 0 si disabilita il disegno dei punti. (predefinito: 2) | INT | Sì | 0 to 16 |

**Nota sul parametro `connections`:** Quando è selezionato `"custom"`, compaiono input booleani aggiuntivi per ciascuna caratteristica facciale (ad es., `face_oval`, `lips`, `left_eye`, `right_eye`, `left_eyebrow`, `right_eyebrow`, `left_iris`, `right_iris`, `nose`, `tesselation`). Verranno disegnate solo le caratteristiche abilitate.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `IMAGE` | L'immagine di input con la mesh dei landmark del volto disegnata sopra. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMeshVisualize/it.md)

---
**Source fingerprint (SHA-256):** `fb5437d73378b0c8daa68669c2e19058ccb7133ed68fc51c8d4c5bab8662f243`

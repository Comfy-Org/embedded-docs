# UnwrapMesh

Genera un atlante UV per una mesh 3D. La superficie della mesh viene suddivisa in chart, ogni chart viene appiattito in due dimensioni e i chart appiattiti vengono impacchettati in un atlante UV [0,1]. I vertici sulle giunzioni dei chart vengono duplicati (una copia per chart, stessa posizione, UV propri), quindi la mesh di output può contenere più vertici della mesh di input e le facce di output possono differire nel numero rispetto all'input.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `mesh` | La mesh di input da srotolare (unwrap). Accetta una singola mesh o un batch di mesh; i batch vengono elaborati un elemento alla volta. | MESH | Sì | — |
| `segmenter` | Algoritmo di charting da usare. `pec`: charting veloce con collasso parallelo degli edge su GPU. `adaptive`: CPU, più lento. (predefinito: "pec") | COMBO | Sì | "pec"<br>"adaptive" |
| `resolution` | Risoluzione target dell'atlante per la scalatura automatica della densità di texel (0 = adatta al contenuto). (predefinito: 1024) | INT | Sì | da 0 a 8192 (passo 256) |
| `padding` | Padding in texel tra i chart. (predefinito: 1) | INT | Sì | da 0 a 16 |
| `weld_distance` | Raggio di fusione dei vertici coincidenti come frazione dell'estensione della mesh (0 = auto). Aumentalo a ~0.001 se ottieni chart per triangolo (input non saldato). (predefinito: 0.0) | FLOAT | Sì | da 0.0 a 1.0 (passo 0.0001) |

Nota: se la mesh di input contiene vertici non saldati, il nodo può avvisare che l'adiacenza tra facce è bassa e produrre chart UV per faccia; aumentare `weld_distance` fonde i vertici coincidenti prima dell'unwrap. Le facce degeneri (facce che riutilizzano lo stesso indice di vertice) vengono scartate durante l'elaborazione.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `mesh` | La mesh di input con un atlante UV generato nell'intervallo [0,1]. I vertici sulle giunzioni (seam) vengono duplicati, quindi il numero di vertici di output può superare quello di input. I colori dei vertici e la texture della mesh di input vengono preservati. | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/it.md)

---
**Source fingerprint (SHA-256):** `fcab6f0b621693d862ee74b5ec498498d2f1f247a66f478704377598a6b39388`

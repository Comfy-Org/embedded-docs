# WanMoveVisualizeTracks

Il nodo WanMoveVisualizeTracks sovrappone i dati di tracciamento del movimento su una sequenza di immagini o fotogrammi video. Disegna rappresentazioni visive dei punti tracciati, inclusi i loro percorsi di movimento e le posizioni attuali, rendendo i dati di movimento visibili e più facili da analizzare.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `images` | La sequenza di immagini di input o fotogrammi video su cui visualizzare i tracciati. | IMAGE | Sì | - |
| `tracks` | I dati di tracciamento del movimento contenenti i percorsi dei punti e le informazioni di visibilità. Se non forniti, le immagini di input vengono passate invariate. | TRACKS | No | - |
| `line_resolution` | Il numero di fotogrammi precedenti da utilizzare quando si disegna la linea del percorso per ogni traccia (predefinito: 24). | INT | Sì | 1 - 1024 |
| `circle_size` | La dimensione del cerchio disegnato nella posizione corrente di ciascuna traccia (predefinito: 12). Contrassegnato come parametro avanzato. | INT | Sì | 1 - 128 |
| `opacity` | L'opacità delle sovrapposizioni delle tracce disegnate (predefinito: 0.75). | FLOAT | Sì | 0.0 - 1.0 |
| `line_width` | La larghezza delle linee utilizzate per disegnare i percorsi delle tracce (predefinito: 16). Contrassegnato come parametro avanzato. | INT | Sì | 1 - 128 |

**Nota:** Se il numero di immagini di input non corrisponde al numero di fotogrammi nei dati `tracks` forniti, la sequenza di immagini verrà ripetuta per corrispondere alla lunghezza della traccia.

**Nota:** I punti della traccia vengono disegnati con un insieme limitato di colori ripetuti, e un punto viene saltato in un fotogramma quando il suo flag di visibilità è zero per quel fotogramma.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | La sequenza di immagini con i dati di tracciamento del movimento visualizzati come sovrapposizioni. Se non sono stati forniti `tracks`, vengono restituite le immagini di input originali. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/it.md)

---
**Source fingerprint (SHA-256):** `d94bfde28dfdad682edcc81b1c63408f1352e0dbc94af4d043d750e8cd4c099b`

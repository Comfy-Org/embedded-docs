# DA3GeometryToMesh

Questo nodo converte un pacchetto DA3_GEOMETRY in una mesh 3D retroproiettando la mappa di profondità e triangolando la nuvola di punti risultante. Elabora una singola immagine da un batch e produce una mesh con texture o senza texture adatta al rendering 3D.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `da3_geometry` | Il pacchetto DA3_GEOMETRY contenente la mappa di profondità, la mappa di confidenza opzionale, la mappa del cielo opzionale e l'immagine sorgente | DA3_GEOMETRY | Sì | - |
| `batch_index` | Quale immagine di un batch convertire. I conteggi dei vertici per immagine differiscono, quindi i batch non possono essere impilati (predefinito: 0). Deve essere inferiore alla dimensione del batch della geometria di input, altrimenti viene generato un errore | INT | Sì | 0 a 4096 |
| `decimation` | Passo dei vertici. 1 = risoluzione completa, 2 = metà, ecc. (predefinito: 1) | INT | Sì | 1 a 8 |
| `discontinuity_threshold` | Elimina i triangoli la cui ampiezza di profondità 3x3 supera questa frazione. 0 = disattivato (predefinito: 0.04) | FLOAT | Sì | 0.0 a 1.0 |
| `confidence_threshold` | Esclude i pixel la cui confidenza normalizzata per immagine è inferiore a questo valore. 0 = mantieni tutti, 1 = mantieni solo il singolo pixel con maggiore confidenza. Usato quando la geometria dispone di una mappa di confidenza (modelli Small/Base) (predefinito: 0.1) | FLOAT | Sì | 0.0 a 1.0 |
| `use_sky_mask` | Esclude dalla mesh i pixel con probabilità di cielo (cielo >= 0.5). Usato quando la geometria dispone di una mappa del cielo (modelli Mono/Metric) (predefinito: True) | BOOLEAN | Sì | True o False |
| `texture` | Usa l'immagine sorgente come texture di colore di base (predefinito: True) | BOOLEAN | Sì | True o False |

I pixel con valori di profondità non finiti, zero o negativi vengono sempre esclusi dalla mesh. Viene generato un errore se la mesh risultante è vuota; il messaggio di errore suggerisce di aumentare `discontinuity_threshold`, ridurre `confidence_threshold` o disabilitare `use_sky_mask`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `MESH` | Una mesh 3D triangolata con vertici, facce, coordinate UV e texture opzionale | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToMesh/it.md)

---
**Source fingerprint (SHA-256):** `1d311223a8d131030bcd4930d21852a21ac9dd5758e7f8b8d20b1cf68698893b`

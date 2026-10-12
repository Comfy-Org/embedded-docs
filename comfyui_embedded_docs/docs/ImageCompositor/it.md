# ImageCompositor

Questo nodo combina più livelli immagine in un'unica immagine composita. Prende uno stack di livelli creato con il nodo Add Layer e, facoltativamente, applica le impostazioni di composizione salvate dall'editor del compositor, fondendo i livelli in base al loro posizionamento, dimensione, rotazione, opacità e modalità di fusione. Una composizione salvata che corrisponde agli input correnti ha la priorità; in caso contrario, il nodo compone dalle proprietà dei livelli e contrassegna lo stato salvato come obsoleto.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `layers` | Stack di livelli da comporre; crealo con Add Layer. Gli elementi sono impilati per z_index, i frame in batch all'interno di un elemento si espandono in livelli consecutivi, e il posizionamento, l'opacità e la modalità di fusione dell'elemento definiscono la composizione iniziale. Senza una tela del documento esplicita, la dimensione è un'estensione massima approssimativa dei livelli posizionati. Una composizione salvata che corrisponde agli input correnti ha la priorità. | LAYERS | Sì | Massimo 50 livelli |
| `compositor` | Composizione a livelli salvata dall'editor del compositor. | COMPOSITOR | No | Nessuno |

**Note sui vincoli:**

- Lo stack di livelli supporta un massimo di 50 livelli espansi; fornirne di più genera un errore.
- Attualmente sono supportati solo elementi di livello raster; altri tipi di elemento generano un errore.
- La versione del documento `layers` deve essere 1; altre versioni generano un errore.
- Lo stato `compositor` salvato viene riprodotto solo quando le impronte digitali degli input registrate corrispondono allo stack di livelli corrente. Se non corrispondono, il nodo esegue il fallback alla composizione dalle proprietà dei livelli e contrassegna lo stato salvato come obsoleto.
- L'opacità del livello viene limitata all'intervallo 0.0 - 1.0.
- Il posizionamento orizzontale e verticale del livello (`x`, `y`) viene limitato al limite massimo di risoluzione.
- La larghezza e l'altezza del livello tornano alla dimensione naturale dell'immagine quando impostate a zero o meno, e vengono limitate al limite massimo di risoluzione.
- La dimensione della tela composita non deve superare il limite massimo di risoluzione.
- Quando non vengono forniti livelli, viene restituita un'immagine segnaposto 64x64.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `IMAGE` | Immagine composita. Include un canale alfa quando la composizione ha aree trasparenti (ad es. sfondo nascosto), altrimenti RGB semplice. | IMAGE |
| `MASK` | Trasparenza della composizione (1 = completamente trasparente). Tutti zeri quando la composizione è opaca. | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositor/it.md)

---
**Source fingerprint (SHA-256):** `76e5e57ade89f9ee172c5e1f0b82579d846d15bafb52b2052246f1f2ad7f0034`

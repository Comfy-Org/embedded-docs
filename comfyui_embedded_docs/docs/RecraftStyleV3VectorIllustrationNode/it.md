# RecraftStyleV3VectorIllustrationNode

Questo nodo seleziona uno stile per l'API Recraft, in particolare la categoria di stile illustrazione vettoriale. È possibile scegliere facoltativamente un sottostile più specifico all'interno di tale categoria. Il nodo restituisce un oggetto di configurazione dello stile che può essere passato ad altri nodi Recraft.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `substyle` | Uno stile più specifico all'interno della categoria illustrazione vettoriale. Le opzioni disponibili sono i sottostili definiti per lo stile `vector_illustration` dall'API Recraft. Se non viene scelto alcun sottostile, viene utilizzato lo stile base `vector_illustration`. | COMBO | Sì | Più opzioni disponibili (elenco dei sottostili caricato dinamicamente per lo stile `vector_illustration`) |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `recraft_style` | Un oggetto di configurazione dello stile Recraft contenente lo stile illustrazione vettoriale selezionato e il sottostile opzionale. Può essere collegato ad altri nodi Recraft. | STYLEV3 |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3VectorIllustrationNode/it.md)

---
**Source fingerprint (SHA-256):** `e88e7ea35b18acb55ec59814981cb36451d922d3287d23dcdb504289ea9f541b`

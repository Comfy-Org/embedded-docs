# Grok Image

Il nodo Grok Image genera una o più immagini da una descrizione testuale utilizzando il modello AI Grok. Invia il prompt a un servizio esterno e restituisce le immagini generate come tensori che possono essere utilizzati nel flusso di lavoro.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello Grok specifico da utilizzare per la generazione di immagini. Modelli diversi possono offrire qualità, velocità o funzionalità variabili. | COMBO | Sì | `"grok-imagine-image-2.0"`<br>`"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `prompt` | Il prompt testuale utilizzato per generare l'immagine. Questa descrizione guida l'AI su cosa creare. Deve contenere almeno 1 carattere (il testo composto solo da spazi non è accettato). | STRING | Sì | N/A |
| `aspect_ratio` | Il rapporto larghezza-altezza desiderato per l'immagine generata. | COMBO | Sì | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `number_of_images` | Numero di immagini da generare (predefinito: 1). | INT | Sì | da 1 a 10 |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi non sono deterministici indipendentemente dal seed (predefinito: 0). | INT | Sì | da 0 a 2147483647 |
| `resolution` | La risoluzione di output desiderata per le immagini generate (predefinita: "1K"). | COMBO | No | `"1K"`<br>`"2K"` |
| `quality` | Livello di qualità, supportato solo dal modello `grok-imagine-image-2.0` (predefinito: "medium"; "low" è una delle opzioni disponibili). Per tutti gli altri modelli, questa impostazione viene ignorata. | COMBO | No | Più opzioni disponibili |

**Nota:** Il parametro `seed` viene utilizzato principalmente per controllare quando il nodo viene rieseguito all'interno di un flusso di lavoro. A causa della natura del servizio AI esterno, le immagini generate non saranno riproducibili o identiche tra le esecuzioni, anche con un seed identico.

**Nota sui prezzi:** Il costo per generare immagini dipende dal `model`, `resolution`, `quality` e `number_of_images` selezionati. Per il modello `grok-imagine-image-2.0`, la qualità "low" costa $0.04 per immagine a risoluzione 1K e $0.06 per immagine a risoluzione 2K; gli altri livelli di qualità costano $0.06 per immagine a 1K e $0.08 per immagine a 2K. Il modello `grok-imagine-image-quality` costa $0.05 per immagine a risoluzione 1K e $0.07 per immagine a risoluzione 2K. Il modello `grok-imagine-image-pro` costa $0.07 per immagine. Il modello `grok-imagine-image` costa $0.02 per immagine.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `output` | L'immagine generata o un batch di immagini. Se `number_of_images` è 1, viene restituito un singolo tensore immagine. Se è maggiore di 1, viene restituito un batch di tensori immagine. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/it.md)

---
**Source fingerprint (SHA-256):** `a89f5df0d4827f45013f1af92541d36b5b8c8edc8626e07af4fe2d85ee5486e7`

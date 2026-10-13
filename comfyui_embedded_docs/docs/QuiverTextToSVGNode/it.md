# Quiver Testo in SVG

Il nodo Quiver Text to SVG genera un'immagine SVG (Scalable Vector Graphic) da una descrizione testuale utilizzando i modelli di Quiver AI. Puoi facoltativamente fornire immagini di riferimento e istruzioni di stile per guidare il processo di generazione.

**Nota:** Questo nodo è contrassegnato come deprecato nel codice sorgente. Quiver ritira i modelli della serie Arrow 1 il 16 ottobre 2026, quindi le opzioni `arrow-1.1`, `arrow-1.1-max` e `arrow-preview` smettono di funzionare dopo tale data. Usa invece `arrow-2` o `arrow-2-telos`.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Descrizione testuale dell'output SVG desiderato. Questa è l'istruzione principale per ciò che deve essere generato. | STRING | Sì | N/D |
| `instructions` | Indicazioni aggiuntive di stile o formattazione. Questo è un parametro facoltativo e avanzato. | STRING | No | N/D |
| `reference_images` | Fino a 4 immagini di riferimento per guidare la generazione. Questo è un input facoltativo. | IMAGE | No | da 0 a 4 immagini |
| `model` | Modello da utilizzare per la generazione SVG. Selezionando un modello vengono rivelati parametri aggiuntivi specifici di quel modello: `temperature`, `top_p` e `presence_penalty`. | DYNAMIC_COMBO | Sì | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi non sono deterministici indipendentemente dal seed. Predefinito: 0. | INT | Sì | da 0 a 2147483647 |
| `reasoning_effort` | Quanto ragionamento il modello impiega prima di disegnare. Livelli più alti migliorano il dettaglio e costano più token. Utilizzato solo dai modelli Arrow 2 (predefinito: "high"). | COMBO | No | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |

**Nota:** L'input `reference_images` accetta un massimo di 4 immagini.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `SVG` | L'immagine SVG (Scalable Vector Graphic) generata. | SVG |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/it.md)

---
**Source fingerprint (SHA-256):** `e03e130a4aedbf003e898300b3a83e343fdfa5b3da35df20d55876d437bf5426`

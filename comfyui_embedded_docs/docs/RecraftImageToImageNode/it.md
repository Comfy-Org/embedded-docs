# RecraftImageToImageNode

Questo nodo modifica un'immagine esistente in base a un prompt testuale e a un'impostazione di forza (strength). Invia l'immagine all'API Recraft V3 e restituisce una nuova immagine che segue il prompt mantenendosi più o meno simile all'originale, a seconda del valore di strength.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da modificare. Quando viene fornito un batch di immagini, ogni immagine viene elaborata individualmente. | IMAGE | Sì | - |
| `prompt` | Prompt per la generazione dell'immagine. Predefinito: stringa vuota. Lunghezza massima: 1000 caratteri. | STRING | Sì | - |
| `n` | Il numero di immagini da generare. Predefinito: 1. | INT | Sì | 1-6 |
| `strength` | Definisce la differenza con l'immagine originale, deve essere compreso in [0, 1], dove 0 significa quasi identica, e 1 significa similarità minima. Predefinito: 0.5. | FLOAT | Sì | 0.0-1.0 (step 0.01) |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi sono non deterministici indipendentemente dal seed. Predefinito: 0. | INT | Sì | 0-18446744073709551615 |
| `recraft_style` | Selezione opzionale dello stile per la generazione dell'immagine. Se non fornito, il valore predefinito è `realistic_image`. | STYLEV3 | No | - |
| `negative_prompt` | Descrizione testuale opzionale di elementi indesiderati su un'immagine. Predefinito: stringa vuota. Fornito come socket di input. | STRING | No | - |
| `recraft_controls` | Controlli aggiuntivi opzionali sulla generazione tramite il nodo Recraft Controls. | CONTROLS | No | - |

**Nota:** Il parametro `seed` attiva solo la riesecuzione del nodo ma non garantisce risultati deterministici. Il parametro `strength` viene arrotondato a 2 cifre decimali internamente. Il `prompt` viene convalidato e non deve superare i 1000 caratteri. Un `negative_prompt` vuoto viene trattato come nessun prompt negativo. Se `recraft_style` non viene fornito, il nodo utilizza per impostazione predefinita lo stile `realistic_image`. Se si utilizza uno `style_id` dalla Infinite Style Library, assicurarsi che non sia uno stile di arte vettoriale, poiché ciò potrebbe causare la ricezione di dati SVG invece di un'immagine da parte del nodo, con conseguente errore. Quando l'input `image` è un batch, ogni immagine nel batch viene elaborata individualmente e tutti i risultati vengono restituiti insieme.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | L'immagine o le immagini generate in base all'immagine di input, al prompt e a strength. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/it.md)

---
**Source fingerprint (SHA-256):** `1932e55d1dc392e6bd42a0bd29f5aaba44b65997b597648a927fba38a27c90ad`

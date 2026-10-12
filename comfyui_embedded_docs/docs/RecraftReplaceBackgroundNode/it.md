# RecraftReplaceBackgroundNode

Sostituisce lo sfondo dell'immagine, in base al prompt fornito. Questo nodo utilizza l'API Recraft per generare nuovi sfondi per le tue immagini in base alla tua descrizione testuale, consentendoti di trasformare completamente lo sfondo mantenendo intatto il soggetto principale. Ogni immagine nel batch di input viene elaborata separatamente e i risultati vengono combinati in un unico batch di output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da elaborare | IMAGE | Sì | - |
| `prompt` | Prompt per la generazione dell'immagine (predefinito: vuoto) | STRING | Sì | - |
| `n` | Il numero di immagini da generare (predefinito: 1) | INT | Sì | 1-6 |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi sono non deterministici indipendentemente dal seed (predefinito: 0) | INT | Sì | 0-18446744073709551615 |
| `recraft_style` | Selezione opzionale dello stile per lo sfondo generato. Se non fornito, il valore predefinito è lo stile "realistic_image" | STYLEV3 | No | - |
| `negative_prompt` | Descrizione testuale opzionale degli elementi indesiderati su un'immagine (predefinito: vuoto) | STRING | No | - |

**Note:**
- Il parametro `seed` controlla quando il nodo viene rieseguito ma non garantisce risultati deterministici a causa della natura dell'API esterna.
- Quando `recraft_style` non è collegato o viene lasciato vuoto, il nodo utilizza lo stile `realistic_image` come fallback.
- Quando `negative_prompt` viene lasciato vuoto, non viene inviato con la richiesta.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine(o) generata(e) con lo sfondo sostituito. Per ogni immagine di input, il numero di risultati generati è determinato da `n`. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/it.md)

---
**Source fingerprint (SHA-256):** `45a2607ae73cc67caa98d33bf536feda83a2021d960dec7cca76cbe0b9fc47ef`

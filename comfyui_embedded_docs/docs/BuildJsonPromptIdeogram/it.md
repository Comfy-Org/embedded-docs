# BuildJsonPromptIdeogram

This node constructs a structured JSON prompt specifically formatted for the Ideogram 4 image generation model. It organizes your text instructions, style preferences, camera or art details, lighting, medium, and optional color palette into the required JSON structure that the model expects.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `element` | Elementi del prompt dal nodo Create Bounding Boxes. | ARRAY | Sì | - |
| `high_level_description` | Descrizione opzionale dell'immagine in una o due frasi. Fortemente consigliata. (predefinito: vuoto) | STRING | No | - |
| `background` | Descrizione obbligatoria dello sfondo o dell'ambiente dell'immagine. Si consiglia vivamente di fornire un valore: il nodo verrà eseguito con una stringa vuota, ma i risultati potrebbero essere imprevedibili. (predefinito: vuoto) | STRING | No | - |
| `style` | La categoria di stile visivo per l'immagine generata. Seleziona una delle opzioni. (predefinito: "none") | COMBO | Sì | `"none"`<br>`"photo"`<br>`"art_style"` |
| `photo` | Dettagli di fotocamera o obiettivo per output fotografici (ad es. 35mm, f/1.4, bokeh). Disponibile solo quando `style` è impostato su "photo". (predefinito: vuoto) | STRING | No | - |
| `art_style` | Descrizione dello stile artistico (ad es. flat vector illustration, bold outlines). Disponibile solo quando `style` è impostato su "art_style". (predefinito: vuoto) | STRING | No | - |
| `aesthetics` | Parole chiave estetiche obbligatorie (ad es. moody, cinematic, desaturated). Si consiglia vivamente di fornire un valore. (predefinito: vuoto) | STRING | No | - |
| `lighting` | Descrizione obbligatoria dell'illuminazione (ad es. golden hour, rim light, dramatic shadows). Si consiglia vivamente di fornire un valore. (predefinito: vuoto) | STRING | No | - |
| `medium` | Tipo di medium obbligatorio (ad es. photograph, illustration, 3d_render, painting, graphic_design). Quando style = photo, impostare su photograph. Si consiglia vivamente di fornire un valore. (predefinito: vuoto) | STRING | No | - |
| `color_palette` | Codici colore esadecimali che guidano i colori dominanti dell'immagine. Fino a 16 voci. | COLORS | No | - |

**Nota:** Quando `style` è impostato su "photo", l'input `photo` diventa disponibile e di solito dovresti impostare `medium` su "photograph". Quando `style` è impostato su "art_style", l'input `art_style` diventa disponibile. I parametri `background`, `aesthetics`, `lighting` e `medium` hanno stringhe vuote predefinite ma sono considerati obbligatori per una generazione affidabile dell'immagine; si consiglia vivamente di fornire dei valori.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `prompt` | Un dizionario JSON strutturato contenente la descrizione di alto livello, la descrizione dello stile (se è selezionato uno stile diverso da "none") e la scomposizione compositiva con sfondo ed elementi. | DICT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BuildJsonPromptIdeogram/it.md)

---
**Source fingerprint (SHA-256):** `56a045e0c7c19531e6443696c0bdf3946df066d03eea7d2d217b7d92f052592f`

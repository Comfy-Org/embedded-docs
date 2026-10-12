# RecraftImageInpaintingNode

Questo nodo modifica aree specifiche di un'immagine in base a un prompt testuale e a una maschera. Utilizza l'API Recraft per modificare in modo intelligente solo le regioni mascherate, mantenendo invariato il resto dell'immagine.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | L'immagine di input da modificare | IMAGE | Sì | - |
| `mask` | La maschera che definisce quali aree dell'immagine devono essere modificate | MASK | Sì | - |
| `prompt` | Prompt per la generazione dell'immagine (predefinito: stringa vuota, lunghezza massima: 1000 caratteri) | STRING | Sì | - |
| `n` | Il numero di immagini da generare (predefinito: 1, minimo: 1, massimo: 6) | INT | Sì | 1-6 |
| `seed` | Seme per determinare se il nodo deve essere rieseguito; i risultati effettivi sono non deterministici indipendentemente dal seme (predefinito: 0) | INT | Sì | 0-18446744073709551615 |
| `recraft_style` | Parametro di stile opzionale per l'API Recraft. Se non fornito, il valore predefinito è lo stile "realistic_image" | STYLEV3 | No | - |
| `negative_prompt` | Descrizione testuale opzionale degli elementi indesiderati in un'immagine (predefinito: stringa vuota) | STRING | No | - |

*Nota: `image` e `mask` devono essere forniti insieme affinché l'operazione di inpainting funzioni. La maschera verrà ridimensionata automaticamente per corrispondere alle dimensioni dell'immagine. Il `prompt` viene convalidato e ha una lunghezza massima di 1000 caratteri. Se viene utilizzato uno `style_id` della Infinite Style Library, assicurarsi che non sia uno stile Vector art, poiché ciò potrebbe causare la restituzione di dati SVG invece di un'immagine da parte dell'API.*

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `image` | L'immagine o le immagini modificate generate in base al prompt e alla maschera. Restituisce un'immagine per ogni immagine di input moltiplicata per il parametro `n` | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/it.md)

---
**Source fingerprint (SHA-256):** `539a49aec582f529a13059388222c3998e22d52618738843d9b2b6e0fb1ea5c3`

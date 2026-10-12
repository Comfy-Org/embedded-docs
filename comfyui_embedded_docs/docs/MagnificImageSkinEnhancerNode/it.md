# Magnific Image Skin Enhancer

Il nodo Magnific Image Skin Enhancer applica un'elaborazione AI specializzata alle immagini di ritratto per migliorare l'aspetto della pelle. Offre tre modalità distinte per diversi obiettivi di miglioramento: creative per effetti artistici, faithful per preservare l'aspetto originale e flexible per miglioramenti mirati come illuminazione o realismo. Il nodo carica l'immagine su un'API esterna per l'elaborazione e restituisce il risultato migliorato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di ritratto da migliorare. | IMAGE | Sì | - |
| `sharpen` | Livello di intensità della nitidezza (predefinito: 0). | INT | No | 0 a 100 |
| `smart_grain` | Livello di intensità della grana intelligente (predefinito: 2). | INT | No | 0 a 100 |
| `mode` | La modalità di elaborazione da usare. `"creative"` è per il miglioramento artistico, `"faithful"` per preservare l'aspetto originale e `"flexible"` per un'ottimizzazione mirata. | COMBO | Sì | `"creative"`<br>`"faithful"`<br>`"flexible"` |
| `skin_detail` | Livello di miglioramento dei dettagli della pelle. Questo input è disponibile solo quando `mode` è impostato su `"faithful"` (predefinito: 80). | INT | No | 0 a 100 |
| `optimized_for` | Obiettivo di ottimizzazione del miglioramento. Questo input è disponibile solo quando `mode` è impostato su `"flexible"`. | COMBO | No | `"enhance_skin"`<br>`"improve_lighting"`<br>`"enhance_everything"`<br>`"transform_to_real"`<br>`"no_make_up"` |

**Vincoli:**

* Il nodo accetta esattamente un'immagine di input.
* L'immagine di input deve avere altezza e larghezza minime di 160 pixel.
* Il rapporto d'aspetto dell'immagine di input deve essere compreso tra 1:3 e 3:1 (validazione non rigorosa).
* Il parametro `skin_detail` è attivo solo quando `mode` è impostato su `"faithful"`.
* Il parametro `optimized_for` è attivo solo quando `mode` è impostato su `"flexible"`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | L'immagine del ritratto migliorata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageSkinEnhancerNode/it.md)

---
**Source fingerprint (SHA-256):** `2430cc0fb1d2042a8eda78f7f5a5794fa6b4e555d3957616ae6891374b556a76`

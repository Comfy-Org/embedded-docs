# BeebleSwitchXImageEdit

Modifica una singola immagine con Beeble SwitchX. Questo nodo può cambiare qualsiasi elemento della scena (sfondo, illuminazione, costume) preservando i pixel originali del soggetto. Fornisci un'immagine di riferimento e/o un prompt testuale per descrivere il nuovo aspetto. La risoluzione massima è di circa 2,77 megapixel.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di origine da modificare. | IMAGE | Sì | - |
| `prompt` | Una descrizione testuale del nuovo aspetto desiderato (ad es. "un cavaliere in armatura scintillante"). | STRING | Sì | - |
| `alpha_mode` | Come gestire la maschera alpha. `"select"` usa un keyframe per selezionare il soggetto, `"fill"` sostituisce l'intera immagine senza una maschera separata, `"custom"` usa una maschera fornita dall'utente. | COMBO | Sì | `"select"`<br>`"fill"`<br>`"custom"` |
| `max_resolution` | La risoluzione massima per l'immagine di output. Una risoluzione più alta costa più crediti. | COMBO | Sì | `"1080p"`<br>`"720p"` |
| `seed` | Un valore di seed per la riproducibilità. | INT | Sì | - |
| `reference_image` | Un'immagine di riferimento opzionale per guidare lo stile o l'aspetto dei nuovi elementi della scena. | IMAGE | No | - |

**Nota su `alpha_mode`:** Quando `alpha_mode` è impostato su `"select"`, devi anche fornire un `alpha_keyframe` (un'immagine keyframe usata per selezionare il soggetto). Quando è impostato su `"custom"`, devi fornire un `alpha_mask` (una maschera creata dall'utente). Quando è impostato su `"fill"`, non è necessario alcun input alpha.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine modificata con gli elementi della scena sostituiti. | IMAGE |
| `alpha` | La maschera alpha usata da Beeble. Vuota per la modalità `"fill"`, che non ha una maschera separata. | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXImageEdit/it.md)

---
**Source fingerprint (SHA-256):** `6fd10dff6ac4f1a15fd05de7a6ff6eda988e60dd4ef32bc8c792480fbbf0c92b`

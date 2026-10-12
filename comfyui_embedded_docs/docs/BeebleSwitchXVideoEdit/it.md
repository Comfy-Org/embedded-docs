# BeebleSwitchXVideoEdit

Modifica un video con Beeble SwitchX. Questo nodo può sostituire qualsiasi elemento della scena (sfondo, illuminazione, costume) preservando i pixel e il movimento del soggetto originale. Fornisci un'immagine di riferimento e/o un prompt testuale per descrivere il nuovo aspetto. Massimo 240 frame, massimo circa 2,77 megapixel per frame.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Il video di input da modificare. | VIDEO | Sì | N/A |
| `prompt` | Una descrizione testuale del nuovo aspetto desiderato per la scena. | STRING | Sì | N/A |
| `alpha_mode` | La modalità della matte alpha. La modalità "fill" non ha una matte separata e riempie l'intero frame. La modalità "select" usa una singola immagine keyframe per definire l'area da modificare. La modalità "custom" usa un video alpha completo per definire l'area da modificare frame per frame. | COMBO | Sì | `"fill"`<br>`"select"`<br>`"custom"` |
| `max_resolution` | La risoluzione massima per il video di output (predefinita: "1080p"). | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `seed` | Un valore di seed per la riproducibilità. Usando lo stesso seed con gli stessi input si otterrà lo stesso risultato. | INT | Sì | 0 a 2147483647 |
| `reference_image` | Un'immagine di riferimento opzionale che descrive il nuovo aspetto desiderato per la scena. | IMAGE | No | N/A |

### Dettagli sulla modalità alpha

Il parametro `alpha_mode` controlla quali parti del video vengono modificate:

- **fill**: L'intero frame del video viene modificato. Non viene prodotta alcuna matte alpha separata.
- **select**: Fornisci una singola immagine keyframe che definisce l'area da modificare. Il nodo la userà per determinare quali parti del video modificare.
- **custom**: Fornisci un video alpha completo che definisce l'area da modificare frame per frame. Questo ti dà un controllo preciso su quali parti di ogni frame vengono modificate.

Quando usi la modalità `select`, devi fornire l'immagine `alpha_keyframe`. Quando usi la modalità `custom`, devi fornire il video `alpha_mask`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video modificato con le modifiche alla scena applicate. | VIDEO |
| `alpha` | La matte alpha usata da Beeble. È vuota per la modalità "fill", che non ha una matte separata. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXVideoEdit/it.md)

---
**Source fingerprint (SHA-256):** `a92e78e6a08ac01466d953562a250b812eb8b1a5fb37efce6fddd7aa1ef380a2`

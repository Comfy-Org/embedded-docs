# RunwayAleph2KeyframeNode

Il nodo Runway Aleph2 Keyframe ancora un'immagine di guida a un momento specifico del video di input, così il modello Aleph2 indirizza la modifica in quel punto del filmato. Collega questo nodo all'input "keyframes" del nodo Runway Aleph2 Video to Video e concatenane diversi insieme (fino a 5) tramite l'input opzionale "keyframes".

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | L'immagine di guida da applicare nel momento scelto del video di input. | IMAGE | Sì | - |
| `timing` | Come posizionare questa immagine sulla timeline del video di input. | COMBO | Sì | "Absolute seconds"<br>"Fraction of duration" |
| `keyframes` | Keyframe precedenti opzionali da concatenare con questo. | KEYFRAME | No | - |

### Dettagli del parametro `timing`

Il parametro `timing` ha due modalità:

- **"Absolute seconds"**: Quando selezionato, appare un sottoparametro `seconds`. Specifica il tempo in secondi dall'inizio del video di input in cui l'immagine viene applicata (predefinito: 0.0, intervallo: da 0.0 a 30.0, passo 0.1).
- **"Fraction of duration"**: Quando selezionato, appare un sottoparametro `fraction`. Specifica in quale punto del video di input l'immagine viene applicata come frazione della sua durata, dove 0.0 è l'inizio e 1.0 è la fine (predefinito: 0.0, intervallo: da 0.0 a 1.0, passo 0.01).

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `keyframes` | Una catena di keyframe che include questo e tutti i keyframe collegati in precedenza. | KEYFRAME |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2KeyframeNode/it.md)

---
**Source fingerprint (SHA-256):** `b5ac6553166b7366fd35f97740861be163f91bc2353f5f83bdc2f04bf40f8478`

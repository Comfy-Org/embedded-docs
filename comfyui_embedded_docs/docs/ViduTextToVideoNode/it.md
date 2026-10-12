# ViduTextToVideoNode

Il nodo Vidu Text To Video Generation crea video a partire da descrizioni testuali. Utilizza il modello di generazione video Vidu per trasformare i prompt testuali in contenuti video con impostazioni personalizzabili per durata, proporzioni e stile visivo.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Nome del modello | COMBO | Sì | `viduq1` |
| `prompt` | Una descrizione testuale per la generazione video | STRING | Sì | - |
| `duration` | Durata del video di output in secondi (predefinito: 5) | INT | No | 5-5 |
| `seed` | Seed per la generazione video (0 per casuale) (predefinito: 0) | INT | No | 0-2147483647 |
| `aspect_ratio` | Le proporzioni del video di output | COMBO | No | `16:9`<br>`9:16`<br>`1:1` |
| `resolution` | I valori supportati possono variare in base al modello e alla durata | COMBO | No | `1080p` |
| `movement_amplitude` | L'ampiezza del movimento degli oggetti nell'inquadratura | COMBO | No | `auto`<br>`small`<br>`medium`<br>`large` |

**Nota:** Il campo `prompt` è obbligatorio e non può essere vuoto. Il parametro `duration` è attualmente fisso a 5 secondi.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `output` | Il video generato in base al prompt testuale | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `913efbb516c40e03ced1fef59905c7efa7737f0506368c9afcacb3b65aa4af66`

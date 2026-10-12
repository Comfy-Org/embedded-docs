# Luma Da Testo a Immagine

Genera immagini in modo sincrono in base a un prompt testuale e a un rapporto d'aspetto. Questo nodo crea immagini utilizzando descrizioni testuali e consente di controllare le dimensioni e lo stile dell'immagine tramite vari input di riferimento, incluse immagini di personaggi e di stile.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt per la generazione dell'immagine (predefinito: stringa vuota). Deve contenere almeno 3 caratteri. | STRING | Sì | - |
| `model` | Selezione del modello per la generazione di immagini. Modelli diversi hanno costi diversi. | COMBO | Sì | `photon-flash-1`<br>`photon-1`<br>`photon` |
| `aspect_ratio` | Rapporto d'aspetto per l'immagine generata (predefinito: `16:9`) | COMBO | Sì | `16:9`<br>`1:1`<br>`4:3`<br>`3:2`<br>`21:9`<br>`9:16`<br>`3:4`<br>`2:3`<br>`9:21` |
| `seed` | Seme per determinare se il nodo deve essere rieseguito; i risultati effettivi non sono deterministici indipendentemente dal seme (predefinito: 0) | INT | Sì | 0 to 18446744073709551615 |
| `style_image_weight` | Peso dell'immagine di stile. Ignorato se non viene fornita `style_image` (predefinito: 1.0) | FLOAT | No | 0.0 to 1.0 |
| `image_luma_ref` | Connessione del nodo Luma Reference per influenzare la generazione con immagini di input; è possibile considerare fino a 4 immagini. | LUMA_REF | No | - |
| `style_image` | Immagine di riferimento di stile; verrà utilizzata solo 1 immagine. | IMAGE | No | - |
| `character_image` | Immagini di riferimento del personaggio; può essere un batch di più immagini, è possibile considerare fino a 4 immagini. | IMAGE | No | - |

**Vincoli dei parametri:**

- Il `prompt` deve contenere almeno 3 caratteri dopo aver rimosso gli spazi bianchi.
- Il parametro `image_luma_ref` può accettare fino a 4 immagini di riferimento.
- Il parametro `character_image` può accettare fino a 4 immagini di riferimento del personaggio.
- Il parametro `style_image` accetta solo 1 immagine di riferimento di stile.
- Il parametro `style_image_weight` viene utilizzato solo quando viene fornita `style_image`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `output` | L'immagine generata in base ai parametri di input. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode/it.md)

---
**Source fingerprint (SHA-256):** `cde0fc1ace28523d658b757d7f829b0d20071bed391964d2d8caa81801265b46`

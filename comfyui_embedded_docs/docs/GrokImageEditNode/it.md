# GrokImageEditNode

Il nodo Grok Image Edit modifica un'immagine esistente in base a un prompt testuale. Invia l'immagine o le immagini di input e la descrizione all'API Grok e restituisce una o più immagini generate che seguono il prompt. Questo nodo è contrassegnato come deprecato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello AI specifico da utilizzare per la modifica delle immagini. | COMBO | Sì | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `image` | L'immagine o le immagini di input da modificare. | IMAGE | Sì |  |
| `prompt` | Il prompt testuale utilizzato per generare l'immagine. Testo multilinea; deve contenere almeno un carattere diverso dallo spazio bianco. | STRING | Sì |  |
| `resolution` | La risoluzione per l'immagine di output. | COMBO | Sì | `"1K"`<br>`"2K"` |
| `number_of_images` | Numero di immagini modificate da generare (predefinito: 1). | INT | Sì | da 1 a 10 |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi sono non deterministici indipendentemente dal seed (predefinito: 0). | INT | Sì | da 0 a 2147483647 |
| `aspect_ratio` | Il rapporto d'aspetto per l'immagine di output. Consentito solo quando più immagini sono collegate all'input `image` (predefinito: "auto"). | COMBO | No | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**Vincoli importanti:**
- L'input `image` supporta fino a 3 immagini, tranne quando si utilizza il modello `grok-imagine-image-pro`, che supporta solo 1 immagine di input.
- Il parametro `aspect_ratio` può essere impostato su un valore personalizzato (non "auto") solo quando più immagini sono collegate all'input `image`. L'impostazione di un rapporto d'aspetto personalizzato con una singola immagine di input causerà un errore.
- Il `prompt` deve contenere almeno un carattere diverso dallo spazio bianco.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | L'immagine o le immagini modificate generate dal nodo. Se viene generata più di un'immagine, le immagini vengono concatenate in un unico batch. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/it.md)

---
**Source fingerprint (SHA-256):** `e2ace07d10901c4e57086da8e3294a5d04e379103e9740131f5355cd4b07625d`

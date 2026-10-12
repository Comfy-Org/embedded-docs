# sync.so Talking Image

Anima un ritratto statico trasformandolo in un video parlante guidato da audio vocale, usando il modello sync-3 di sync.so. La durata dell'output corrisponde alla durata dell'audio e il costo è proporzionale alla durata dell'output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | Una singola immagine con un volto chiaramente visibile, fino a 4K (4096x2160). | IMAGE | Sì | È richiesta esattamente un'immagine |
| `audio` | Audio vocale che guida il video parlante; la durata dell'output corrisponde alla sua durata. Collega qui qualsiasi nodo TTS per guidare l'animazione a partire dal testo. | AUDIO | Sì | Durata massima: 600 secondi |
| `prompt` | Guida opzionale su come il ritratto prende vita, ad es. "fai sorridere il soggetto e fallo guardare verso la fotocamera". Lascia vuoto per un movimento naturale del parlato. (predefinito: "") | STRING | No | Testo multiriga |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 0) | INT | No | Da 0 a 2147483647 |
| `model` | Modello di generazione sync.so. L'input immagine è esclusivo di sync-3. | COMBO | Sì | `"sync-3"` |
| `speaker_selection` | Quale volto animare quando sono visibili più persone. `default`: lascia decidere al modello. `coordinates`: punta al volto al pixel (`speaker_x`, `speaker_y`) nell'immagine. Il rilevamento automatico non è supportato per le immagini. (predefinito: "default") | COMBO | No | `"default"`<br>`"coordinates"` |
| `speaker_x` | Coordinata X in pixel del volto dell'oratore. Usata solo quando `speaker_selection` è `"coordinates"`. (predefinito: 0) | INT | No | Da 0 a 4096 |
| `speaker_y` | Coordinata Y in pixel del volto dell'oratore. Usata solo quando `speaker_selection` è `"coordinates"`. (predefinito: 0) | INT | No | Da 0 a 4096 |
| `auto_downscale` | Ridimensiona automaticamente l'immagine verso il basso se supera il limite di input 4K (4096x2160); le coordinate dell'oratore vengono scalate di conseguenza. Se disabilitato, un'immagine di dimensioni eccessive genera invece un errore. (predefinito: True) | BOOLEAN | No | True<br>False |

**Nota:** I parametri `speaker_x` e `speaker_y` vengono usati solo quando `speaker_selection` è impostato su `"coordinates"`. Quando `auto_downscale` è abilitato, le coordinate dell'oratore vengono scalate automaticamente per corrispondere alle dimensioni dell'immagine ridimensionata.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Il video parlante generato con il ritratto animato sincronizzato con l'audio di input. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SyncTalkingImageNode/it.md)

---
**Source fingerprint (SHA-256):** `21f722cdcc5ff017949887ed2252854feebb9b913034dc6a6c3ce196ad089468`

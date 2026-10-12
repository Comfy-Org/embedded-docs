# ByteDanceImageNode

Il nodo ByteDance Image genera immagini usando modelli ByteDance tramite un'API basata su prompt testuali. Consente di selezionare un modello, specificare le dimensioni dell'immagine e controllare vari parametri di generazione come seed e scala di guidance. Il nodo si connette al servizio di generazione immagini di ByteDance e restituisce l'immagine creata.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello ByteDance da usare per la generazione delle immagini. Attualmente è disponibile una sola opzione di modello. | STRING | Sì | `"seedream-3-0-t2i-250415"` |
| `prompt` | Il prompt testuale usato per generare l'immagine. Deve contenere almeno 1 carattere dopo aver rimosso gli spazi bianchi. | STRING | Sì | - |
| `size_preset` | Scegli una dimensione consigliata. Seleziona Custom per usare larghezza e altezza indicate di seguito. I preset disponibili sono definiti dall'elenco `RECOMMENDED_PRESETS`. | STRING | Sì | Vedi descrizione |
| `width` | Larghezza personalizzata per l'immagine. Questo valore viene usato solo quando `size_preset` è impostato su `Custom`. Predefinito: 1024. | INT | Sì | 512 to 2048 (step 64) |
| `height` | Altezza personalizzata per l'immagine. Questo valore viene usato solo quando `size_preset` è impostato su `Custom`. Predefinito: 1024. | INT | Sì | 512 to 2048 (step 64) |
| `seed` | Seed da usare per la generazione. Predefinito: 0. | INT | No | 0 to 2147483647 (step 1) |
| `guidance_scale` | Un valore più alto fa sì che l'immagine segua più fedelmente il prompt. Predefinito: 2.5. | FLOAT | No | 1.0 to 10.0 (step 0.01) |
| `watermark` | Indica se aggiungere una filigrana "AI generated" all'immagine. Predefinito: False. Questo è un parametro avanzato. | BOOLEAN | No | True / False |

**Nota sui parametri di dimensione:** I parametri `width` e `height` vengono usati solo quando `size_preset` è impostato su `Custom`. Se viene selezionata una dimensione preset, le dimensioni del preset hanno la precedenza sui valori personalizzati di larghezza e altezza. Quando si usano dimensioni personalizzate, sia la larghezza sia l'altezza devono essere comprese tra 512 e 2048 pixel.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine generata restituita dall'API ByteDance come tensore. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/it.md)

---
**Source fingerprint (SHA-256):** `0b40c75ca43ef3cccbc644e64822f701a0d772decacd813c58d7d5ac60c230a1`

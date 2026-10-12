# FluxProCannyNode

Genera un'immagine utilizzando un'immagine di controllo (Canny). Questo nodo prende un'immagine di controllo e genera una nuova immagine basata sul prompt fornito, seguendo la struttura dei bordi rilevata nell'immagine di controllo.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `control_image` | L'immagine di input usata per il controllo del rilevamento dei bordi Canny | IMAGE | Sì | - |
| `prompt` | Prompt per la generazione dell'immagine (predefinito: stringa vuota) | STRING | No | - |
| `prompt_upsampling` | Indica se eseguire l'upsampling sul prompt. Se attivo, modifica automaticamente il prompt per una generazione più creativa, ma i risultati sono non deterministici (lo stesso seed non produrrà esattamente lo stesso risultato). (predefinito: False) | BOOLEAN | No | - |
| `canny_low_threshold` | Soglia bassa per il rilevamento dei bordi Canny; ignorata se `skip_preprocessing` è True (predefinito: 0.1) | FLOAT | No | 0.01 - 0.99 |
| `canny_high_threshold` | Soglia alta per il rilevamento dei bordi Canny; ignorata se `skip_preprocessing` è True (predefinito: 0.4) | FLOAT | No | 0.01 - 0.99 |
| `skip_preprocessing` | Indica se saltare la preelaborazione; impostare su True se `control_image` è già in formato Canny, False se è un'immagine grezza. (predefinito: False) | BOOLEAN | No | - |
| `guidance` | Forza di guidance per il processo di generazione dell'immagine (predefinito: 30) | FLOAT | No | 1 - 100 |
| `steps` | Numero di passaggi per il processo di generazione dell'immagine (predefinito: 50) | INT | No | 15 - 50 |
| `seed` | Il seed casuale usato per creare il rumore. (predefinito: 0) | INT | No | 0 - 18446744073709551615 |

**Nota:** Quando `skip_preprocessing` è impostato su True, i parametri `canny_low_threshold` e `canny_high_threshold` vengono ignorati poiché si presume che l'immagine di controllo sia già stata elaborata come immagine di bordi Canny. La `control_image` viene quindi utilizzata direttamente come immagine preelaborata.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output_image` | L'immagine generata in base all'immagine di controllo e al prompt | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProCannyNode/it.md)

---
**Source fingerprint (SHA-256):** `dedf55a2b2c183519d7f5be0d9a96abbe40716a247f574fc0d50f10f715949a7`

# BriaImageEditNode

Il nodo Bria FIBO Image Edit modifica un'immagine esistente utilizzando un'istruzione testuale. Invia l'immagine e il prompt all'API Bria, dove il modello FIBO crea una versione modificata. Una maschera opzionale può limitare le modifiche a un'area specifica.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | La versione del modello da utilizzare per la modifica dell'immagine. | COMBO | Sì | `"FIBO"` |
| `image` | L'immagine di input che si desidera modificare. | IMAGE | Sì | - |
| `prompt` | Istruzione per modificare l'immagine (predefinito: vuoto). | STRING | Sì | - |
| `negative_prompt` | Testo che descrive ciò che non si desidera visualizzare nell'immagine modificata (predefinito: vuoto). | STRING | Sì | - |
| `structured_prompt` | Una stringa contenente il prompt di modifica strutturato in formato JSON. Utilizzarlo al posto del prompt usuale per un controllo preciso e programmatico (predefinito: vuoto). | STRING | Sì | - |
| `seed` | Un numero utilizzato per inizializzare la generazione casuale, garantendo risultati riproducibili (predefinito: 1). | INT | Sì | 1 a 2147483647 |
| `guidance_scale` | Un valore più alto fa sì che l'immagine segua più fedelmente il prompt (predefinito: 3). | FLOAT | Sì | 3.0 a 5.0 |
| `steps` | Il numero di passaggi di denoising eseguiti dal modello (predefinito: 50). | INT | Sì | 20 a 50 |
| `moderation` | Impostazioni di moderazione. Selezionando `"true"` vengono mostrate opzioni di moderazione aggiuntive. | DYNAMIC_COMBO | Sì | `"false"`<br>`"true"` |
| `mask` | Se omesso, la modifica si applica all'intera immagine. | MASK | No | - |

### Input di moderazione

Quando `moderation` è impostato su `"true"`, questi input aggiuntivi diventano disponibili:

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt_content_moderation` | Indica se moderare il testo del prompt per contenuti inappropriati (predefinito: false). | BOOLEAN | No | `true`<br>`false` |
| `visual_input_moderation` | Indica se moderare l'immagine di input per contenuti inappropriati (predefinito: false). | BOOLEAN | No | `true`<br>`false` |
| `visual_output_moderation` | Indica se moderare l'immagine di output modificata per contenuti inappropriati (predefinito: true). | BOOLEAN | No | `true`<br>`false` |

**Vincoli importanti:**

- Almeno uno tra `prompt` e `structured_prompt` deve essere non vuoto. Se entrambi sono vuoti, il nodo genera un errore.
- Quando `moderation` è impostato su `"true"`, vengono mostrati i tre input di moderazione sopra.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine modificata restituita dall'API Bria. | IMAGE |
| `structured_prompt` | Il prompt strutturato utilizzato o generato durante il processo di modifica. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/it.md)

---
**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`

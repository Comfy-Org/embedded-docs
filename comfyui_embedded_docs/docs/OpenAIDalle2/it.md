# OpenAIDalle2

Genera immagini in modo sincrono tramite l'endpoint DALL·E 2 di OpenAI. Il nodo invia un prompt testuale all'API DALL·E 2 di OpenAI e restituisce l'immagine o le immagini risultanti a ComfyUI. Può anche modificare un'immagine esistente quando vengono forniti insieme un `image` e un `mask`.

## Come funziona

Questo nodo si connette all'API DALL·E 2 di OpenAI per creare immagini basate su descrizioni testuali. Quando fornisci un prompt testuale, il nodo lo invia ai server di OpenAI, che generano le immagini corrispondenti e le restituiscono a ComfyUI. Il nodo può operare in due modalità: generazione standard di immagini usando solo un prompt testuale, oppure modalità di modifica dell'immagine quando vengono forniti sia un'immagine che una maschera. In modalità modifica, usa la maschera per determinare quali parti dell'immagine originale devono essere modificate, mantenendo invariate le altre aree.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt testuale per DALL·E (predefinito: vuoto) | STRING | Sì | - |
| `seed` | non ancora implementato nel backend (predefinito: 0) | INT | No | da 0 a 2147483647 |
| `size` | Dimensione immagine (predefinito: "1024x1024") | COMBO | No | "256x256"<br>"512x512"<br>"1024x1024" |
| `n` | Quante immagini generare (predefinito: 1) | INT | No | da 1 a 8 |
| `image` | Immagine di riferimento opzionale per la modifica dell'immagine. | IMAGE | No | - |
| `mask` | Maschera opzionale per inpainting (le aree bianche saranno sostituite) | MASK | No | - |

**Nota:** La modalità di modifica dell'immagine viene attivata solo quando vengono forniti insieme sia `image` che `mask`. Se ne viene fornito solo uno, viene generato un errore. La `mask` deve avere le stesse dimensioni dell'`image`; in caso contrario, viene generato un errore. In modalità modifica, le aree bianche della maschera indicano le regioni che saranno sostituite.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `IMAGE` | L'immagine o le immagini generate o modificate da DALL·E 2 | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/it.md)

---
**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`

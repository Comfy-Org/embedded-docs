# FluxProUltraImageNode

Genera immagini utilizzando Flux Pro 1.1 Ultra tramite API, in base a prompt e risoluzione. Questo nodo si connette a un servizio esterno per creare immagini in base alla tua descrizione testuale e alle dimensioni specificate.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt per la generazione dell'immagine (predefinito: stringa vuota) | STRING | Sì | - |
| `prompt_upsampling` | Indica se eseguire l'upsampling sul prompt. Se attivo, modifica automaticamente il prompt per una generazione più creativa, ma i risultati non sono deterministici (lo stesso seed non produrrà esattamente lo stesso risultato). (predefinito: False) | BOOLEAN | No | - |
| `seed` | Il seed casuale utilizzato per creare il rumore. (predefinito: 0) | INT | No | da 0 a 18446744073709551615 |
| `aspect_ratio` | Proporzioni dell'immagine; deve essere compreso tra 1:4 e 4:1. (predefinito: "16:9") | STRING | No | - |
| `raw` | Quando è True, genera immagini meno elaborate e dall'aspetto più naturale. (predefinito: False) | BOOLEAN | No | - |
| `image_prompt` | Immagine di riferimento opzionale per guidare la generazione | IMAGE | No | - |
| `image_prompt_strength` | Rapporto di fusione tra il prompt e l'immagine di riferimento. (predefinito: 0.1) | FLOAT | No | da 0.0 a 1.0 |

**Nota:** Il parametro `aspect_ratio` deve essere compreso tra 1:4 e 4:1. Quando viene fornito `image_prompt`, `image_prompt_strength` diventa attivo e controlla quanto l'immagine di riferimento influenza l'output finale. Se `image_prompt` non viene fornito, il parametro `prompt` viene validato per assicurarsi che non sia vuoto.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output_image` | L'immagine generata da Flux Pro 1.1 Ultra | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProUltraImageNode/it.md)

---
**Source fingerprint (SHA-256):** `6c9292ea666055ccd309d9e5d6d7cf8985f7b8f1e1faeda1e961b429b249f494`

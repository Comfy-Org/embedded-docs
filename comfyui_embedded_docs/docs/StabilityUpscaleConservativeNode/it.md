# StabilityUpscaleConservativeNode

Esegue l'upscale dell'immagine a risoluzione 4K con modifiche minime. Questo nodo utilizza l'upscaling conservativo di Stability AI per aumentare la risoluzione dell'immagine preservando il contenuto originale e apportando solo lievi modifiche.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da upscalare | IMAGE | Sì | - |
| `prompt` | Cosa desideri vedere nell'immagine di output. Un prompt forte e descrittivo che definisca chiaramente elementi, colori e soggetti porterà a risultati migliori. (predefinito: stringa vuota) | STRING | Sì | - |
| `creativity` | Controlla la probabilità di creare dettagli aggiuntivi non fortemente condizionati dall'immagine iniziale. (predefinito: 0.35) | FLOAT | Sì | 0.2 - 0.5 |
| `seed` | Il seed casuale utilizzato per creare il rumore. (predefinito: 0) | INT | Sì | 0 - 4294967294 |
| `negative_prompt` | Parole chiave di ciò che non desideri vedere nell'immagine di output. Questa è una funzionalità avanzata. (predefinito: stringa vuota) | STRING | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | L'immagine upscalata a risoluzione 4K | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleConservativeNode/it.md)

---
**Source fingerprint (SHA-256):** `e4faa795d5a197cdc85c6985b99e8a7229b2b64f929eea3fefff3aff32558c18`

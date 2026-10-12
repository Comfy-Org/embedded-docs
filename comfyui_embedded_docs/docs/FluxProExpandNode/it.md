# Flux.1 Espandi Immagine

Esegue l'outpainting di un'immagine in base al prompt. Questo nodo espande un'immagine aggiungendo pixel in alto, in basso, a sinistra e a destra, generando al contempo nuovi contenuti che corrispondono alla descrizione testuale fornita.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da espandere | IMAGE | Sì | - |
| `prompt` | Prompt per la generazione dell'immagine (predefinito: "") | STRING | No | - |
| `prompt_upsampling` | Indica se eseguire l'upsampling sul prompt. Se attivo, modifica automaticamente il prompt per una generazione più creativa, ma i risultati non sono deterministici (lo stesso seed non produrrà esattamente lo stesso risultato). (predefinito: False) | BOOLEAN | No | - |
| `top` | Numero di pixel da espandere nella parte superiore dell'immagine (predefinito: 0) | INT | No | 0-2048 |
| `bottom` | Numero di pixel da espandere nella parte inferiore dell'immagine (predefinito: 0) | INT | No | 0-2048 |
| `left` | Numero di pixel da espandere sul lato sinistro dell'immagine (predefinito: 0) | INT | No | 0-2048 |
| `right` | Numero di pixel da espandere sul lato destro dell'immagine (predefinito: 0) | INT | No | 0-2048 |
| `guidance` | Intensità della guidance per il processo di generazione dell'immagine (predefinito: 60) | FLOAT | No | 1.5-100 |
| `steps` | Numero di step per il processo di generazione dell'immagine (predefinito: 50) | INT | No | 15-50 |
| `seed` | Il seed casuale utilizzato per creare il rumore. (predefinito: 0) | INT | No | 0-18446744073709551615 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | L'immagine di output espansa | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProExpandNode/it.md)

---
**Source fingerprint (SHA-256):** `faff1e1311a3208066a499a358923c6e335ea1785baeafe3761484641f7f12d6`

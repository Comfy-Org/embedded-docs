# Flux.1 Riempi Immagine

Esegue l'inpainting di un'immagine in base alla maschera e al prompt. Questo nodo utilizza il modello Flux.1 per riempire le aree mascherate di un'immagine in base alla descrizione testuale fornita, generando nuovo contenuto che corrisponde all'immagine circostante.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input su cui eseguire l'inpainting | IMAGE | Sì | - |
| `mask` | La maschera che definisce quali aree dell'immagine devono essere riempite | MASK | Sì | - |
| `prompt` | Prompt per la generazione dell'immagine (predefinito: stringa vuota) | STRING | No | - |
| `prompt_upsampling` | Indica se eseguire l'upsampling sul prompt. Se attivo, modifica automaticamente il prompt per una generazione più creativa, ma i risultati non sono deterministici (lo stesso seed non produrrà esattamente lo stesso risultato). (predefinito: false) | BOOLEAN | No | - |
| `guidance` | Intensità della guidance per il processo di generazione dell'immagine (predefinito: 60) | FLOAT | No | 1.5-100 |
| `steps` | Numero di passaggi per il processo di generazione dell'immagine (predefinito: 50) | INT | No | 15-50 |
| `seed` | Il seed casuale utilizzato per creare il rumore. (predefinito: 0) | INT | No | 0-18446744073709551615 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output_image` | L'immagine generata con le aree mascherate riempite in base al prompt | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/it.md)

---
**Source fingerprint (SHA-256):** `11aa071c52897788d9d7dae4105ffdf747d3cb91d75a0ad7cfacd7ca1ddd2ac1`

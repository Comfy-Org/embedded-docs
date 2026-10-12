# Morphology

Il nodo Morphology applica varie operazioni morfologiche alle immagini, ovvero operazioni matematiche utilizzate per elaborare e analizzare le forme nelle immagini. Può eseguire operazioni come erosione, dilatazione, apertura, chiusura e altre, utilizzando una dimensione del kernel personalizzabile per controllare l'intensità dell'effetto.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input da elaborare | IMAGE | Sì | - |
| `operation` | L'operazione morfologica da applicare (predefinito: "erode") | STRING | Sì | `"erode"`<br>`"dilate"`<br>`"open"`<br>`"close"`<br>`"gradient"`<br>`"bottom_hat"`<br>`"top_hat"` |
| `kernel_size` | La dimensione del kernel dell'elemento strutturante (predefinito: 3). Deve essere un numero dispari. | INT | Sì | 3-999 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine elaborata dopo l'applicazione dell'operazione morfologica | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/it.md)

---
**Source fingerprint (SHA-256):** `ea596f8d30975f153fccbc5651eec0fbbf308ef1c616313d996c200cddf748e3`

# AlignYourStepsScheduler

Il nodo AlignYourStepsScheduler genera valori sigma (livelli di rumore) per il processo di denoising basandosi su diversi tipi di modello. Calcola i livelli di rumore appropriati per ogni fase del processo di campionamento e regola il numero totale di passaggi in base al parametro `denoise`, contribuendo ad allineare i passaggi di campionamento ai requisiti specifici dei diversi modelli di diffusione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model_type` | Specifica il tipo di modello da usare per il calcolo dei sigma (predefinito: "SD1") | COMBO | Sì | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `steps` | Il numero totale di passaggi di campionamento da generare (predefinito: 10) | INT | Sì | 1 to 10000 |
| `denoise` | Controlla quanto denoising applicare all'immagine: 1.0 utilizza tutti i passaggi, mentre valori inferiori ne utilizzano un numero minore (predefinito: 1.0) | FLOAT | Sì | 0.0 to 1.0 (step: 0.01) |

Nota: ogni tipo di modello dispone di una schedulazione dei livelli di rumore integrata contenente 11 valori sigma (per 10 passaggi). Quando `denoise` è 0.0, il nodo restituisce un tensore sigma vuoto. Quando `denoise` è compreso tra 0.0 e 1.0, il numero effettivo di passaggi viene calcolato come `round(steps × denoise)` e viene utilizzata solo la porzione finale corrispondente della schedulazione sigma. Se il valore `steps` richiesto non corrisponde alla lunghezza della schedulazione integrata, i livelli di rumore vengono interpolati log-linearmente per corrispondere al numero di passaggi richiesto. Il valore sigma finale è sempre impostato a 0.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sigmas` | Restituisce i valori sigma calcolati per il processo di denoising | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/it.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`

# Imposta Primo Sigma

Il nodo SetFirstSigma modifica una sequenza di sigma sostituendo solo il suo primo valore con un valore sigma personalizzato. Prende in input una sequenza di sigma esistente e un nuovo valore sigma, quindi restituisce una nuova sequenza di sigma in cui tutti i valori tranne il primo rimangono invariati.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `sigmas` | La sequenza di valori sigma in input da modificare | SIGMAS | Sì | - |
| `sigma` | Il nuovo valore sigma da impostare come primo elemento della sequenza (predefinito: 136.0) | FLOAT | Sì | 0.0 a 20000.0 (passo: 0.001) |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `sigmas` | La sequenza sigma modificata con il primo elemento sostituito dal valore sigma personalizzato | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/it.md)

---
**Source fingerprint (SHA-256):** `5302bc61a7ca094fee9ee2ad8c9dc32997ef0bbf27c9945acd7287e7df6b6db3`

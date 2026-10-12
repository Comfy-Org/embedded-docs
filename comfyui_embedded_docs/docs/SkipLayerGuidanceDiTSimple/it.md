# SkipLayerGuidanceDiTSimple

Versione semplice del nodo SkipLayerGuidanceDiT che modifica solo il passaggio non condizionato durante il processo di denoising. Questo nodo applica la skip layer guidance a specifici layer transformer nei modelli DiT (Diffusion Transformer), saltando selettivamente determinati layer durante il passaggio non condizionato in base ai parametri specificati di temporizzazione e di layer.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui applicare la skip layer guidance | MODEL | Sì | - |
| `double_layers` | Elenco separato da virgole degli indici dei layer double block da saltare (predefinito: "7, 8, 9") | STRING | No | - |
| `single_layers` | Elenco separato da virgole degli indici dei layer single block da saltare (predefinito: "7, 8, 9") | STRING | No | - |
| `start_percent` | La percentuale iniziale del processo di denoising in cui ha inizio la skip layer guidance (predefinito: 0.0) | FLOAT | No | 0.0 - 1.0 |
| `end_percent` | La percentuale finale del processo di denoising in cui termina la skip layer guidance (predefinito: 1.0) | FLOAT | No | 0.0 - 1.0 |

**Nota:** La skip layer guidance viene applicata solo quando sia `double_layers` sia `single_layers` contengono indici di layer validi. Se entrambi sono vuoti, il nodo restituisce il modello originale invariato. La skip layer guidance è attiva solo quando il valore sigma del passo di denoising corrente è compreso tra `start_percent` e `end_percent` (convertiti internamente in valori sigma).

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello modificato con la skip layer guidance applicata ai layer specificati | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiTSimple/it.md)

---
**Source fingerprint (SHA-256):** `f153348d75cf3b52d7d7d541f7467e51c797e1fe5844516591db7a191415cdb2`

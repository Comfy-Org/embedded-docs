# SkipLayerGuidanceDiT

Migliora la guida verso una struttura dettagliata utilizzando un altro set di CFG negativa con layer saltati. Questa versione generica di SkipLayerGuidance può essere usata su qualsiasi modello DiT ed è ispirata a Perturbed Attention Guidance. L'implementazione sperimentale originale è stata creata per SD3.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui applicare la guida con salto dei layer | MODEL | Sì | - |
| `double_layers` | Numeri di layer separati da virgola per i blocchi doppi da saltare (predefinito: "7, 8, 9") | STRING | Sì | - |
| `single_layers` | Numeri di layer separati da virgola per i blocchi singoli da saltare (predefinito: "7, 8, 9") | STRING | Sì | - |
| `scale` | Fattore di scala della guida (predefinito: 3.0) | FLOAT | Sì | 0.0 - 10.0 |
| `start_percent` | Percentuale iniziale per l'applicazione della guida (predefinito: 0.01) | FLOAT | Sì | 0.0 - 1.0 |
| `end_percent` | Percentuale finale per l'applicazione della guida (predefinito: 0.15) | FLOAT | Sì | 0.0 - 1.0 |
| `rescaling_scale` | Fattore di scala di ridimensionamento per regolare l'ampiezza dell'output (predefinito: 0.0, ovvero nessun ridimensionamento) | FLOAT | Sì | 0.0 - 10.0 |

**Nota:** Se sia `double_layers` che `single_layers` sono vuoti (non contengono numeri di layer), il nodo restituisce il modello originale senza applicare alcuna guida.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello modificato con la guida con salto dei layer applicata | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/it.md)

---
**Source fingerprint (SHA-256):** `35ca97f87913d0efcbb502ca040a8f357da112b202184d8786f63acd76809808`

# SkipLayerGuidanceSD3

Il nodo SkipLayerGuidanceSD3 migliora la guida verso una struttura dettagliata applicando un ulteriore insieme di classifier-free guidance con layer saltati. Questa implementazione sperimentale è ispirata a Perturbed Attention Guidance e funziona bypassando selettivamente determinati layer durante il processo di condizionamento negativo per migliorare i dettagli strutturali nell'output generato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui applicare la guida con skip layer | MODEL | Sì | - |
| `layers` | Elenco di indici di layer da saltare, separati da virgole (predefinito: "7, 8, 9") | STRING | Sì | - |
| `scale` | La forza dell'effetto della guida con skip layer (predefinito: 3.0) | FLOAT | Sì | 0.0 - 10.0 |
| `start_percent` | Il punto di inizio dell'applicazione della guida come percentuale del totale dei passaggi (predefinito: 0.01) | FLOAT | Sì | 0.0 - 1.0 |
| `end_percent` | Il punto finale dell'applicazione della guida come percentuale del totale dei passaggi (predefinito: 0.15) | FLOAT | Sì | 0.0 - 1.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato con la guida con skip layer applicata | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceSD3/it.md)

---
**Source fingerprint (SHA-256):** `8fba6e3037387e6beab64175099de1c96babdd492609099ba8ad3a49a6c34efe`

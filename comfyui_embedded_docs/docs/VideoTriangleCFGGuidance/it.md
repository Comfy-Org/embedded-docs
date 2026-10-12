# VideoTriangleCFGGuidance

Il nodo VideoTriangleCFGGuidance applica uno schema di scalatura triangolare della classifier-free guidance (CFG) a un modello video. Varia la scala di condizionamento usando un'onda triangolare che oscilla tra `min_cfg` e la scala di condizionamento originale del modello. Questo crea uno schema di guida dinamico che può aiutare a migliorare la coerenza e la qualità della generazione video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello video a cui applicare la guida CFG triangolare. | MODEL | Sì | - |
| `min_cfg` | Il valore minimo della scala CFG per lo schema triangolare. Questo parametro è mostrato nella sezione avanzata dell'interfaccia del nodo (predefinito: 1.0). | FLOAT | Sì | 0.0 - 100.0 (passo: 0.5, arrotondamento: 0.01) |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato con la guida CFG triangolare applicata. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/it.md)

---
**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`

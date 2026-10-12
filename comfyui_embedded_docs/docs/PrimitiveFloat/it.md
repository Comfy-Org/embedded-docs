# PrimitiveFloat

Il nodo PrimitiveFloat crea un valore numerico in virgola mobile che può essere utilizzato nel flusso di lavoro. Accetta un singolo input numerico e restituisce in output lo stesso valore, consentendo di definire e passare valori float tra nodi diversi nella pipeline di ComfyUI.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `value` | Il valore numerico in virgola mobile da restituire in output (predefinito: 0.0) | FLOAT | Sì | da -sys.maxsize a sys.maxsize (passo: 0.1) |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | Il valore numerico in virgola mobile fornito in input | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveFloat/it.md)

---
**Source fingerprint (SHA-256):** `df57e5900e972e17da365fbbdb7b7db777dda6f9f938e1074f1a89451d4b7c73`

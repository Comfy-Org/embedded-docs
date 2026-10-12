# CurveEditor

Il nodo Curve Editor fornisce un'interfaccia visiva per regolare e ottimizzare una curva. È possibile modificare la forma di una curva di input direttamente nell'interfaccia del nodo e, facoltativamente, visualizzare un istogramma accanto ad essa come riferimento visivo. Il nodo supporta l'output intermedio durante la modifica, consentendo di vedere i risultati in tempo reale mentre si apportano modifiche, e restituisce la curva modificata per l'utilizzo in altre parti del workflow.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `curve` | La curva di input da modificare. | CURVE | Sì | N/A |
| `histogram` | Un istogramma opzionale da visualizzare accanto alla curva come riferimento visivo. | HISTOGRAM | No | N/A |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `curve` | La curva modificata dopo le regolazioni apportate nell'interfaccia del nodo. | CURVE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/it.md)

---
**Source fingerprint (SHA-256):** `6c4459998b1a3dd3a53f84cb1c231c448c64aa55b96444bc4ac7470556a3b915`

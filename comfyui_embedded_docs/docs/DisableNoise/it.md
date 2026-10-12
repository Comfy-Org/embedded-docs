# Disabilita Rumore

Questo nodo fornisce una configurazione di rumore vuota che disabilita la generazione di rumore durante il campionamento. Restituisce un oggetto rumore speciale che non contiene dati di rumore, quindi qualsiasi nodo a esso collegato salta le operazioni relative al rumore. È inoltre individuabile tramite l'alias "zero noise".

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| *Nessun parametro di input* | Questo nodo non richiede alcun parametro di input. | - | - | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `NOISE` | Restituisce una configurazione di rumore vuota che può essere utilizzata per disabilitare la generazione di rumore nei processi di campionamento. | NOISE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/it.md)

---
**Source fingerprint (SHA-256):** `b9edcda655dab3196233b6c66fdb41eb0585b153616b793016d532992b922934`

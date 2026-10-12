# TomePatchModel

TomePatchModel applica Token Merging (ToMe) a un modello di diffusione per ridurre il costo computazionale durante l'inferenza. Funziona unendo token simili all'interno del meccanismo di attenzione del modello, così il modello elabora meno token mantenendo in gran parte intatta la qualità dell'output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione a cui applicare il token merging | MODEL | Sì | - |
| `ratio` | La proporzione di token da unire (predefinito: 0.3). Valori più alti uniscono più token, il che può offrire una maggiore accelerazione ma potenzialmente una qualità inferiore. | FLOAT | Sì | 0.0 - 1.0 |

Nota: se il numero di token in un blocco di attenzione è sufficientemente piccolo da non richiedere downsampling, le funzioni di merging vengono sostituite con no-op e il modello viene eseguito invariato per quel blocco.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato con il token merging applicato | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/it.md)

---
**Source fingerprint (SHA-256):** `1202c0df17f357440cd156fa0920f70c18a318e32c41dc04cecff11613f0072f`

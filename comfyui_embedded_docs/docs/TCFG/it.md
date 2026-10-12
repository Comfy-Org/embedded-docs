# Tangential Damping CFG

TCFG (Tangential Damping CFG) affina le predizioni incondizionate (negative) per allinearle meglio alle predizioni condizionate (positive) durante il processo di campionamento. Questa tecnica migliora la qualità dell'output applicando uno smorzamento tangenziale alla guida incondizionata, basandosi sul paper di ricerca 2503.18137. Il nodo modifica il comportamento di campionamento del modello regolando il modo in cui le predizioni incondizionate vengono elaborate durante il classifier-free guidance.

## Input

| Parametro | Descrizione | Tipo di dati | Richiesto | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui applicare il TCFG (Tangential Damping CFG) | MODEL | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `patched_model` | Il modello modificato con il TCFG (Tangential Damping CFG) applicato | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TCFG/it.md)

---
**Source fingerprint (SHA-256):** `6e0e1df09bdc29f14a4828ec54fd29f89926b9d8121bc8ba9f95ce066b899e95`

# ThresholdMask

Il nodo ThresholdMask converte una maschera in una maschera binaria applicando un valore di soglia. Confronta ogni pixel della maschera di input con il valore di soglia specificato e crea una nuova maschera in cui i pixel sopra la soglia diventano 1 (bianco) e i pixel inferiori o uguali alla soglia diventano 0 (nero).

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `mask` | La maschera di input da elaborare | MASK | Sì | - |
| `value` | Il valore di soglia per la binarizzazione (predefinito: 0.5) | FLOAT | Sì | 0.0 - 1.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `mask` | La maschera binaria risultante dopo l'applicazione della soglia | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ThresholdMask/it.md)

---
**Source fingerprint (SHA-256):** `eff4479b70c1ca87ba9ba17b771edf5d816cf13c12ac0767cd7ee79d18e326c3`

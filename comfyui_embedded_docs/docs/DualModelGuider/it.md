# Dual Model CFG Guider

Questo nodo consente di utilizzare due modelli diversi durante il processo di campionamento CFG guidato: un modello per il passaggio positivo (condizionale) e un modello separato per il passaggio negativo (non condizionale). Quando non viene fornito alcun modello negativo, si comporta come un guider CFG standard che utilizza un singolo modello.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modello utilizzato per il passaggio positivo (condizionale). | MODEL | Sì | |
| `model_negative` | Modello utilizzato per il passaggio negativo (non condizionale). Usa lo stesso modello per il CFG ordinario. | MODEL | No | |
| `positive` | L'input di condizionamento positivo. | CONDITIONING | Sì | |
| `cfg` | Il valore di scala CFG (predefinito: 4.0). | FLOAT | Sì | 0.0 a 100.0 (passo: 0.1) |
| `negative` | Condizionamento negativo eseguito sul modello negativo. Lascia non collegato per un passaggio non condizionale senza testo (solo immagine). | CONDITIONING | No | |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `GUIDER` | Un oggetto guider configurato con i modelli e il condizionamento specificati per l'uso nel campionamento. | GUIDER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualModelGuider/it.md)

---
**Source fingerprint (SHA-256):** `a60803156e98d2ffe975d39922dfbeacafd1a2155d88dd2e285ac1426a1e7a33`

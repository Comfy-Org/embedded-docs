# ModelSamplingContinuousV

Il nodo ModelSamplingContinuousV regola il comportamento di campionamento di un modello applicando il campionamento continuo V-prediction. Crea un clone del modello di input e lo configura con valori sigma minimi e massimi personalizzati per un controllo più preciso sul processo di campionamento.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello di input da modificare con il campionamento continuo V-prediction | MODEL | Sì | - |
| `sampling` | Il metodo di campionamento da applicare; attualmente V-prediction è l'unica opzione disponibile (predefinito: `"v_prediction"`) | COMBO | Sì | `"v_prediction"` |
| `sigma_max` | Il valore sigma massimo per il campionamento (parametro avanzato, predefinito: 500.0, passo: 0.001) | FLOAT | Sì | 0.0 - 1000.0 |
| `sigma_min` | Il valore sigma minimo per il campionamento (parametro avanzato, predefinito: 0.03, passo: 0.001) | FLOAT | Sì | 0.0 - 1000.0 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `model` | Il modello modificato a cui è stato applicato il campionamento continuo V-prediction | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/it.md)

---
**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`

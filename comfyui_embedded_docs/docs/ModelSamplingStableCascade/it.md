# ModelSamplingStableCascade

Il nodo ModelSamplingStableCascade applica le impostazioni di campionamento Stable Cascade a un modello applicando un valore di shift ai parametri di campionamento. Restituisce una copia patchata del modello di input con la configurazione personalizzata di campionamento Stable Cascade, lasciando invariato il modello originale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di input a cui applicare il campionamento Stable Cascade | MODEL | Sì | - |
| `shift` | Il valore di shift applicato ai parametri di campionamento (predefinito: 2.0) | FLOAT | Sì | 0.0 - 100.0 (passo 0.01) |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato con il campionamento Stable Cascade applicato | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/it.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`

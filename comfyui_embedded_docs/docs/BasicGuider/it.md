# BasicGuider

Il nodo BasicGuider crea un semplice meccanismo di guida per il processo di campionamento. Prende in input un modello e dati di condizionamento e produce un oggetto guider che può essere utilizzato per guidare il processo di generazione durante il campionamento. Questo nodo fornisce la funzionalità di guida fondamentale necessaria per la generazione controllata.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello da utilizzare per la guida | MODEL | Sì | - |
| `conditioning` | I dati di condizionamento che guidano il processo di generazione | CONDITIONING | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `GUIDER` | Un oggetto guider che può essere utilizzato durante il processo di campionamento per guidare la generazione | GUIDER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/it.md)

---
**Source fingerprint (SHA-256):** `8ea6b56be58ae99baaf13a04c4fadbf8ad921801d8f2ce2aecce768cc34a3b20`

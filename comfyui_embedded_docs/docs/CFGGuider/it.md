# CFG Guider

Il nodo CFG Guider crea un sistema di guida per controllare il processo di campionamento nella generazione di immagini. Riceve in input un modello insieme a input di condizionamento positivo e negativo, quindi applica una scala di guida classifier-free per indirizzare la generazione verso il contenuto desiderato evitando elementi indesiderati. Questo nodo restituisce in output un oggetto guider che può essere utilizzato dai nodi di campionamento per controllare la direzione della generazione dell'immagine.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello da utilizzare per la guida | MODEL | Sì | - |
| `positive` | Il condizionamento positivo che guida la generazione verso il contenuto desiderato | CONDITIONING | Sì | - |
| `negative` | Il condizionamento negativo che indirizza la generazione lontano dal contenuto indesiderato | CONDITIONING | Sì | - |
| `cfg` | La scala di guida classifier-free che controlla quanto fortemente il condizionamento influenza la generazione (predefinito: 8.0) | FLOAT | Sì | 0.0 to 100.0 (step: 0.1) |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `GUIDER` | Un oggetto guider che può essere passato ai nodi di campionamento per controllare il processo di generazione | GUIDER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/it.md)

---
**Source fingerprint (SHA-256):** `73b57bfbb6d4fc083a8089bc0f786f82d03e0d7b2faeeb7a42b3d87e38047b9e`

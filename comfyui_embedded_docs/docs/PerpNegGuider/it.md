# PerpNegGuider

Il nodo PerpNegGuider crea un sistema di guida per controllare la generazione di immagini utilizzando il condizionamento negativo perpendicolare. Riceve in ingresso condizionamenti positivo, negativo e vuoto e applica un algoritmo di guida specializzato che calcola tutte e tre le predizioni di rumore in un singolo batch per efficienza. Questo nodo è progettato per test sperimentali e offre un controllo fine sulla forza della guida e sulla scala negativa.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello da utilizzare per la generazione della guida | MODEL | Sì | - |
| `positive` | Il condizionamento positivo che guida la generazione verso il contenuto desiderato | CONDITIONING | Sì | - |
| `negative` | Il condizionamento negativo che guida la generazione lontano dal contenuto indesiderato | CONDITIONING | Sì | - |
| `empty_conditioning` | Il condizionamento vuoto o neutro utilizzato come riferimento di base per la guida negativa perpendicolare | CONDITIONING | Sì | - |
| `cfg` | La scala di guida classifier-free che controlla quanto fortemente il condizionamento influenza la generazione (predefinito: 8.0) | FLOAT | Sì | 0.0 - 100.0 |
| `neg_scale` | Il fattore di scala negativo che regola la forza dell'effetto negativo perpendicolare (predefinito: 1.0) | FLOAT | Sì | 0.0 - 100.0 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `guider` | Un sistema di guida configurato pronto per l'uso nella pipeline di generazione | GUIDER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNegGuider/it.md)

---
**Source fingerprint (SHA-256):** `02e4b4e0ea413da31c280cb1e510bdf5caa7b5187eb6de94632e45a91e881820`

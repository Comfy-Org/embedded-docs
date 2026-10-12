# BetaSamplingScheduler

Il nodo BetaSamplingScheduler genera una sequenza di livelli di rumore (sigma) per il processo di campionamento utilizzando un algoritmo di pianificazione beta. Richiede un modello e parametri di configurazione per creare una programmazione del rumore personalizzata che controlla il processo di denoising durante la generazione delle immagini. Questo scheduler consente di regolare finemente la traiettoria di riduzione del rumore tramite i parametri alpha e beta.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello utilizzato per il campionamento, che fornisce l'oggetto di campionamento del modello | MODEL | Sì | - |
| `steps` | Il numero di passaggi di campionamento per cui generare i sigma (predefinito: 20) | INT | Sì | da 1 a 10000 |
| `alpha` | Parametro alpha per lo scheduler beta, che controlla la curva di pianificazione (predefinito: 0.6, parametro avanzato) | FLOAT | Sì | da 0.0 a 50.0 (passo 0.01) |
| `beta` | Parametro beta per lo scheduler beta, che controlla la curva di pianificazione (predefinito: 0.6, parametro avanzato) | FLOAT | Sì | da 0.0 a 50.0 (passo 0.01) |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `SIGMAS` | Una sequenza di livelli di rumore (sigma) utilizzata per il processo di campionamento | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/it.md)

---
**Source fingerprint (SHA-256):** `80adae3cbedff7fe544a1fbcf638af7965f1216e422931063ecf67da53ddff95`

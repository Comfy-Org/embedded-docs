# LatentCut

Il nodo LatentCut estrae una sezione specifica dai campioni latenti lungo una dimensione scelta. Ritaglia una porzione della rappresentazione latente specificando la dimensione (x, y o t), la posizione iniziale e quanto estrarre. Il nodo supporta sia l'indicizzazione positiva sia quella negativa e regola automaticamente la quantità di estrazione in modo che rimanga entro i limiti disponibili.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `samples` | I campioni latenti di input da cui estrarre | LATENT | Sì | - |
| `dim` | La dimensione lungo la quale tagliare i campioni latenti. "x" taglia lungo l'ultimo asse (tipicamente la larghezza), "y" lungo il penultimo asse (tipicamente l'altezza) e "t" lungo il terzultimo asse (tipicamente i fotogrammi nei latenti video) | COMBO | Sì | "x"<br>"y"<br>"t" |
| `index` | La posizione iniziale per il taglio (predefinita: 0). I valori positivi contano dall'inizio, quelli negativi dalla fine. Il nodo limita l'indice per mantenerlo entro l'intervallo valido dei campioni latenti | INT | Sì | da -16384 a 16384 |
| `amount` | Il numero di elementi da estrarre lungo la dimensione specificata (predefinito: 1). Deve essere almeno 1. Il nodo riduce automaticamente questo valore se supererebbe i dati disponibili oltre l'indice iniziale | INT | Sì | da 1 a 16384 |

Nota: i valori `index` e `amount` vengono regolati per adattarsi alla dimensione effettiva del latente lungo la dimensione selezionata. Se `index` è maggiore della dimensione, viene limitato all'ultima posizione valida. Se `index` è negativo, viene limitato alla dimensione in valore assoluto, e `amount` viene limitato in modo che non superi la fine dei dati.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | La porzione estratta dei campioni latenti | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/it.md)

---
**Source fingerprint (SHA-256):** `7682de2644a4b85dba0571406f9f9802eca7caab09dc2ccf1ac91dc13b41bcdf`

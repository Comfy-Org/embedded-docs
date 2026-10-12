# RandomNoise

Il nodo RandomNoise crea un generatore di rumore basato su un valore di seed da utilizzare durante il processo di campionamento. Lo stesso seed produce sempre lo stesso pattern di rumore, consentendo risultati coerenti e riproducibili su più esecuzioni. I sampler utilizzano il rumore generato durante l'elaborazione delle immagini latenti.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `noise_seed` | Il valore di seed utilizzato per generare il pattern di rumore casuale (predefinito: 0). Lo stesso seed produce sempre lo stesso output di rumore. Questo input include un'opzione di controllo dopo la generazione per aggiornare automaticamente il seed dopo ogni generazione. | INT | Sì | 0 a 18446744073709551615 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `noise` | Un oggetto noise che genera rumore casuale per i campioni latenti in base al valore di seed fornito. Utilizzato dai sampler durante il processo di campionamento. | NOISE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/it.md)

---
**Source fingerprint (SHA-256):** `b55ff98c636c55f064ede82c6848ffa163d1fd9b0cf6195f4a35603cfbe2bc1e`

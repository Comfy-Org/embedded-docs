# SdTurboScheduler

SDTurboScheduler è progettato per generare una sequenza di valori sigma per il campionamento delle immagini, regolando la sequenza in base al livello di denoise e al numero di step specificati. Sfrutta le capacità di campionamento di un modello specifico per produrre questi valori sigma, cruciali per controllare il processo di denoising durante la generazione delle immagini.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il parametro `model` specifica il modello generativo da utilizzare per la generazione dei valori sigma. È cruciale per determinare il comportamento e le capacità di campionamento specifici dello scheduler. | `MODEL` |
| `steps` | Il parametro `steps` determina la lunghezza della sequenza di sigma da generare, influenzando direttamente la granularità del processo di denoising. | `INT` |
| `denoise` | Il parametro `denoise` regola il punto di partenza della sequenza di sigma, consentendo un controllo più fine sul livello di denoising applicato durante la generazione delle immagini. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sigmas` | Una sequenza di valori sigma generata in base al modello, agli step e al livello di denoise specificati. Questi valori sono essenziali per controllare il processo di denoising nella generazione delle immagini. | `SIGMAS` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDTurboScheduler/it.md)

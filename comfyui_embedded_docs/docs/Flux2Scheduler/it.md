# Flux2Scheduler

Flux2Scheduler genera una sequenza di livelli di rumore (sigmas) per il processo di denoising, specificamente adattata al modello Flux. Calcola una schedulazione basata sul numero di passaggi di denoising e sulle dimensioni dell'immagine di destinazione, che influenza la progressione della rimozione del rumore durante la generazione dell'immagine.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `steps` | Il numero di passaggi di denoising da eseguire. Un valore più alto in genere porta a risultati più dettagliati ma richiede più tempo di elaborazione (predefinito: 20). | INT | Sì | 1 to 4096 |
| `width` | La larghezza dell'immagine da generare, in pixel. Questo valore influenza il calcolo della schedulazione del rumore (predefinito: 1024). | INT | Sì | 16 to 16384 |
| `height` | L'altezza dell'immagine da generare, in pixel. Questo valore influenza il calcolo della schedulazione del rumore (predefinito: 1024). | INT | Sì | 16 to 16384 |

Nota: la schedulazione viene calcolata dalla lunghezza della sequenza dell'immagine, che deriva da `width` e `height` come `(width * height) / 256`, riflettendo il downsampling latente 16x del modello. Le immagini più grandi producono sequenze più lunghe, il che modifica di conseguenza la schedulazione del rumore.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sigmas` | Una sequenza di valori di livello di rumore (sigmas) che definiscono la schedulazione di denoising per il campionatore. | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/it.md)

---
**Source fingerprint (SHA-256):** `9606177f37f7bc03aef524623f03b7f24bcdc3d9327dcdf74863fe2befeb2b65`

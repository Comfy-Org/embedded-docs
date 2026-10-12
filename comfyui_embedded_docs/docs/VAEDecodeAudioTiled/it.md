# Decodifica audio VAE (a blocchi)

Questo nodo converte una rappresentazione audio compressa (campioni latenti) nuovamente in una forma d'onda audio utilizzando un autoencoder variazionale (VAE). Elabora i dati in sezioni più piccole e sovrapposte (tile) per gestire l'uso della memoria, rendendolo adatto a gestire sequenze audio più lunghe. L'audio decodificato viene anche normalizzato per mantenere un livello di volume coerente.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `samples` | La rappresentazione latente compressa dell'audio da decodificare. | LATENT | Sì | N/A |
| `vae` | Il modello autoencoder variazionale utilizzato per eseguire la decodifica. | VAE | Sì | N/A |
| `tile_size` | La dimensione di ciascun tile di elaborazione. L'audio viene decodificato in sezioni di questa lunghezza per conservare memoria (predefinito: 512). Deve essere un multiplo di 8. | INT | Sì | 32 to 8192 (step 8) |
| `overlap` | Il numero di campioni di sovrapposizione tra tile adiacenti. Questo aiuta a ridurre gli artefatti ai bordi tra i tile (predefinito: 64). Deve essere un multiplo di 8. | INT | Sì | 0 to 1024 (step 8) |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | La forma d'onda audio decodificata, incluse le informazioni sulla frequenza di campionamento. | AUDIO |

La frequenza di campionamento dell'output viene presa dall'input `samples` quando questo ne contiene una; in caso contrario, viene letta dal modello VAE (valore predefinito: 44100 Hz).

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/it.md)

---
**Source fingerprint (SHA-256):** `5ddedf218ba27ab9f463646c1e5288091172f2d7fae8f2980bb2b5e4d3dca89c`

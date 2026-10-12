# SamplerCustomAdvanced

Il nodo SamplerCustomAdvanced esegue un campionamento avanzato nello spazio latente utilizzando configurazioni personalizzate di rumore, guida e campionamento. Elabora un'immagine latente attraverso un processo di campionamento guidato con un generatore di rumore e un programma sigma personalizzabili, producendo sia l'output campionato finale sia una versione denoizzata, quando disponibile.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `noise` | Il generatore di rumore che fornisce il pattern di rumore iniziale e il seed per il processo di campionamento | NOISE | Sì | - |
| `guider` | Il modello di guida che indirizza il processo di campionamento verso l'output desiderato | GUIDER | Sì | - |
| `sampler` | L'algoritmo di campionamento che definisce come lo spazio latente viene attraversato durante la generazione | SAMPLER | Sì | - |
| `sigmas` | Il programma sigma che controlla i livelli di rumore durante i passaggi di campionamento | SIGMAS | Sì | - |
| `latent_image` | La rappresentazione latente iniziale che funge da punto di partenza per il campionamento. Supporta una chiave opzionale `noise_mask` per la denoizzazione selettiva, e chiavi opzionali `downscale_ratio_spacial` e `downscale_ratio_temporal` per una gestione avanzata del latente | LATENT | Sì | - |

## Output

| Nome dell'output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | La rappresentazione latente finale campionata dopo il completamento del processo di campionamento. Eventuali chiavi `downscale_ratio_spacial` o `downscale_ratio_temporal` dal latente di input vengono rimosse da questo output | LATENT |
| `denoised_output` | Una versione denoizzata dell'output quando il processo di campionamento produce una previsione pulita intermedia (x0); altrimenti restituisce lo stesso valore di `output`. Quando disponibile, rappresenta la migliore stima del modello del latente pulito | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/it.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`

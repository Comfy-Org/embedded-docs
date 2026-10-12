# Kandinsky5ImageToVideo

Il nodo Kandinsky5ImageToVideo prepara i dati di condizionamento e latent per la generazione video utilizzando il modello Kandinsky. Crea un latent video vuoto dimensionato in base a larghezza, altezza, lunghezza e dimensione del batch richieste e può facoltativamente codificare un'immagine iniziale per guidare i fotogrammi iniziali del video generato aggiornando il condizionamento positivo e negativo.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | I prompt di condizionamento positivi per guidare la generazione video. | CONDITIONING | Sì | N/A |
| `negative` | I prompt di condizionamento negativi per allontanare la generazione video da determinati concetti. | CONDITIONING | Sì | N/A |
| `vae` | Il modello VAE utilizzato per codificare l'immagine iniziale opzionale nello spazio latente. | VAE | Sì | N/A |
| `width` | La larghezza del video di output in pixel (predefinito: 768). | INT | Sì | 16 to 16384 (step 16) |
| `height` | L'altezza del video di output in pixel (predefinito: 512). | INT | Sì | 16 to 16384 (step 16) |
| `length` | Il numero di fotogrammi nel video (predefinito: 121). | INT | Sì | 1 to 16384 (step 4) |
| `batch_size` | Il numero di sequenze video da generare simultaneamente (predefinito: 1). | INT | Sì | 1 to 4096 |
| `start_image` | Un'immagine iniziale opzionale o un batch di fotogrammi. Se fornita, viene codificata e utilizzata per sostituire l'inizio rumoroso dei latent di output del modello. | IMAGE | No | N/A |

**Nota:** Quando viene fornita una `start_image`, questa viene ridimensionata automaticamente per corrispondere a `width` e `height` specificati usando l'interpolazione bilineare. Solo i primi `length` fotogrammi del batch di immagini vengono utilizzati per la codifica; eventuali fotogrammi aggiuntivi vengono ignorati. Se il batch di immagini contiene meno di `length` fotogrammi, vengono utilizzati solo quei fotogrammi. Vengono codificati solo i canali RGB dell'immagine. Il latent codificato viene quindi iniettato sia nel condizionamento `positive` sia in quello `negative` per guidare l'aspetto iniziale del video, e i fotogrammi codificati puliti sostituiscono l'inizio rumoroso dei latent di output del modello.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Il condizionamento positivo modificato, aggiornato con i dati dell'immagine iniziale codificata quando viene fornita una `start_image`. | CONDITIONING |
| `negative` | Il condizionamento negativo modificato, aggiornato con i dati dell'immagine iniziale codificata quando viene fornita una `start_image`. | CONDITIONING |
| `latent` | Latent video vuoto. Un tensore latente riempito di zeri, con forma adatta alle dimensioni specificate. | LATENT |
| `cond_latent` | Immagini iniziali codificate pulite, utilizzate per sostituire l'inizio rumoroso dei latent di output del modello. Vuoto quando non viene fornita alcuna `start_image`. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/it.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`

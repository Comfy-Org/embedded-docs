# HunyuanImageToVideo

Il nodo HunyuanImageToVideo converte le immagini in rappresentazioni latenti video utilizzando il modello video Hunyuan. Accetta input di condizionamento e immagini iniziali opzionali per generare latenti video che possono essere ulteriormente elaborati dai modelli di generazione video. Il nodo supporta diversi tipi di guida per controllare come l'immagine iniziale influenza il processo di generazione video.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Input di condizionamento positivo per guidare la generazione video | CONDITIONING | Sì | - |
| `vae` | Modello VAE utilizzato per codificare le immagini nello spazio latente | VAE | Sì | - |
| `width` | Larghezza del video di output in pixel (predefinito: 848, passo: 16) | INT | Sì | 16 to MAX_RESOLUTION |
| `height` | Altezza del video di output in pixel (predefinito: 480, passo: 16) | INT | Sì | 16 to MAX_RESOLUTION |
| `length` | Numero di fotogrammi nel video di output (predefinito: 53, passo: 4) | INT | Sì | 1 to MAX_RESOLUTION |
| `batch_size` | Numero di video da generare simultaneamente (predefinito: 1) | INT | Sì | 1 to 4096 |
| `guidance_type` | Metodo per incorporare l'immagine iniziale nella generazione video (predefinito: "v1 (concat)"). Opzione avanzata | COMBO | Sì | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `start_image` | Immagine iniziale opzionale (o sequenza di immagini) per inizializzare la generazione video. Vengono utilizzati solo i primi `length` fotogrammi e i primi 3 canali di colore | IMAGE | No | - |

**Nota:** Quando viene fornito `start_image`, il nodo utilizza metodi di guida diversi in base al `guidance_type` selezionato:

- "v1 (concat)": Concatena il latente dell'immagine con il latente video e applica una maschera per fondere l'immagine nel video
- "v2 (replace)": Sostituisce i fotogrammi video iniziali con il latente dell'immagine e applica una maschera di rumore
- "custom": Usa l'immagine come latente di riferimento per la guida

Se `start_image` non viene fornito, non viene aggiunto alcun condizionamento di guida e il latente viene restituito come un semplice blocco di zeri.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Condizionamento positivo modificato con la guida dell'immagine applicata quando viene fornito `start_image` | CONDITIONING |
| `latent` | Rappresentazione latente video pronta per ulteriori elaborazioni da parte dei modelli di generazione video | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/it.md)

---
**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`

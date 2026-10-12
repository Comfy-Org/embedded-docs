# InstructPixToPixConditioning

Il nodo InstructPixToPixConditioning prepara i dati di condizionamento per l'editing delle immagini InstructPix2Pix combinando prompt testuali positivi e negativi con i dati dell'immagine. Codifica l'immagine di input tramite un VAE in una rappresentazione latente e collega tale latente sia al condizionamento positivo sia a quello negativo, restituendo anche un latente vuoto corrispondente. Le dimensioni dell'immagine vengono ritagliate automaticamente a multipli di 8 pixel in modo che il VAE possa elaborarle.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Dati di condizionamento positivi contenenti prompt testuali e impostazioni per le caratteristiche desiderate dell'immagine | CONDITIONING | Sì | - |
| `negative` | Dati di condizionamento negativi contenenti prompt testuali e impostazioni per le caratteristiche indesiderate dell'immagine | CONDITIONING | Sì | - |
| `vae` | Modello VAE utilizzato per codificare le immagini di input in rappresentazioni latenti | VAE | Sì | - |
| `pixels` | Immagine di input da elaborare e codificare nello spazio latente | IMAGE | Sì | - |

**Nota:** Le dimensioni dell'immagine di input vengono regolate automaticamente tramite ritaglio centrale a multipli di 8 pixel sia in larghezza sia in altezza, per garantire la compatibilità con il processo di codifica del VAE.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Dati di condizionamento positivi con il latente dell'immagine codificata collegato come `concat_latent_image` | CONDITIONING |
| `negative` | Dati di condizionamento negativi con il latente dell'immagine codificata collegato come `concat_latent_image` | CONDITIONING |
| `latent` | Tensore latente di zeri con le stesse dimensioni dell'immagine codificata | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/it.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`

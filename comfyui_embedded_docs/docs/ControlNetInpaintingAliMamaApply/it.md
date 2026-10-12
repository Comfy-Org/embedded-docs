# ControlNetInpaintingAliMamaApply

Il nodo ControlNetInpaintingAliMamaApply applica il condizionamento ControlNet per attività di inpainting combinando il condizionamento positivo e negativo con un'immagine di controllo e una maschera. Elabora l'immagine e la maschera di input per creare un condizionamento modificato che guida il processo di generazione, consentendo di controllare quali aree dell'immagine vengono sottoposte a inpainting. Il nodo supporta la regolazione della forza e i controlli temporali per ottimizzare l'influenza del ControlNet durante le diverse fasi del processo di generazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Il condizionamento positivo che guida la generazione verso il contenuto desiderato | CONDITIONING | Sì | - |
| `negative` | Il condizionamento negativo che guida la generazione lontano dal contenuto indesiderato | CONDITIONING | Sì | - |
| `control_net` | Il modello ControlNet che fornisce controllo aggiuntivo sulla generazione | CONTROL_NET | Sì | - |
| `vae` | Il VAE (Autoencoder variazionale) utilizzato per codificare e decodificare le immagini | VAE | Sì | - |
| `image` | L'immagine di input che funge da guida di controllo per il ControlNet | IMAGE | Sì | - |
| `mask` | La maschera che definisce quali aree dell'immagine devono essere sottoposte a inpainting | MASK | Sì | - |
| `strength` | La forza dell'effetto ControlNet (predefinito: 1.0, passo: 0.01) | FLOAT | Sì | 0.0 to 10.0 |
| `start_percent` | Parametro avanzato. Il punto di inizio (in percentuale) da cui comincia l'influenza del ControlNet durante la generazione (predefinito: 0.0, passo: 0.001) | FLOAT | Sì | 0.0 to 1.0 |
| `end_percent` | Parametro avanzato. Il punto finale (in percentuale) in cui termina l'influenza del ControlNet durante la generazione (predefinito: 1.0, passo: 0.001) | FLOAT | Sì | 0.0 to 1.0 |

**Nota:** Quando il ControlNet ha `concat_mask` abilitato, la maschera viene invertita e applicata all'immagine prima dell'elaborazione, e la maschera invertita viene inclusa nei dati di concatenazione extra inviati al ControlNet.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Il condizionamento positivo modificato con ControlNet applicato per l'inpainting | CONDITIONING |
| `negative` | Il condizionamento negativo modificato con ControlNet applicato per l'inpainting | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/it.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`

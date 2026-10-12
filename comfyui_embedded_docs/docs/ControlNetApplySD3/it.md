# Applica ControlNet con VAE

Questo nodo applica la guida ControlNet al condizionamento di Stable Diffusion 3. Riceve in input i condizionamenti positive e negative insieme a un modello ControlNet e a un'immagine, quindi applica la guida di controllo con parametri regolabili di forza e temporizzazione per influenzare il processo di generazione.

**Nota:** Questo nodo è stato contrassegnato come deprecato e potrebbe essere rimosso nelle versioni future.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Il condizionamento positivo a cui applicare la guida ControlNet | CONDITIONING | Sì | - |
| `negative` | Il condizionamento negativo a cui applicare la guida ControlNet | CONDITIONING | Sì | - |
| `control_net` | Il modello ControlNet da usare per la guida | CONTROL_NET | Sì | - |
| `vae` | Il modello VAE usato nel processo | VAE | Sì | - |
| `image` | L'immagine di input che ControlNet userà come guida | IMAGE | Sì | - |
| `strength` | La forza dell'effetto ControlNet (predefinito: 1.0). Se impostato su 0.0, il nodo salta l'applicazione di ControlNet e restituisce il condizionamento invariato. | FLOAT | Sì | 0.0 - 10.0 |
| `start_percent` | Il punto di partenza nel processo di generazione in cui ControlNet inizia ad applicarsi (predefinito: 0.0) | FLOAT | Sì | 0.0 - 1.0 |
| `end_percent` | Il punto finale nel processo di generazione in cui ControlNet smette di applicarsi (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |

**Nota:** Quando `strength` è impostato su 0.0, non viene applicata alcuna guida ControlNet e il condizionamento di input viene passato invariato a entrambi gli output.

**Nota:** Se lo stesso condizionamento viene riutilizzato altrove e contiene già informazioni di controllo, il nuovo ControlNet viene collegato dopo il precedente, quindi è possibile applicare più ControlNet in sequenza.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Il condizionamento positivo modificato con la guida ControlNet applicata | CONDITIONING |
| `negative` | Il condizionamento negativo modificato con la guida ControlNet applicata | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/it.md)

---
**Source fingerprint (SHA-256):** `b76b0683c05e38102280ca8b0bd23f39a9b9b1b4f52125c77c95686c0a06f398`

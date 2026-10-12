# Applica Fun ControlNet

ZImageFunControlnet applica una patch di rete di controllo a un modello base, così da poter guidare il processo di generazione o modifica delle immagini. Combina un modello, una patch del modello e un VAE e consente di controllare quanto fortemente l'effetto di controllo influenza il risultato. Gli input opzionali `image`, `inpaint_image` e `mask` permettono modifiche più mirate. Il nodo funziona con le patch Z-Image ControlNet e con le patch Qwen Image 2.1 Fun ControlNet caricate tramite il nodo Load Model Patch.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello base utilizzato per il processo di generazione. | MODEL | Sì | - |
| `model_patch` | Un modello patch specializzato che applica la guida della rete di controllo. | MODEL_PATCH | Sì | - |
| `vae` | L'autoencoder variazionale utilizzato per codificare e decodificare le immagini. | VAE | Sì | - |
| `strength` | L'intensità dell'influenza della rete di controllo. I valori positivi applicano l'effetto, mentre i valori negativi possono invertirlo (predefinito: 1.0). | FLOAT | Sì | -10.0 a 10.0 (passo 0.01) |
| `image` | Un'immagine base opzionale per guidare il processo di generazione. | IMAGE | No | - |
| `inpaint_image` | Un'immagine opzionale utilizzata specificamente per le aree di inpainting definite da una maschera. | IMAGE | No | - |
| `mask` | Una maschera opzionale che definisce quali aree di un'immagine devono essere modificate o riempite tramite inpainting. | MASK | No | - |
| `start_percent` | Il punto nel processo di denoising, come frazione del numero totale di passaggi di campionamento, in cui la rete di controllo inizia ad avere effetto (predefinito: 0.0). | FLOAT | No | 0.0 a 1.0 (passo 0.001) |
| `end_percent` | Il punto nel processo di denoising in cui la rete di controllo smette di avere effetto (predefinito: 1.0). | FLOAT | No | 0.0 a 1.0 (passo 0.001) |

**Nota:** Il parametro `inpaint_image` viene in genere usato insieme a una `mask` per specificare il contenuto per l'inpainting. Il comportamento del nodo può cambiare in base a quali input opzionali vengono forniti (ad es., usando `image` per la guida oppure usando `image`, `mask` e `inpaint_image` per l'inpainting). I valori `start_percent` e `end_percent` limitano la rete di controllo a una finestra del processo di denoising e, al di fuori di tale finestra, il modello viene campionato senza la patch. Se `strength` è 0, oppure se nessuno dei parametri `image`, `inpaint_image` e `mask` è collegato, il nodo restituisce il modello base invariato. Per le patch Z-Image Control, una maschera fornita viene invertita (1.0 - mask) prima dell'uso, mentre una patch Qwen Image 2.1 Fun ControlNet usa la maschera così com'è. Questo nodo è contrassegnato come sperimentale.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello con la patch della rete di controllo applicata, pronto per l'uso in una pipeline di campionamento. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/it.md)

---
**Source fingerprint (SHA-256):** `9673b8b6e091713bcc93fe5fd1cfed12e6941571d1017e10ac94c19e1afd4ca1`

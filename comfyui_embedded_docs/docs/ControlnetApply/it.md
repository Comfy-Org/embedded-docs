# ControlnetApply

L'uso di ControlNet richiede la pre-elaborazione delle immagini di input. Poiché i nodi iniziali di ComfyUI non includono preprocessori né modelli ControlNet, installa prima i preprocessori ControlNet [scarica qui i preprocessori](https://github.com/Fannovel16/comfy_controlnet_preprocessors) e i modelli ControlNet corrispondenti.

## Input

| Parametro | Tipo di dato | Funzione |
| --- | --- | --- |
| `positive` | `CONDITIONING` | Dati di condizionamento positivo, provenienti da CLIP Text Encoder o da altri input di condizionamento |
| `negative` | `CONDITIONING` | Dati di condizionamento negativo, provenienti da CLIP Text Encoder o da altri input di condizionamento |
| `control_net` | `CONTROL_NET` | Il modello ControlNet da applicare, in genere fornito in input da ControlNet Loader |
| `image` | `IMAGE` | Immagine per l'applicazione di ControlNet, deve essere elaborata dal preprocessore |
| `vae` | `VAE` | Input del modello VAE |
| `strength` | `FLOAT` | Controlla la forza delle regolazioni della rete, intervallo di valori 0~10. Valori consigliati tra 0,5~1,5 sono ragionevoli. Valori più bassi consentono una maggiore libertà del modello, valori più alti impongono vincoli più severi. Valori troppo alti possono produrre immagini strane. Puoi testare e regolare questo valore per mettere a punto l'influenza della rete di controllo. |
| `start_percent` | `FLOAT` | Valore 0,000~1,000, determina quando iniziare ad applicare ControlNet come percentuale; ad es., 0,2 significa che la guida di ControlNet inizierà a influenzare la generazione dell'immagine al 20% del processo di diffusione |
| `end_percent` | `FLOAT` | Valore 0,000~1,000, determina quando interrompere l'applicazione di ControlNet come percentuale; ad es., 0,8 significa che la guida di ControlNet smetterà di influenzare la generazione dell'immagine all'80% del processo di diffusione |

### Output

| Parametro | Tipo di dato | Funzione |
| --- | --- | --- |
| `positive` | `CONDITIONING` | Dati di condizionamento positivo elaborati da ControlNet; possono essere inviati in output ai successivi nodi ControlNet o K Sampler |
| `negative` | `CONDITIONING` | Dati di condizionamento negativo elaborati da ControlNet; possono essere inviati in output ai successivi nodi ControlNet o K Sampler |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlnetApply/it.md)

# QwenImageDiffsynthControlnet

QwenImageDiffsynthControlnet applica una patch della rete di controllo di sintesi diffusiva a un modello di base. Utilizza un'immagine di input e una maschera opzionale per guidare il processo di generazione del modello con una forza regolabile, producendo un modello con patch che incorpora l'influenza della rete di controllo per una sintesi di immagini più controllata.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di base su cui applicare la patch della rete di controllo | MODEL | Sì | - |
| `model_patch` | Il modello patch della rete di controllo da applicare al modello di base | MODEL_PATCH | Sì | - |
| `vae` | Il VAE (Variational Autoencoder) utilizzato nel processo di diffusione | VAE | Sì | - |
| `image` | L'immagine di input utilizzata per guidare la rete di controllo. Vengono utilizzati solo i primi tre canali di colore (RGB); eventuali canali aggiuntivi vengono scartati | IMAGE | Sì | - |
| `strength` | La forza dell'influenza della rete di controllo (predefinito: 1.0) | FLOAT | Sì | -10.0 a 10.0 (passo 0.01) |
| `mask` | Maschera opzionale che definisce le aree in cui applicare la rete di controllo. Per le patch DiffSynth e Z-Image, la maschera viene invertita internamente prima dell'uso | MASK | No | - |
| `start_percent` | Il punto nel processo di denoising, come frazione del numero totale di passaggi di campionamento, in cui la rete di controllo inizia ad avere effetto (predefinito: 0.0) | FLOAT | No | 0.0 a 1.0 (passo 0.001) |
| `end_percent` | Il punto nel processo di denoising in cui la rete di controllo smette di avere effetto (predefinito: 1.0) | FLOAT | No | 0.0 a 1.0 (passo 0.001) |

**Nota:** I valori `start_percent` e `end_percent` limitano la rete di controllo a una finestra del processo di denoising; al di fuori di tale finestra il modello viene campionato senza la patch. Se `strength` è impostato a 0, il nodo restituisce il modello di base invariato. Quando viene fornita una maschera, questa viene invertita (1.0 - mask) e rimodellata per i percorsi Z-Image Control e DiffSynth standard, mentre una patch Qwen Image 2.1 Fun ControlNet utilizza la maschera così com'è. Il nodo sceglie la propria implementazione interna della patch dal modello patch caricato, quindi gli stessi input si comportano in modo leggermente diverso per Z-Image Control, Qwen Image 2.1 Fun ControlNet e checkpoint DiffSynth standard. Questo nodo è contrassegnato come sperimentale.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato a cui è stata applicata la patch della rete di controllo di sintesi diffusiva | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/it.md)

---
**Source fingerprint (SHA-256):** `7be42c001c2937af7ca5c2d45aa8a529574aa9117b4740c62da822910041d231`

# ModelPatchLoader

Il nodo ModelPatchLoader carica un file di patch del modello dalla cartella `model_patches` e lo prepara per l'uso in un workflow. Rileva automaticamente il tipo di patch contenuto nel file, costruisce l'architettura corrispondente, carica i pesi salvati e racchiude tutto in un model patcher, così può essere applicato ad altri modelli. Supporta molti formati di patch specializzati, inclusi rami ControlNet aggiuntivi, modelli feature embedder, adattatori, moduli di guida animation/LLLite e moduli simili.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `name` | Il nome file della patch del modello da caricare dalla cartella `model_patches`. Seleziona uno dei file di patch disponibili dall'elenco. | COMBO | Sì | Elenco generato dinamicamente di tutti i file di patch del modello trovati nella cartella `model_patches` |

Nota: questo nodo è contrassegnato come sperimentale. Il tipo di patch viene rilevato automaticamente dal contenuto del file, quindi non è necessaria alcuna selezione manuale del tipo. Il nodo legge i metadati del checkpoint e ispeziona le chiavi dei pesi per decidere quale architettura costruire (ad esempio Qwen Image block-wise ControlNet, Qwen Image 2.1 Fun ControlNet, Z-Image ControlNet, Wan Uni3C ControlNet, MiniMax H3 Fun ControlNet, SigLIP feature projection, Lightricks duration head, Anima LLLite, MultiTalk o SUPIR). I pesi vengono caricati con il caricamento sicuro abilitato, e il modello viene posizionato sul dispositivo di offload all'interno di un `CoreModelPatcher` in modo che possa essere successivamente applicato a un altro modello.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `MODEL_PATCH` | La patch del modello caricata, racchiusa in un model patcher, pronta per essere applicata a un modello nel workflow | MODEL_PATCH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/it.md)

---
**Source fingerprint (SHA-256):** `83b607f3c2b4b210e6ca3d310ef974757a6caf3c83f1d2d5165f3b8248928e9c`

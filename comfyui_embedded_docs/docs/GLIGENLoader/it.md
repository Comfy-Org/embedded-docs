# GligenLoader

Questo nodo rileva i modelli presenti nella cartella `ComfyUI/models/gligen` e legge anche i modelli da percorsi aggiuntivi configurati nel file extra_model_paths.yaml. A volte potrebbe essere necessario **aggiornare l'interfaccia di ComfyUI** per consentirle di leggere i file dei modelli dalla cartella corrispondente.

Il nodo `GLIGENLoader` è progettato per caricare modelli GLIGEN, che sono modelli generativi specializzati. Facilita il processo di recupero e inizializzazione di questi modelli da percorsi specificati, rendendoli pronti per ulteriori attività generative.

## Input

| Campo | Descrizione | Tipo di dati Comfy |
| --- | --- | --- |
| `gligen_name` | Il nome del modello GLIGEN da caricare, che specifica quale file del modello recuperare e caricare, fondamentale per l'inizializzazione del modello GLIGEN. | `COMBO[STRING]` |

## Output

| Campo | Descrizione | Tipo di dati |
| --- | --- | --- |
| `gligen` | Il modello GLIGEN caricato, pronto per l'uso in attività generative, che rappresenta il modello completamente inizializzato caricato dal percorso specificato. | `GLIGEN` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENLoader/it.md)

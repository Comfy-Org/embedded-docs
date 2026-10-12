# Carica modello di stile

Questo nodo rileva i modelli situati nella cartella `ComfyUI/models/style_models` e legge anche i modelli dai percorsi aggiuntivi configurati nel file extra_model_paths.yaml. A volte potrebbe essere necessario **aggiornare l'interfaccia di ComfyUI** per consentirle di leggere i file dei modelli dalla cartella corrispondente.

Il nodo StyleModelLoader è progettato per caricare un modello di stile da un percorso specificato. Si concentra sul recupero e sull'inizializzazione dei modelli di stile che possono essere utilizzati per applicare stili artistici specifici alle immagini, consentendo così la personalizzazione degli output visivi in base al modello di stile caricato.

## Input

| Nome parametro | Descrizione | Tipo Comfy | Tipo Python |
| --- | --- | --- | --- |
| `style_model_name` | Specifica il nome del modello di stile da caricare. Questo nome viene utilizzato per individuare il file del modello all'interno di una struttura di directory predefinita, consentendo il caricamento dinamico di modelli di stile diversi in base all'input dell'utente o alle esigenze dell'applicazione. | COMBO[STRING] | `str` |

## Output

| Nome parametro | Descrizione | Tipo Comfy | Tipo Python |
| --- | --- | --- | --- |
| `style_model` | Restituisce il modello di stile caricato, pronto per l'uso nell'applicazione degli stili alle immagini. Ciò consente la personalizzazione dinamica degli output visivi applicando stili artistici diversi. | `STYLE_MODEL` | `StyleModel` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelLoader/it.md)

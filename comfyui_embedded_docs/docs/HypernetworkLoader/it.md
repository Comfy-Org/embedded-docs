# Carica Hypernetwork

Questo nodo rileva i modelli presenti nella cartella `ComfyUI/models/hypernetworks` e legge anche i modelli da percorsi aggiuntivi configurati nel file extra_model_paths.yaml. In alcuni casi, potrebbe essere necessario **aggiornare l'interfaccia di ComfyUI** per consentirle di leggere i file dei modelli dalla cartella corrispondente.

Il nodo HypernetworkLoader è progettato per migliorare o modificare le capacità di un determinato modello applicando un hypernetwork. Carica un hypernetwork specificato e lo applica al modello, potenzialmente alterandone il comportamento o le prestazioni in base al parametro `strength`. Questo processo consente regolazioni dinamiche dell'architettura o dei parametri del modello, rendendo possibili sistemi AI più flessibili e adattivi.

## Input

| Campo | Descrizione | Tipo di dato Comfy |
| --- | --- | --- |
| `model` | Il modello di base a cui verrà applicato l'hypernetwork, che determina l'architettura da migliorare o modificare. | `MODEL` |
| `hypernetwork_name` | Il nome dell'hypernetwork da caricare e applicare al modello, che influisce sul comportamento o sulle prestazioni modificate del modello. | `COMBO[STRING]` |
| `strength` | Uno scalare che regola l'intensità dell'effetto dell'hypernetwork sul modello, consentendo una messa a punto delle modifiche. | `FLOAT` |

## Output

| Campo | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello modificato dopo l'applicazione dell'hypernetwork, che mostra l'impatto dell'hypernetwork sul modello originale. | `MODEL` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HypernetworkLoader/it.md)

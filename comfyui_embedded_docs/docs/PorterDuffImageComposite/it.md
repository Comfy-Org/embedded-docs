# PorterDuffImageComposite

Il nodo PorterDuffImageComposite è progettato per eseguire la composizione di immagini utilizzando gli operatori di composizione Porter-Duff. Consente di combinare immagini sorgente e di destinazione secondo varie modalità di fusione, permettendo di creare effetti visivi complessi manipolando la trasparenza delle immagini e sovrapponendo immagini in modi creativi.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `source` | Il tensore dell'immagine sorgente da comporre sopra l'immagine di destinazione. Svolge un ruolo cruciale nel determinare il risultato visivo finale in base alla modalità di composizione selezionata. | `IMAGE` |
| `source_alpha` | Il canale alpha dell'immagine sorgente, che specifica la trasparenza di ogni pixel dell'immagine sorgente. Influisce su come l'immagine sorgente si fonde con l'immagine di destinazione. | `MASK` |
| `destination` | Il tensore dell'immagine di destinazione che funge da sfondo sul quale viene composta l'immagine sorgente. Contribuisce all'immagine finale composta in base alla modalità di fusione. | `IMAGE` |
| `destination_alpha` | Il canale alpha dell'immagine di destinazione, che definisce la trasparenza dei pixel dell'immagine di destinazione. Influenza la fusione delle immagini sorgente e di destinazione. | `MASK` |
| `mode` | La modalità di composizione Porter-Duff da applicare, che determina come le immagini sorgente e di destinazione vengono fuse insieme. Ogni modalità crea effetti visivi diversi. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine composta risultante dall'applicazione della modalità Porter-Duff specificata. | `IMAGE` |
| `mask` | Il canale alpha dell'immagine composta, che indica la trasparenza di ogni pixel. | `MASK` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PorterDuffImageComposite/it.md)

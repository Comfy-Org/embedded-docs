# GligenTextBoxApply

Il nodo `GLIGENTextBoxApply` è progettato per integrare il condizionamento basato su testo nell'input di un modello generativo, in particolare applicando i parametri della casella di testo e codificandoli tramite un modello CLIP. Questo processo arricchisce il condizionamento con informazioni spaziali e testuali, facilitando una generazione più precisa e sensibile al contesto.

## Input

| Parametro | Descrizione | Tipo di dato Comfy |
| --- | --- | --- |
| `conditioning_to` | Specifica il condizionamento di input iniziale a cui verranno aggiunti i parametri della casella di testo e le informazioni testuali codificate. Svolge un ruolo cruciale nel determinare l'output finale integrando nuovi dati di condizionamento. | `CONDITIONING` |
| `clip` | Il modello CLIP utilizzato per codificare il testo fornito in un formato che può essere utilizzato dal modello generativo. È essenziale per convertire le informazioni testuali in un formato di condizionamento compatibile. | `CLIP` |
| `gligen_textbox_model` | Rappresenta la configurazione specifica del modello GLIGEN da utilizzare per generare la casella di testo. È cruciale per garantire che la casella di testo venga generata secondo le specifiche desiderate. | `GLIGEN` |
| `text` | Il contenuto testuale da codificare e integrare nel condizionamento. Fornisce le informazioni semantiche che guidano il modello generativo. | `STRING` |
| `width` | La larghezza della casella di testo in pixel. Definisce la dimensione spaziale della casella di testo all'interno dell'immagine generata. | `INT` |
| `height` | L'altezza della casella di testo in pixel. Come per la larghezza, definisce la dimensione spaziale della casella di testo all'interno dell'immagine generata. | `INT` |
| `x` | La coordinata x dell'angolo superiore sinistro della casella di testo all'interno dell'immagine generata. Specifica la posizione orizzontale della casella di testo. | `INT` |
| `y` | La coordinata y dell'angolo superiore sinistro della casella di testo all'interno dell'immagine generata. Specifica la posizione verticale della casella di testo. | `INT` |

## Output

| Parametro | Descrizione | Tipo di dato Comfy |
| --- | --- | --- |
| `conditioning` | L'output di condizionamento arricchito, che include i dati di condizionamento originali insieme ai parametri della casella di testo appena aggiunti e alle informazioni testuali codificate. Viene utilizzato per guidare il modello generativo nella produzione di output sensibili al contesto. | `CONDITIONING` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GligenTextBoxApply/it.md)

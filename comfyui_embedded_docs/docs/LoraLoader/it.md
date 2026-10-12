# Carica LoRA (Modello e CLIP)

Questo nodo rileva automaticamente i modelli situati nella cartella LoRA (incluse le sottocartelle), il cui percorso modello corrispondente è `ComfyUI\models\loras`. Per ulteriori informazioni, consulta Installazione dei modelli LoRA

Il nodo LoRA Loader viene utilizzato principalmente per caricare modelli LoRA. Puoi pensare ai modelli LoRA come a dei filtri che possono conferire alle tue immagini stili, contenuti e dettagli specifici:

- Applicare stili artistici specifici (come la pittura a inchiostro)
- Aggiungere caratteristiche di determinati personaggi (come i personaggi dei videogiochi)
- Aggiungere dettagli specifici all'immagine

Tutto ciò può essere ottenuto tramite LoRA.

Se hai bisogno di caricare più modelli LoRA, puoi concatenare direttamente più nodi tra loro, come mostrato di seguito:

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | In genere viene utilizzato per collegarsi al modello base | MODEL |
| `clip` | In genere viene utilizzato per collegarsi al modello CLIP | CLIP |
| `lora_name` | Seleziona il nome del modello LoRA da utilizzare | COMBO[STRING] |
| `strength_model` | Intervallo di valori da -100.0 a 100.0, in genere utilizzato tra 0~1 per la generazione quotidiana di immagini. Valori più alti producono effetti di regolazione del modello più pronunciati | FLOAT |
| `strength_clip` | Intervallo di valori da -100.0 a 100.0, in genere utilizzato tra 0~1 per la generazione quotidiana di immagini. Valori più alti producono effetti di regolazione più pronunciati | FLOAT |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello con le regolazioni LoRA applicate | MODEL |
| `clip` | L'istanza CLIP con le regolazioni LoRA applicate | CLIP |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoader/it.md)

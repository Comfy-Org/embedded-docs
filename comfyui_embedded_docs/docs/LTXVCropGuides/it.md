# LTXVCropGuides

Il nodo LTXVCropGuides rimuove i dati di guida dei keyframe da un flusso di lavoro di generazione video. Conta i keyframe registrati nel condizionamento positivo, ritaglia quel numero di fotogrammi dalla fine dei campioni latenti e della maschera di rumore, e cancella l'indice dei keyframe e le voci di attenzione guida da entrambi gli input di condizionamento. Quando non viene trovato alcun keyframe, gli input di condizionamento vengono restituiti invariati e il latent viene passato attraverso con un tensore di campioni clonato e la sua maschera di rumore.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | L'input di condizionamento positivo contenente informazioni di guida per la generazione. Il numero di keyframe che contiene determina quanti fotogrammi vengono ritagliati dal latent. | CONDITIONING | Sì | - |
| `negative` | L'input di condizionamento negativo contenente informazioni di guida su ciò che va evitato nella generazione. I suoi dati sui keyframe vengono cancellati insieme al condizionamento positivo. | CONDITIONING | Sì | - |
| `latent` | La rappresentazione latente contenente campioni di immagine e dati della maschera di rumore. Quando sono presenti keyframe, i fotogrammi dei keyframe finali vengono rimossi sia dai campioni sia dalla maschera di rumore. | LATENT | Sì | - |

Nota: Il ritaglio avviene solo quando vengono rilevati indici di keyframe nel condizionamento positivo. Se non viene rilevato alcun keyframe, i condizionamenti positivo e negativo vengono restituiti invariati, mentre il latent viene comunque restituito con un tensore di campioni clonato e una maschera di rumore esplicita (se il latent di input non ne ha una, viene creata una maschera di tutti uno).

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Il condizionamento positivo elaborato con indici dei keyframe e voci di attenzione guida cancellati | CONDITIONING |
| `negative` | Il condizionamento negativo elaborato con indici dei keyframe e voci di attenzione guida cancellati | CONDITIONING |
| `latent` | La rappresentazione latente ritagliata con campioni e maschera di rumore adattati, in cui le sezioni dei keyframe sono state rimosse | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/it.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`

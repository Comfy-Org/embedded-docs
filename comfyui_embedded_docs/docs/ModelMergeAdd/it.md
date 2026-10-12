# ModelMergeAdd

Il nodo ModelMergeAdd è progettato per unire due modelli aggiungendo patch chiave da un modello all'altro. Questo processo prevede la clonazione del primo modello e quindi l'applicazione delle patch dal secondo modello, consentendo la combinazione delle caratteristiche o dei comportamenti di entrambi i modelli.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model1` | Il primo modello da clonare e al quale verranno aggiunte le patch dal secondo modello. Funge da modello di base per il processo di unione. | `MODEL` |
| `model2` | Il secondo modello dal quale vengono estratte le patch chiave e aggiunte al primo modello. Contribuisce con caratteristiche o comportamenti aggiuntivi al modello unito. | `MODEL` |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il risultato dell'unione di due modelli tramite l'aggiunta di patch chiave dal secondo modello al primo. Questo modello unito combina le caratteristiche o i comportamenti di entrambi i modelli. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAdd/it.md)

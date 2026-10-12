# PairConditioningCombine

Il nodo PairConditioningCombine unisce due coppie separate di condizionamento (ciascuna composta da un condizionamento positivo e uno negativo) in un'unica coppia combinata. Riceve il condizionamento positivo e negativo da due sorgenti diverse e li combina usando la logica interna di ComfyUI, restituendo un condizionamento positivo finale e un condizionamento negativo finale. Questo nodo è sperimentale ed è progettato per flussi di lavoro avanzati di manipolazione del condizionamento.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive_A` | Primo input di condizionamento positivo | CONDITIONING | Sì | - |
| `negative_A` | Primo input di condizionamento negativo | CONDITIONING | Sì | - |
| `positive_B` | Secondo input di condizionamento positivo | CONDITIONING | Sì | - |
| `negative_B` | Secondo input di condizionamento negativo | CONDITIONING | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Output di condizionamento positivo combinato | CONDITIONING |
| `negative` | Output di condizionamento negativo combinato | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/it.md)

---
**Source fingerprint (SHA-256):** `34c14207930ba31fea054b2e641e9666e738ed786aa117449c4a27667bde41b1`

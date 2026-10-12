# Finestre di Contesto LTXV

Questo nodo imposta finestre di contesto per modelli simili a LTXV durante il campionamento. Divide la generazione in finestre sovrapposte per aiutare a gestire l'uso della memoria e migliorare la coerenza temporale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello a cui applicare le finestre di contesto durante il campionamento. | MODEL | Sì | - |
| `context_length` | La lunghezza della finestra di contesto in frame reali. Deve essere 8*n + 1. (predefinito: 145) | INT | Sì | Minimo: 1<br>Massimo: nodes.MAX_RESOLUTION<br>Passo: 8 |
| `context_overlap` | La sovrapposizione della finestra di contesto in frame reali. (predefinito: 40) | INT | Sì | Minimo: 0<br>Passo: 8 |
| `context_schedule` | Algoritmo di pianificazione dipendente dallo step per le finestre di contesto. (predefinito: "UNIFORM_STANDARD") | COMBO | Sì | `"STATIC_STANDARD"`<br>`"UNIFORM_STANDARD"`<br>`"UNIFORM_LOOPED"`<br>`"BATCHED"` |
| `context_stride` | Il passo della finestra di contesto; applicabile solo alle pianificazioni uniformi. (predefinito: 1) | INT | Sì | Minimo: 1 |
| `closed_loop` | Se chiudere il ciclo della finestra di contesto; applicabile solo alle pianificazioni a ciclo. (predefinito: False) | BOOLEAN | Sì | True<br>False |
| `fuse_method` | Il metodo da usare per fondere le finestre di contesto. Le opzioni disponibili sono definite da `ContextFuseMethods.LIST_STATIC`. (predefinito: "PYRAMID") | COMBO | Sì | Definito da `ContextFuseMethods.LIST_STATIC` |
| `freenoise` | Se applicare lo shuffling del rumore FreeNoise, migliora la fusione delle finestre. (predefinito: True) | BOOLEAN | Sì | True<br>False |
| `retain_first_frame` | Mantieni il primo frame latente in ogni finestra di contesto (può aiutare a mantenere il riferimento iniziale). (predefinito: False) | BOOLEAN | Sì | True<br>False |
| `split_conds_to_windows` | Se suddividere più condizionamenti (creati da ConditionCombine) in ciascuna finestra in base all'indice di regione. (predefinito: False) | BOOLEAN | Sì | True<br>False |

**Nota:** Il valore `context_length` è fornito in frame reali e viene convertito internamente in frame latenti usando la formula `((context_length - 1) // 8) + 1`, con un minimo di 1. Anche il valore `context_overlap` è fornito in frame reali e viene convertito in frame latenti usando la divisione intera per 8, con un minimo di 0. Il tooltip per `context_length` indica che deve seguire il pattern 8*n + 1.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `MODEL` | Il modello con le finestre di contesto applicate per il campionamento. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/it.md)

---
**Source fingerprint (SHA-256):** `148649d0a938e08c932a163f5d7614332626fba37b8f79db7f92bbcf422e692f`

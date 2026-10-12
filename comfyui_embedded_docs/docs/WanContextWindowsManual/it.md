# WanContextWindowsManual

Il nodo WAN Context Windows (Manual) consente di configurare manualmente le finestre di contesto per i modelli video in stile Wan. Applica queste impostazioni durante il campionamento, offrendo controllo su lunghezza della finestra, sovrapposizione, pianificazione e metodo di fusione usati mentre il modello elabora il video. La lunghezza del contesto e la sovrapposizione sono specificate in frame reali e vengono convertite internamente per l'elaborazione 2D del modello.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui applicare le finestre di contesto durante il campionamento. | MODEL | Sì | - |
| `context_length` | La lunghezza della finestra di contesto in frame reali. Deve essere 4*n + 1 (predefinito: 81). | INT | Sì | da 1 a 16384 (MAX_RESOLUTION), passo 4 |
| `context_overlap` | La sovrapposizione della finestra di contesto in frame reali (predefinito: 30). | INT | Sì | 0 o superiore |
| `context_schedule` | Algoritmo di pianificazione dipendente dal passo per le finestre di contesto (predefinito: "uniform_standard"). | COMBO | Sì | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `context_stride` | Lo stride della finestra di contesto; applicabile solo alle pianificazioni uniformi (predefinito: 1). | INT | Sì | 1 o superiore |
| `closed_loop` | Indica se chiudere il ciclo della finestra di contesto; applicabile solo alle pianificazioni cicliche (predefinito: False). | BOOLEAN | Sì | - |
| `fuse_method` | Il metodo da usare per fondere le finestre di contesto (predefinito: "pyramid"). | COMBO | Sì | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | Indica se applicare il rimescolamento del rumore di FreeNoise, migliora la fusione delle finestre (predefinito: True). | BOOLEAN | Sì | - |
| `retain_first_frame` | Mantiene il primo frame I2V in ogni finestra di contesto (può aiutare a mantenere il riferimento iniziale) (predefinito: False). | BOOLEAN | Sì | - |
| `split_conds_to_windows` | Indica se suddividere più conditioning (creati da ConditionCombine) in ciascuna finestra in base all'indice di regione (predefinito: False). | BOOLEAN | Sì | - |

**Nota:** `context_stride` influisce solo sulle pianificazioni uniformi, mentre `closed_loop` si applica solo alle pianificazioni cicliche. La lunghezza e la sovrapposizione del contesto sono specificate in frame reali e vengono automaticamente convertite e limitate ai valori minimi validi durante l'elaborazione (`context_length` diventa ((length - 1) / 4) + 1, `context_overlap` diventa overlap / 4). `context_length` deve rispettare la forma 4*n + 1. `retain_first_frame` è pensato per l'uso image-to-video. `split_conds_to_windows` prevede più conditioning creati dal nodo ConditionCombine. Il parametro `fuse_method` include diverse opzioni oltre a "pyramid".

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello con la configurazione delle finestre di contesto applicata. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/it.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`

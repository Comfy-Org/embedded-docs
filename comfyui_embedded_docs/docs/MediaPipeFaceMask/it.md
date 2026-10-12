# MediaPipeFaceMask

## Panoramica

Questo nodo crea una maschera binaria (un'immagine in bianco e nero) basata sui landmark del volto rilevati da MediaPipe. Disegna forme poligonali riempite per ciascuna regione del volto rilevata, producendo una maschera per fotogramma in un batch. Quando più volti vengono rilevati nello stesso fotogramma, le loro maschere vengono combinate in un'unica maschera.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `face_landmarks` | I dati dei landmark del volto provenienti da un nodo di rilevamento del volto MediaPipe. | FACE_LANDMARKS | Sì | - |
| `regions` | Seleziona quali regioni facciali includere nella maschera. `"all"` crea una maschera dall'unione di tutte le regioni del volto (ovale del volto, labbra, occhi, iridi). `"custom"` consente di attivare/disattivare ogni regione singolarmente. Predefinito: `"all"` | COMBO | Sì | `"all"`<br>`"custom"` |

Quando `regions` è impostato su `"custom"`, diventano disponibili i seguenti parametri booleani aggiuntivi:

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `face_oval` | Include la regione dell'ovale del volto nella maschera. Predefinito: True | BOOLEAN | No | True/False |
| `lips` | Include la regione delle labbra nella maschera. Predefinito: True | BOOLEAN | No | True/False |
| `eyes` | Include la regione degli occhi nella maschera. Predefinito: True | BOOLEAN | No | True/False |
| `irises` | Include la regione delle iridi nella maschera. Predefinito: True | BOOLEAN | No | True/False |

**Nota:** Quando si utilizza la modalità `"all"`, la maschera include tutte le regioni combinate. Poiché l'ovale del volto racchiude le altre regioni, selezionare `"all"` produce di fatto lo stesso risultato che selezionare solo l'ovale del volto.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `MASK` | Un tensore di maschera binaria in cui le regioni del volto sono bianche (valore 1.0) e lo sfondo è nero (valore 0.0). La maschera ha le stesse dimensioni dell'immagine di input e contiene una maschera per fotogramma nel batch. | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMask/it.md)

---
**Source fingerprint (SHA-256):** `92270002a42ed59bc75e676a6881e1899186d3c8a1bb4dd4c0d39b3762b5bb66`

# LotusConditioning

Il nodo LotusConditioning fornisce embedding di conditioning fissi e precalcolati per il modello Lotus. Poiché Lotus utilizza un encoder congelato con conditioning nullo, il nodo incorpora direttamente gli embedding del prompt risultanti invece di eseguire inferenza o caricare grandi file di tensori, quindi il suo output non cambia mai. Il conditioning restituito può essere collegato direttamente a una pipeline di generazione che si aspetta un conditioning compatibile con Lotus.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| *Nessun input* | Questo nodo non accetta alcun parametro di input. | - | - | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `conditioning` | Gli embedding di conditioning precalcolati per il modello Lotus. Restituito come lista di conditioning che contiene gli embedding fissi del prompt insieme a un dizionario vuoto. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/it.md)

---
**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`

# CLIPSubtract

Il nodo CLIPSubtract esegue un'operazione di sottrazione tra due modelli CLIP. Prende il primo modello CLIP come base e sottrae le patch chiave dal secondo modello CLIP, con un moltiplicatore opzionale per controllare l'intensità della sottrazione. Ciò consente una fusione di modelli sottoposti a fine-tuning rimuovendo caratteristiche specifiche da un modello usando un altro.

## Input

| Parametro | Descrizione | Tipo di dato | Tipo di input | Predefinito | Intervallo |
| --- | --- | --- | --- | --- | --- |
| `clip1` | Il modello CLIP di base che verrà modificato | CLIP | Obbligatorio | - | - |
| `clip2` | Il modello CLIP le cui patch chiave verranno sottratte dal modello di base | CLIP | Obbligatorio | - | - |
| `multiplier` | Controlla la forza dell'operazione di sottrazione. I valori positivi sottraggono caratteristiche da clip2, mentre i valori negativi aggiungono invece caratteristiche. | FLOAT | Obbligatorio | 1.0 | -10.0 to 10.0, step 0.01 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CLIP` | Il modello CLIP risultante dopo l'operazione di sottrazione | CLIP |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/it.md)

---
**Source fingerprint (SHA-256):** `ea7b6f838d6eb083d2d9bc07891b6ef2f3e625861ab1de9279df351e58f2a2a8`

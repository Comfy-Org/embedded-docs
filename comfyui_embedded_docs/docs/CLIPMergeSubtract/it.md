# CLIPMergeSubtract

Il nodo CLIPMergeSubtract esegue la fusione dei modelli sottraendo i pesi di un modello CLIP da un altro. Crea un nuovo modello CLIP clonando il primo modello e poi sottraendo le patch chiave dal secondo modello, con un moltiplicatore regolabile per controllare la forza della sottrazione. Ciò consente una miscelazione di modelli ottimizzati rimuovendo caratteristiche specifiche dal modello di base.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip1` | Il modello CLIP di base che verrà clonato e modificato | CLIP | Sì | - |
| `clip2` | Il modello CLIP i cui patch chiave verranno sottratte dal modello di base | CLIP | Sì | - |
| `multiplier` | Controlla la forza dell'operazione di sottrazione (predefinito: 1.0) | FLOAT | Sì | da -10.0 a 10.0 (passo: 0.01) |

**Nota:** Il nodo esclude i parametri `.position_ids` e `.logit_scale` dall'operazione di sottrazione, indipendentemente dal valore del moltiplicatore.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `clip` | Il modello CLIP risultante dopo aver sottratto i pesi del secondo modello dal primo | CLIP |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/it.md)

---
**Source fingerprint (SHA-256):** `62a8cf719c34d9e2b7321f6eeb03c881f0767fd36b80e25e74feff4c0a29045e`

# CreateList

Il nodo Create List combina più input in un'unica lista sequenziale. Accetta un numero qualsiasi di slot di input che condividono lo stesso tipo di dato e concatena i loro elementi nell'ordine in cui gli slot sono collegati. Il risultato è un'unica lista contenente tutti gli elementi collegati.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `inputs` | Un numero variabile di slot di input denominati `input`, `input_2`, `input_3` e così via. Ogni slot accetta una lista di elementi dello stesso tipo di dato (ad esempio, tutti IMAGE o tutti STRING). Nuovi slot vengono creati automaticamente quando necessario. Il nodo concatena le liste nell'ordine degli slot. | Any | Sì | Numero qualsiasi di slot; ogni slot accetta un numero qualsiasi di elementi |

**Nota:** Tutti gli input collegati devono condividere lo stesso tipo di dato. Ogni slot collegato fornisce una lista di elementi e il nodo combina le liste nell'ordine degli slot (`input`, poi `input_2`, poi `input_3`, ...). Il nodo è anche ricercabile con gli alias "Image Iterator", "Text Iterator" e "Iterator".

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `list` | Un'unica lista contenente tutti gli elementi dagli input collegati, concatenati nell'ordine in cui gli slot sono stati forniti. Il tipo di dato dell'output corrisponde al tipo di dato dell'input. | Any |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/it.md)

---
**Source fingerprint (SHA-256):** `4824fa6af46ab08cd3c10b033dbb3e43682b468e1dbd934fffb571349e025b96`

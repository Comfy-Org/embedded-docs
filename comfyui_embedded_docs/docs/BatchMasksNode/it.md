# BatchMasksNode

Il nodo Batch Masks combina più input maschera individuali in un unico batch. Accetta un numero variabile di input maschera e li restituisce come un singolo tensore di maschera raggruppato in batch, consentendo l'elaborazione in batch delle maschere nei nodi successivi. Se le maschere di input hanno dimensioni diverse, vengono ridimensionate automaticamente per corrispondere alle dimensioni della prima maschera.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `mask` | Gli input maschera da combinare in un batch. È richiesta almeno una maschera. Puoi aggiungere fino a 50 maschere in totale facendo clic sul pulsante "+" sul nodo. Se le maschere hanno dimensioni diverse, vengono ridimensionate automaticamente per corrispondere alle dimensioni della prima maschera. | MASK | Sì | Da 1 a 50 maschere |

**Nota:** Questo nodo utilizza un modello di input autogrow. Devi collegare almeno una maschera. Puoi aggiungere fino ad altri 49 input maschera per un totale di 50 maschere. Tutte le maschere collegate verranno combinate in un unico batch. Se le maschere hanno altezze o larghezze diverse, vengono ridimensionate automaticamente per corrispondere alle dimensioni della prima maschera utilizzando l'interpolazione bilineare.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Una singola maschera in batch contenente tutte le maschere di input impilate insieme. Se non viene fornita alcuna maschera, restituisce None. | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchMasksNode/it.md)

---
**Source fingerprint (SHA-256):** `7e9bc4be72c7fa8fceab2cf167c72b7e1ff858c0281d977f2ad3ab433d9d58d6`

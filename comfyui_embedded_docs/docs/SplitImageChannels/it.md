# Split Image Channels

Suddivide un'immagine nei suoi canali rosso, verde e blu e restituisce il canale alpha come maschera. Ogni output di colore è un'immagine in scala di grigi a tre canali, quindi può essere visualizzata in anteprima e salvata come un'immagine normale. Usalo per ispezionare o modificare un singolo canale oppure per estrarre la trasparenza da un'immagine.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine da suddividere. Un input a canale singolo (scala di grigi) viene espanso in modo che tutti e tre gli output di colore contengano gli stessi dati. | IMAGE | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `red` | Il canale rosso, come immagine in scala di grigi a tre canali. | IMAGE |
| `green` | Il canale verde, come immagine in scala di grigi a tre canali. | IMAGE |
| `blue` | Il canale blu, come immagine in scala di grigi a tre canali. | IMAGE |
| `alpha` | Alpha come maschera, invertita allo stesso modo di Load Image, quindi 1 indica i pixel completamente trasparenti. Un'immagine senza canale alpha restituisce una maschera con tutti i valori a zero. | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageChannels/it.md)

---
**Source fingerprint (SHA-256):** `0f300d2e86c74e856001eb82da26c871c94c1dae5ec73a4504ca258420fbcf52`

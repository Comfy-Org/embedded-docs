# Empty Flux 2 Latent

Il nodo Empty Flux 2 Latent crea una rappresentazione latente vuota riempita di zeri. Viene utilizzato come punto di partenza per il processo di denoising del modello Flux. Le dimensioni latenti sono ricavate dai valori di input `width` e `height`, ciascuno diviso per 16.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `width` | La larghezza dell'immagine finale da generare. La larghezza latente sarà questo valore diviso per 16. Il valore predefinito è 1024. | INT | Sì | 16 a 16384 |
| `height` | L'altezza dell'immagine finale da generare. L'altezza latente sarà questo valore diviso per 16. Il valore predefinito è 1024. | INT | Sì | 16 a 16384 |
| `batch_size` | Il numero di campioni latenti da generare in un singolo batch. Il valore predefinito è 1. | INT | No | 1 a 4096 |

**Nota:** Gli input `width` e `height` usano un passo di 16, quindi devono essere divisibili per 16. Questo perché il nodo li divide per questo fattore per creare le dimensioni latenti.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `samples` | Un tensore latente riempito di zeri. La forma è `[batch_size, 128, height // 16, width // 16]`. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/it.md)

---
**Source fingerprint (SHA-256):** `f8356568f0ab521a3f246d1f672492e74f9a2f449694961b913bd14a5f0f3878`

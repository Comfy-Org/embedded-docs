# LtxvApiImageToVideo

Il nodo LTXV Image To Video genera un video di qualità professionale da una singola immagine iniziale. Utilizza un'API esterna per creare una sequenza video basata sul tuo prompt testuale, consentendoti di personalizzare durata, risoluzione e frame rate.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | Primo fotogramma da utilizzare per il video. | IMAGE | Sì | - |
| `model` | Il modello AI da utilizzare per la generazione video. Il modello "Pro" è ottimizzato per la qualità, mentre il modello "Fast" è ottimizzato per la velocità. | COMBO | Sì | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | Una descrizione testuale che guida il contenuto e il movimento del video generato (predefinito: vuoto). | STRING | Sì | - |
| `duration` | La durata del video in secondi (predefinito: 8). | COMBO | Sì | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | La risoluzione di output del video generato. | COMBO | Sì | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | I fotogrammi al secondo per il video (predefinito: 25). | COMBO | Sì | `25`<br>`50` |
| `generate_audio` | Se true, il video generato includerà audio generato dall'IA coerente con la scena (predefinito: False). | BOOLEAN | No | - |

**Vincoli importanti:**

* L'input `image` deve contenere esattamente un'immagine.
* Il `prompt` deve essere lungo tra 1 e 10.000 caratteri.
* Se selezioni una `duration` superiore a 10 secondi, devi usare il modello **"LTX-2 (Fast)"**, una risoluzione **"1920x1080"** e **25** FPS. Questa combinazione è necessaria per video più lunghi.

**Nota:** Questo nodo è contrassegnato come deprecato. Il costo stimato visualizzato sul nodo dipende dal `model`, dalla `duration` e dalla `resolution` selezionati.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `video` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/it.md)

---
**Source fingerprint (SHA-256):** `fa3928262e59105718b6ed97ddc8d2801e540b6b0c142541d92525dd75540cc7`

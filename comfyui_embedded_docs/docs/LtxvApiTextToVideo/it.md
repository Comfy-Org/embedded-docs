# LtxvApiTextToVideo

Il nodo LTXV Text To Video genera video di qualità professionale da una descrizione testuale. Si connette a un'API esterna per creare video con durata, risoluzione e frequenza dei fotogrammi personalizzabili. Puoi anche scegliere di aggiungere al video audio generato dall'IA.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello AI da utilizzare per la generazione del video. "LTX-2 (Pro)" offre una qualità superiore, mentre "LTX-2 (Fast)" è ottimizzato per la velocità. | COMBO | Sì | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | La descrizione testuale che l'IA utilizzerà per generare il video. Questo campo supporta più righe di testo e deve contenere da 1 a 10.000 caratteri. Predefinito: "" (vuoto). | STRING | Sì | - |
| `duration` | La durata del video generato in secondi (predefinito: 8). | COMBO | Sì | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | Le dimensioni in pixel (larghezza x altezza) del video di output. | COMBO | Sì | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | I fotogrammi al secondo del video (predefinito: 25). | COMBO | Sì | `25`<br>`50` |
| `generate_audio` | Se impostato su true, il video generato includerà audio generato dall'IA coerente con la scena (predefinito: False). Questa è un'impostazione avanzata opzionale. | BOOLEAN | No | - |

**Vincoli importanti:**

* Il `prompt` deve avere una lunghezza compresa tra 1 e 10.000 caratteri.
* Se si seleziona una `duration` maggiore di 10 secondi, è necessario utilizzare anche il modello `"LTX-2 (Fast)"`, una risoluzione `"1920x1080"` e un `fps` di `25`. Questa combinazione è richiesta per video più lunghi.
* Il prezzo dipende dal `model`, dalla `duration` e dalla `resolution` selezionati.

**Nota:** Questo nodo è deprecato.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/it.md)

---
**Source fingerprint (SHA-256):** `8cf7409e46bb92abdff8a12e0d4ab49d67bb70e66c0c9074c9af99d1cf250df8`

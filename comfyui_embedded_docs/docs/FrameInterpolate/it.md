# FrameInterpolate

Il nodo Frame Interpolate crea nuovi frame tra quelli esistenti in una sequenza di immagini, aumentando di fatto la frequenza dei fotogrammi. Utilizza un modello AI per prevedere l'aspetto che dovrebbero avere i frame intermedi, il che può essere usato per creare effetti al rallentatore fluidi o per aumentare la fluidità di un video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `interp_model` | Il modello di interpolazione dei frame da usare per generare i frame intermedi | INTERP_MODEL | Sì | - |
| `images` | Un batch di immagini consecutive (frame) tra cui interpolare. Richiede almeno 2 immagini. Se vengono forniti meno di 2 frame, il nodo restituisce le immagini di input invariate. | IMAGE | Sì | - |
| `multiplier` | Il numero di volte di cui moltiplicare il conteggio dei frame. Ad esempio, un moltiplicatore di 2 raddoppia il numero di frame. (predefinito: 2) | INT | Sì | da 2 a 16 |

**Nota:** Il nodo richiede almeno 2 frame di input e un `multiplier` pari almeno a 2. Se una delle due condizioni non è soddisfatta, le immagini di input vengono restituite invariate.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `IMAGE` | Un nuovo batch di immagini con i frame interpolati inseriti tra i frame originali, ottenendo una sequenza più fluida. Il numero totale di frame in output è `(number of input frames - 1) * multiplier + 1`. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/it.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`

# AnimaLLLiteApply

AnimaLLLiteApply applica una patch di animazione leggera a un modello di diffusione, consentendo una generazione controllata da immagine a immagine con forza e tempistica regolabili. Integra una patch del modello preconfigurata con un'immagine di input e una maschera opzionale, modificando i layer di attenzione e MLP del modello per influenzare il processo di generazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello di diffusione di base a cui applicare la patch | MODEL | Sì | |
| `model_patch` | La patch di animazione preconfigurata da applicare | MODEL_PATCH | Sì | |
| `image` | L'immagine di riferimento per guidare la generazione. Vengono usati solo i primi 3 canali di colore (RGB) | IMAGE | Sì | |
| `strength` | La forza dell'effetto della patch (predefinito: 1.0, passo: 0.01) | FLOAT | Sì | da -10.0 a 10.0 |
| `start_percent` | La percentuale del processo di denoising alla quale la patch inizia ad avere effetto (predefinito: 0.0, passo: 0.001) | FLOAT | Sì | da 0.0 a 1.0 |
| `end_percent` | La percentuale del processo di denoising alla quale la patch smette di avere effetto (predefinito: 1.0, passo: 0.001) | FLOAT | Sì | da 0.0 a 1.0 |
| `mask` | Una maschera opzionale per limitare l'effetto della patch ad aree specifiche dell'immagine | MASK | No | |

**Nota sui vincoli dei parametri:** Se il `model_patch` ha 4 canali di input e non viene fornita alcuna `mask`, viene creata automaticamente una maschera di zeri per corrispondere alle dimensioni dell'immagine. Se il `model_patch` non ha 4 canali di input, il parametro `mask` viene ignorato e impostato a `None`. Vengono usati solo i primi 3 canali di colore dell'immagine di input. Questo nodo è contrassegnato come sperimentale in ComfyUI.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `MODEL` | Il modello di diffusione con patch a cui è stata applicata la patch di animazione | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AnimaLLLiteApply/it.md)

---
**Source fingerprint (SHA-256):** `48e455b767509a5a8c329365d5ffded86d6f4545d575c9fdc5ffbaf4da7c2287`

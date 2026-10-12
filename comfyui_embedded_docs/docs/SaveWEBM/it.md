# Salva WEBM

Il nodo SaveWEBM salva una sequenza di immagini come file video WEBM. Riceve più immagini di input e le codifica in un video utilizzando il codec VP9 o AV1 con impostazioni di qualità e frame rate configurabili. Il file video risultante viene salvato nella directory di output con metadati che includono le informazioni del prompt.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `images` | Le immagini RGBA vengono salvate con il loro canale alfa come trasparenza (solo codec vp9). | IMAGE | Sì | - |
| `filename_prefix` | Prefisso per il nome del file di output (predefinito: "ComfyUI"). | STRING | No | - |
| `codec` | Codec video da utilizzare per la codifica. | COMBO | Sì | "vp9"<br>"av1" |
| `fps` | Frame rate per il video di output (predefinito: 24.0). | FLOAT | No | 0.01-1000.0 |
| `crf` | Un crf più alto indica una qualità inferiore con un file di dimensioni minori; un crf più basso indica una qualità superiore con un file di dimensioni maggiori (predefinito: 32.0). | FLOAT | No | 0-63.0 |

**Nota sul canale alfa:** Il canale alfa delle immagini RGBA viene preservato solo quando si utilizza il codec VP9. Quando si utilizza il codec AV1, il canale alfa viene ignorato e vengono codificati solo i dati RGB.

**Nota sulla denominazione dei file:** I video vengono salvati nella directory di output come `{filename_prefix}_{counter:05}_.webm`, dove il contatore viene incrementato automaticamente per evitare di sovrascrivere file esistenti.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `images` | Le immagini di input, passate invariate dopo il salvataggio del video. | IMAGE |
| UI preview | Anteprima video che mostra il file WEBM salvato. | PREVIEW |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/it.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`

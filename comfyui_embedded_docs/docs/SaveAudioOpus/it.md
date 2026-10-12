# SaveAudioOpus

Il nodo SaveAudioOpus salva i dati audio in un file nel formato Opus, consentendoti di scegliere la qualità di codifica (bitrate) e il prefisso del nome file per il file esportato. Questo nodo è deprecato e potrebbe essere rimosso nelle versioni future.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `audio` | I dati audio da salvare come file Opus. Viene generato un ValueError se questo è None (ad esempio, quando il video di origine non ha una traccia audio). | AUDIO | Sì | - |
| `filename_prefix` | Il prefisso utilizzato per il nome file di output (predefinito: "audio/ComfyUI"). | STRING | No | - |
| `quality` | Il bitrate utilizzato per codificare il file Opus; valori più alti producono una qualità migliore ma file più grandi (predefinito: "128k"). | COMBO | No | `"64k"`<br>`"96k"`<br>`"128k"`<br>`"192k"`<br>`"320k"` |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `audio` | I dati audio che sono stati salvati nel file Opus. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/it.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`

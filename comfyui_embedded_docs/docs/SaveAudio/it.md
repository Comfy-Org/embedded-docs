# SaveAudio

Questo nodo salva i dati audio in un file in formato FLAC. Prende un input audio e lo scrive nella directory di output utilizzando il prefisso del nome file specificato, inoltre passa l'audio al suo output. Questo nodo è deprecato e dovrebbe essere sostituito con il nodo Save Audio attuale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `audio` | I dati audio da salvare | AUDIO | Sì | - |
| `filename_prefix` | Il prefisso per il nome file di output (predefinito: "audio/ComfyUI") | STRING | No | - |

*Nota: i parametri `prompt` e `extra_pnginfo` sono nascosti e gestiti automaticamente dal sistema.*

Se l'input `audio` non riceve dati (ad esempio, quando il video di origine non ha una traccia audio), il nodo genera un errore e non viene salvato alcun file.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-----------|-----------|
| `audio` | I dati audio forniti all'input, passati attraverso dopo il salvataggio del file | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/it.md)

---
**Source fingerprint (SHA-256):** `6ac62d315f14213091cd179a05f0bbd51f1b1a5056bb5c06ca137d2b574d6017`

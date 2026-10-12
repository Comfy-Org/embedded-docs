# AudioConcat

Il nodo AudioConcat combina due input audio unendoli insieme. Riceve due input audio e li connette nell'ordine specificato, posizionando il secondo audio prima o dopo il primo audio. Il nodo gestisce automaticamente formati audio diversi convertendo l'audio mono in stereo e allineando le frequenze di campionamento tra i due input.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio1` | Il primo input audio da concatenare | AUDIO | Sì | - |
| `audio2` | Il secondo input audio da concatenare | AUDIO | Sì | - |
| `direction` | Indica se aggiungere `audio2` dopo o prima di `audio1` (predefinito: "after") | COMBO | Sì | `"after"`<br>`"before"` |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `AUDIO` | L'audio combinato contenente entrambi i file audio di input uniti insieme | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/it.md)

---
**Source fingerprint (SHA-256):** `faccc3d42e9c6927deadb7d5f7fe9e5bbbf08e4e9a3d636f42a2b9f995eec8c1`

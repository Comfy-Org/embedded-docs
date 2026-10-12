# AudioEncoderLoader

## Panoramica

Il nodo AudioEncoderLoader carica un modello audio encoder da un file memorizzato nella cartella `audio_encoders`. Riceve come input il nome del file di un modello audio encoder e restituisce il modello caricato, che può quindi essere utilizzato per attività di elaborazione audio nel workflow. Se il file selezionato non contiene un modello audio encoder valido, il nodo genera un errore.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio_encoder_name` | Seleziona quale file di modello audio encoder caricare dalla cartella degli audio encoder | COMBO | Sì | Elenco dei file audio encoder disponibili nella cartella `audio_encoders` |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `audio_encoder` | Il modello audio encoder caricato, pronto per l'uso nei flussi di lavoro di elaborazione audio | AUDIO_ENCODER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/it.md)

---
**Source fingerprint (SHA-256):** `780d0c7fcf571e5ef02d273791e5d2e894baa6d5900d845ed65e9ce669769f7e`

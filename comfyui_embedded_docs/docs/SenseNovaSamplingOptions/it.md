# Opzioni di campionamento SenseNova

SenseNova Sampling Options imposta il flow shift di SenseNova su un modello. Clona il modello di input, allega una configurazione di campionamento del modello SenseNova utilizzando il valore di flow shift scelto e restituisce il modello patchato da usare durante il campionamento.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello a cui viene applicata la configurazione di campionamento con flow shift di SenseNova. | MODEL | Sì | - |
| `shift` | Il valore di flow shift da impostare sul campionamento del modello SenseNova (predefinito: 3.0; passo UI: 0.01). | FLOAT | Sì | Nessun minimo o massimo definito |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `MODEL` | Un clone del modello di input con il flow shift di SenseNova applicato alla sua configurazione di campionamento. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaSamplingOptions/it.md)

---
**Source fingerprint (SHA-256):** `b0dea4a5c226bccb54bb1d70e8ea2791a645018853571429c556034351e9e75a`

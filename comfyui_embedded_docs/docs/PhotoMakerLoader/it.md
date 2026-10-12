# Carica modello PhotoMaker

Il nodo PhotoMakerLoader carica un modello PhotoMaker dai file modello disponibili. Legge il file selezionato, carica i pesi del relativo ID encoder e prepara l'ID encoder di PhotoMaker per l'uso in attività di generazione di immagini basate sull'identità. Questo nodo è contrassegnato come sperimentale ed è destinato a scopi di test.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `photomaker_model_name` | Il nome del file del modello PhotoMaker da caricare. Le opzioni disponibili sono determinate dai file modello presenti nella cartella `photomaker`. | COMBO | Sì | Più opzioni disponibili (popolate dinamicamente dalla cartella `photomaker`) |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `photomaker_model` | Il modello PhotoMaker caricato contenente l'ID encoder, pronto per l'uso nelle operazioni di codifica dell'identità. | PHOTOMAKER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/it.md)

---
**Source fingerprint (SHA-256):** `1b26630fadbdc144cd42ca7393f743b079ee7463deb9c8b31b628b5dc7432317`

# CheckpointLoader

Il nodo CheckpointLoader carica un checkpoint di modello pre-addestrato insieme al relativo file di configurazione. Richiede in input un file di configurazione e un file checkpoint e restituisce i componenti del modello caricati — il modello principale, il modello CLIP e il modello VAE — per l'utilizzo nel workflow. Questo nodo è deprecato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `config_name` | Il file di configurazione che definisce l'architettura e le impostazioni del modello | COMBO | Sì | File di configurazione disponibili |
| `ckpt_name` | Il file checkpoint contenente i pesi e i parametri del modello addestrato | COMBO | Sì | File checkpoint disponibili |

**Nota:** Questo nodo richiede che siano selezionati sia un file di configurazione sia un file checkpoint. Il file di configurazione deve corrispondere all'architettura del file checkpoint caricato.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `MODEL` | Il componente principale del modello caricato, pronto per l'inferenza | MODEL |
| `CLIP` | Il componente del modello CLIP caricato per la codifica del testo | CLIP |
| `VAE` | Il componente del modello VAE caricato per la codifica e la decodifica delle immagini | VAE |

**Nota importante:** Questo nodo è stato contrassegnato come deprecato e potrebbe essere rimosso nelle versioni future. Per i nuovi workflow, valuta la possibilità di utilizzare nodi di caricamento alternativi.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/it.md)

---
**Source fingerprint (SHA-256):** `820cd9f7a5ccd5a70d2b29906c8deca3632d2ccba84ca51022717e061afb72b3`

# Carica Modello MoGe

Carica un modello MoGe (Monocular Geometry) da un file e lo prepara per l'uso in attività di stima della geometria. Il nodo legge il file del modello selezionato dalla cartella `geometry_estimation` e inizializza il modello MoGe con i suoi pesi memorizzati.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model_name` | Il nome del file del modello MoGe da caricare. Seleziona tra i file del modello disponibili nella cartella `geometry_estimation` della tua installazione di ComfyUI. | COMBO | Sì | Elenco dei file del modello disponibili nella cartella `geometry_estimation` |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `MOGE_MODEL` | L'istanza del modello MoGe caricata, pronta per l'uso nei flussi di lavoro di stima della geometria. | MOGE_MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/it.md)

---
**Source fingerprint (SHA-256):** `b5b55f94d3762852d5a1480c0b00d15da4e534adbeb544bf7c47da012e5a6353`

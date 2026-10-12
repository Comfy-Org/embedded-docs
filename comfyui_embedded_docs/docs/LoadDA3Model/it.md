# Carica Depth Anything 3

Il nodo **Load Depth Anything 3** carica un modello Depth Anything 3 da un file, preparandolo per le attività di stima della profondità. È possibile selezionare il file del modello e, facoltativamente, scegliere la precisione numerica (tipo di dati) per i pesi del modello.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_name` | Il nome del file del modello Depth Anything 3 da caricare. | STRING | Sì | Elenco dei file modello disponibili nella cartella `geometry_estimation` |
| `weight_dtype` | La precisione numerica (tipo di dati) per i pesi del modello. "default" usa la precisione originale del modello, "fp16" usa virgola mobile a 16 bit, "bf16" usa bfloat16 e "fp32" usa virgola mobile a 32 bit. (predefinito: "default") | STRING | No | `"default"`<br>`"fp16"`<br>`"bf16"`<br>`"fp32"` |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `DA3_MODEL` | Il modello Depth Anything 3 caricato, pronto per l'uso nei flussi di lavoro di stima della profondità. | DA3_MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadDA3Model/it.md)

---
**Source fingerprint (SHA-256):** `b1b3f4075cd9172bc1f274848b9300bca20d3cbd53b23d3c4a9f0986b36e409e`

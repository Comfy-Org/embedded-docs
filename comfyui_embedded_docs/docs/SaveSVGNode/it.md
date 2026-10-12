# Salva SVG

Salva i file SVG su disco. Questo nodo prende in input dati SVG e li scrive nella directory di output di ComfyUI, gestendo automaticamente la denominazione dei file con suffissi incrementali. Quando le informazioni di prompt del workflow sono disponibili, vengono incorporate direttamente nel file SVG come elemento di metadati.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `svg` | I dati SVG da salvare su disco | SVG | Sì | - |
| `filename_prefix` | Il prefisso per il file da salvare. Può includere informazioni di formattazione come %date:yyyy-MM-dd% o %Empty Latent Image.width% per includere valori dai nodi. (predefinito: "svg/ComfyUI") | STRING | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `svg` | I dati SVG originali, passati attraverso dopo il salvataggio | SVG |
| `ui` | Informazioni sul file salvato, inclusi nome file, sottocartella e tipo, per la visualizzazione nell'interfaccia ComfyUI | DICT |

**Nota:** Questo nodo incorpora automaticamente i metadati del workflow (prompt e informazioni PNG aggiuntive) nel file SVG quando disponibili. I metadati vengono inseriti come sezione CDATA all'interno dell'elemento metadata del file SVG. I file vengono salvati usando il pattern `filename_prefix_00001_.svg`; durante l'elaborazione di un batch, `%batch_num%` nel prefisso viene sostituito con l'indice dell'elemento batch corrente. Il nodo è un nodo di output, quindi produce un risultato salvato nella cartella di output anche se il file stesso non viene visualizzato come anteprima immagine.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/it.md)

---
**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`
